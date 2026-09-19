#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
python3 - "$ROOT" <<'PY'
from pathlib import Path
import datetime as dt
import re
import sys
import yaml

root = Path(sys.argv[1])
registry = yaml.safe_load((root / "registry.yaml").read_text())
snapshot = yaml.safe_load((root / "snapshot.yaml").read_text())
entries = snapshot["entries"]
universe = registry["universe"]
assert registry["registry_repo"] is True
assert registry["registry_role"] == "public_scoped"
assert registry["catalog_order"] == "category_then_added_desc"
assert registry["catalog_time_source"] == "owned_created_at_external_starred_at"
assert snapshot["universe"] == universe
assert snapshot["snapshot_id"] == registry["canonical_snapshot"]
assert snapshot["generated_from"] == "zinan92/park-operating-system"
assert snapshot["export_checksum"] == registry["export_checksum"]
assert len({item["repo"] for item in entries}) == len(entries)
assert entries and all(item["universe"] == universe for item in entries)
assert all(re.fullmatch(r"https://github\.com/[^/ ]+/[^/ ]+", item["source_url"]) for item in entries)
assert all(item["primary_category"] for item in entries)
assert all(item["status"] in {"READY", "BUILDING", "EXPLORING"} for item in entries)
assert all(item["review_status"] in {"confirmed", "needs_review"} for item in entries)
category_order = ["data", "equity-research", "trading-strategy", "trading-infra", "dashboard", "full-trading-system-agent", "knowledge-and-collections"]
sort_keys = []
for item in entries:
    timestamp = dt.datetime.fromisoformat(item["catalog_added_at"].replace("Z", "+00:00"))
    sort_keys.append((category_order.index(item["primary_category"]), -timestamp.timestamp(), item["repo"].lower()))
assert sort_keys == sorted(sort_keys)
external_ids = {item["repo"] for item in entries if not item["owned"]}
owned_ids = {item["repo"] for item in entries if item["owned"] and not item["archived"]}
starred_ids = {item["repo"] for item in entries if item["starred"] and not item["owned"] and not item["archived"]}
archived_ids = {item["repo"] for item in entries if item["archived"]}
owned_projection = {item["repo"] for item in yaml.safe_load((root / "entries/owned.yaml").read_text())["entries"]}
starred_projection = {item["repo"] for item in yaml.safe_load((root / "entries/starred.yaml").read_text())["entries"]}
archived_projection = {item["repo"] for item in yaml.safe_load((root / "entries/archived.yaml").read_text())["entries"]}
assert owned_projection == owned_ids
assert starred_projection == starred_ids
assert archived_projection == archived_ids
assert not owned_projection & starred_projection
assert not archived_projection & (owned_projection | starred_projection)
locks = yaml.safe_load((root / "locks/sources.lock.yaml").read_text())["locks"]
assert {item["repo"] for item in locks} == external_ids
assert all(item["content_lock"]["locked_ref"] and len(item["content_lock"]["locked_ref"]) == 40 for item in locks)
tags = set(yaml.safe_load((root / "tags.yaml").read_text())["tags"])
assert all(set(item.get("tags", [])) <= tags for item in entries)
print(f"PASS: {universe} scoped registry ({len(entries)} entries)")
PY
