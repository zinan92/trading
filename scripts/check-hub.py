#!/usr/bin/env python3
"""Validate evaluations/criteria.json, evaluations/assessments/*.json and the pages render-hub.py generates."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EVAL = ROOT / "evaluations"
CRIT = json.loads((EVAL / "criteria.json").read_text())
STAGE_IDS = [s["id"] for s in CRIT["stages"]]
RATINGS = set(CRIT["rating_scale"])
STAGE_VALUES = set(CRIT["stage_scale"])
CAT_DIR = {
    "data": "data",
    "equity-research": "equity-research",
    "trading-strategy": "trading-strategy",
    "trading-infra": "trading-infra",
    "dashboard": "dashboard",
    "full-trading-system-agent": "full-trading-system",
    "knowledge-and-collections": "knowledge-and-collections",
}
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


# criteria weights
for cid, cat in CRIT["categories"].items():
    if cat["criteria"] and sum(c["weight"] for c in cat["criteria"]) != 100:
        err(f"criteria {cid}: weights do not sum to 100")
    for s in cat["stages"]:
        if s not in STAGE_IDS:
            err(f"criteria {cid}: unknown stage {s}")

# assessments
products: list[dict] = []
for f in sorted((EVAL / "assessments").glob("*.json")):
    if f.name.startswith("_"):
        continue
    doc = json.loads(f.read_text())
    for p in doc["products"]:
        p["_file"] = f.name
        products.append(p)

stubs = [p for p in products if p.get("stub")]
products_full = [p for p in products if not p.get("stub")]
repos = [p["repo"] for p in products_full]
for s in stubs:
    if s["repo"] not in repos:
        err(f"stub for {s['repo']} has no full card elsewhere")
if len(repos) != len(set(repos)):
    dup = {r for r in repos if repos.count(r) > 1}
    err(f"duplicate products across assessments: {sorted(dup)}")

snapshot = yaml.safe_load((ROOT / "snapshot.yaml").read_text())
catalog = {e["repo"]: e["primary_category"] for e in snapshot["entries"]}
expected = {r for r, c in catalog.items() if c != "knowledge-and-collections"}
missing = expected - set(repos)
extra = set(repos) - set(catalog)
if missing:
    err(f"catalog entries without a card: {sorted(missing)}")
if extra:
    err(f"cards for repos not in catalog: {sorted(extra)}")

REQUIRED = ["repo", "name", "catalog_category", "evaluated_as", "claimed", "delivered", "stages", "criteria", "best_for", "not_for", "next", "interface"]
for p in products:
    tag = f"{p['_file']}:{p.get('repo')}"
    for k in REQUIRED:
        if k not in p:
            err(f"{tag}: missing field {k}")
    if p.get("repo") in catalog and p.get("catalog_category") != catalog[p["repo"]]:
        err(f"{tag}: catalog_category {p.get('catalog_category')} != snapshot {catalog[p['repo']]}")
    if p.get("evaluated_as") not in CRIT["categories"]:
        err(f"{tag}: unknown evaluated_as {p.get('evaluated_as')}")
        continue
    if p.get("delivered", {}).get("status") not in ("done", "partial", "failed", "unverified"):
        err(f"{tag}: bad delivered.status")
    stages = p.get("stages", {})
    if set(stages) != set(STAGE_IDS):
        err(f"{tag}: stages keys must be exactly {STAGE_IDS}")
    for k, v in stages.items():
        if v not in STAGE_VALUES:
            err(f"{tag}: stage {k} has bad value {v}")
    if p.get("stub"):
        continue
    cat = CRIT["categories"][p["evaluated_as"]]
    want = {c["id"] for c in cat["criteria"]}
    got = set(p.get("criteria", {}))
    if want != got:
        err(f"{tag}: criteria ids {sorted(got)} != {sorted(want)}")
    ev_dir = ROOT / p["evidence_dir"] if p.get("evidence_dir") else None
    if ev_dir is not None and not ev_dir.is_dir():
        err(f"{tag}: evidence_dir missing {p['evidence_dir']}")
    for cid_, r in p.get("criteria", {}).items():
        if r.get("rating") not in RATINGS:
            err(f"{tag}: {cid_} bad rating {r.get('rating')}")
        if not r.get("evidence"):
            err(f"{tag}: {cid_} has no evidence text")
        if r.get("rating") in ("done", "partial", "failed") and not r.get("shots"):
            err(f"{tag}: {cid_} rated {r['rating']} but cites no screenshot or record")
        for s in r.get("shots", []):
            if ev_dir is None or not (ev_dir / s).is_file():
                err(f"{tag}: {cid_} cites missing file {s}")
    if p.get("hero") and (ev_dir is None or not (ev_dir / p["hero"]).is_file()):
        err(f"{tag}: hero missing {p['hero']}")
    if p.get("suggested_category") and p["suggested_category"] not in CRIT["categories"]:
        err(f"{tag}: bad suggested_category")
    blob = json.dumps(p, ensure_ascii=False)
    if "/Users/" in blob:
        err(f"{tag}: contains a local absolute path")

# generated pages exist and links resolve
pages = [ROOT / "README.md", EVAL / "README.md", EVAL / "FRAMEWORK.md"]
for cid, d in CAT_DIR.items():
    if cid == "knowledge-and-collections":
        continue
    page = EVAL / d / "README.md"
    if not page.is_file():
        err(f"missing generated page {page.relative_to(ROOT)}")
    else:
        pages.append(page)
readme = (ROOT / "README.md").read_text()
if readme.count("<!-- HUB:START -->") != 1 or readme.count("<!-- HUB:END -->") != 1:
    err("root README must contain exactly one HUB block")
for old in ("<!-- EVALUATION:START -->", "<!-- EVALUATION:DATA:START -->"):
    if old in readme:
        err(f"root README still contains retired block {old}; run scripts/render-hub.py last")
for f in pages:
    txt = f.read_text()
    if "/Users/" in txt:
        err(f"{f.relative_to(ROOT)}: contains a local absolute path")
    anchors = set(re.findall(r'<a id="([^"]+)"></a>', txt))
    for target in re.findall(r"\]\(([^)\s]+)\)", txt) + re.findall(r'(?:href|src)="([^"]+)"', txt):
        if re.match(r"https?://|mailto:", target):
            continue
        path, _, frag = target.partition("#")
        dest = (f.parent / path) if path else f
        if not dest.exists():
            err(f"{f.relative_to(ROOT)}: broken link {target}")
            continue
        if frag and dest.suffix == ".md":
            dest_txt = txt if dest == f else dest.read_text()
            if f'<a id="{frag}"></a>' not in dest_txt:
                err(f"{f.relative_to(ROOT)}: missing anchor {target}")

if errors:
    print("\n".join(errors))
    print(f"FAIL: {len(errors)} problem(s)")
    sys.exit(1)
n_ranked = 0
print(f"PASS: {len(products)} cards cover {len(expected)} evaluated catalog entries; criteria, evidence files, pages and links verified")
