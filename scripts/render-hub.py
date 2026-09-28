#!/usr/bin/env python3
"""Render the pipeline evaluation hub from evaluations/criteria.json and evaluations/assessments/*.json.

Outputs (all generated, do not hand-edit):
  evaluations/README.md                 pipeline overview across every evaluated product
  evaluations/<category>/README.md      one page per evaluated category: criteria, ranking, cards
  README.md                             the <!-- HUB:START --> ... <!-- HUB:END --> block and per-row card links
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL = ROOT / "evaluations"
CRIT = json.loads((EVAL / "criteria.json").read_text())
STAGES = CRIT["stages"]
STAGE_IDS = [s["id"] for s in STAGES]
CATS = CRIT["categories"]
RATING = CRIT["rating_scale"]
STAGE_SYM = {k: v["symbol"] for k, v in CRIT["stage_scale"].items()}
MIN_VERIFIED = 0.40
MIN_APPLICABLE = 0.60
GEN_NOTE = "<!-- 本文件由 scripts/render-hub.py 生成，请改 evaluations/assessments/*.json 后重跑 -->"

CATALOG_ORDER = [
    "data",
    "equity-research",
    "trading-strategy",
    "trading-infra",
    "dashboard",
    "full-trading-system-agent",
    "knowledge-and-collections",
]
CAT_DIR = {
    "data": "data",
    "equity-research": "equity-research",
    "trading-strategy": "trading-strategy",
    "trading-infra": "trading-infra",
    "dashboard": "dashboard",
    "full-trading-system-agent": "full-trading-system",
    "knowledge-and-collections": "knowledge-and-collections",
}
STATUS_SYM = {"done": "✅", "partial": "🟡", "failed": "❌", "unverified": "⬜"}
STATUS_LABEL = {"done": "做到", "partial": "部分", "failed": "未做到", "unverified": "未验证"}


def slug(repo: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", repo.split("/")[-1].lower()).strip("-")


def load_products() -> list[dict]:
    products = []
    for f in sorted((EVAL / "assessments").glob("*.json")):
        if f.name.startswith("_"):
            continue
        doc = json.loads(f.read_text())
        for p in doc["products"]:
            p["_file"] = f.name
            products.append(p)
    return products


def score(p: dict) -> dict:
    cat = CATS[p["evaluated_as"]]
    total = applicable = verified = 0.0
    counts = {k: 0 for k in RATING}
    for c in cat["criteria"]:
        r = p["criteria"][c["id"]]["rating"]
        counts[r] += 1
        if r == "na":
            continue
        applicable += c["weight"]
        total += c["weight"] * RATING[r]["value"]
        if r in ("done", "partial", "failed"):
            verified += c["weight"]
    if not cat["criteria"] or not applicable:
        return {"score": None, "verified": 0.0, "applicable": 0.0, "ranked": False, "counts": counts}
    ratio = verified / applicable
    app_ratio = applicable / sum(c["weight"] for c in cat["criteria"])
    return {"score": round(total / applicable * 100), "verified": ratio, "applicable": app_ratio, "ranked": ratio >= MIN_VERIFIED and app_ratio >= MIN_APPLICABLE, "counts": counts}


def rank_key(p: dict):
    return (-p["_score"]["score"], -p["_score"]["verified"], p["name"].lower())


def rel(from_dir: Path, target: str) -> str:
    return os.path.relpath(ROOT / target, from_dir).replace(os.sep, "/")


def stage_cells(p: dict) -> str:
    return " | ".join(STAGE_SYM[p["stages"][s]] for s in STAGE_IDS)


def stage_compact(p: dict) -> str:
    return "`" + "".join(STAGE_SYM[p["stages"][s]] for s in STAGE_IDS) + "`"


def stage_header() -> tuple[str, str]:
    head = " | ".join(f"{s['n']} {s['short']}" for s in STAGES)
    sep = " | ".join(":--:" for _ in STAGES)
    return head, sep


def record_link(p: dict, from_dir: Path) -> str | None:
    if not p.get("evidence_dir"):
        return None
    d = ROOT / p["evidence_dir"]
    for name in ("findings.md", "trial-findings.md", "README.md"):
        if (d / name).is_file():
            return rel(from_dir, f"{p['evidence_dir']}/{name}")
    return None


def gallery_link(p: dict, from_dir: Path) -> tuple[str | None, int]:
    if not p.get("evidence_dir"):
        return None, 0
    d = ROOT / p["evidence_dir"]
    n = len([f for f in (d / "images").glob("*") if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")]) if (d / "images").is_dir() else 0
    if (d / "screenshots.md").is_file():
        return rel(from_dir, f"{p['evidence_dir']}/screenshots.md"), n
    return None, n


def product_link(p: dict, from_dir: Path) -> str:
    """Markdown link to a product's card, or to its evidence record when its category has no page."""
    if p["evaluated_as"] == "knowledge-and-collections":
        recl = record_link(p, from_dir)
        return f"[{p['name']}]({recl})" if recl else f"[{p['name']}](https://github.com/{p['repo']})"
    page = rel(from_dir, f"evaluations/{CAT_DIR[p['evaluated_as']]}/README.md")
    return f"[{p['name']}]({page}#{slug(p['repo'])})"


def short_status(p: dict) -> str:
    return f"{STATUS_SYM[p['delivered']['status']]} {p['delivered']['summary']}"


def card(p: dict, rank: int | None, from_dir: Path) -> str:
    cat = CATS[p["evaluated_as"]]
    sc = p["_score"]
    head = f"{rank}. " if rank else ""
    score_txt = f"{sc['score']}/100 · 已验证 {round(sc['verified']*100)}%" if sc["score"] is not None else "不排名"
    out = [f'<a id="{slug(p["repo"])}"></a>', f"### {head}{p['name']} · {score_txt}", ""]
    if p.get("hero") and p.get("evidence_dir"):
        gal, _ = gallery_link(p, from_dir)
        img = rel(from_dir, f"{p['evidence_dir']}/{p['hero']}")
        out.append(f'<a href="{gal or img}"><img src="{img}" alt="{p["name"]} 代表截图" width="560"></a>')
        out.append("")
    h, s = stage_header()
    out += [f"| {h} |", f"| {s} |", f"| {stage_cells(p)} |", ""]
    out.append(f"**声称：** {p['claimed']}")
    out.append("")
    out.append(f"**实测：** {short_status(p)}")
    out.append("")
    if cat["criteria"]:
        out += ["| 标准 | 权重 | 评级 | 证据 |", "|---|---:|:--:|---|"]
        for c in cat["criteria"]:
            r = p["criteria"][c["id"]]
            shots = ""
            if p.get("evidence_dir"):
                links = [f"[图{i+1}]({rel(from_dir, p['evidence_dir'] + '/' + sfile)})" for i, sfile in enumerate(r.get("shots", []))]
                shots = (" " + " ".join(links)) if links else ""
            out.append(f"| {c['id']} {c['name']} | {c['weight']} | {RATING[r['rating']]['symbol']} | {r['evidence']}{shots} |")
        out.append("")
    out.append(f"**适合：** {p['best_for']}  \n**不适合：** {p['not_for']}")
    out.append("")
    unv = "；".join(p.get("unverified") or []) or "无"
    out.append(f"**未验证：** {unv}  \n**下一步：** {p['next']}")
    out.append("")
    bits = []
    gal, n = gallery_link(p, from_dir)
    if gal:
        bits.append(f"[{n} 张截图]({gal})")
    recl = record_link(p, from_dir)
    if recl:
        bits.append(f"[实测记录]({recl})")
    if p.get("tested_revision"):
        bits.append(f"实测版本 `{str(p['tested_revision'])[:12]}`")
    if p.get("catalog_lock"):
        bits.append(f"目录锁 `{str(p['catalog_lock'])[:12]}`")
    bits.append(p["interface"])
    if p.get("markets"):
        bits.append("、".join(p["markets"]))
    out.append("证据：" + " · ".join(bits))
    if p["catalog_category"] != p["evaluated_as"]:
        out.append("")
        out.append(f"目录归 **{CATS[p['catalog_category']]['name']}**，按 **{cat['name']}** 标准评测；分类建议不改 canonical 目录。")
    if p.get("notes"):
        out.append("")
        out.append(f"备注：{p['notes']}")
    out.append("")
    return "\n".join(out)


def ranking_table(products: list[dict], from_dir: Path, page: str) -> str:
    rows = ["| 排名 | 产品 | 分数 | 已验证 | 环节 1–10 | 实测 | 卡片 |", "|---:|---|---:|---:|---|---|---|"]
    for i, p in enumerate(products, 1):
        sc = p["_score"]
        rows.append(
            f"| {i} | [{p['name']}](https://github.com/{p['repo']}) | **{sc['score']}** | {round(sc['verified']*100)}% | {stage_compact(p)} | {short_status(p)} | [卡片]({page}#{slug(p['repo'])}) |"
        )
    return "\n".join(rows)


def unranked_table(products: list[dict], page: str) -> str:
    rows = ["| 产品 | 原因 | 卡片 |", "|---|---|---|"]
    for p in products:
        sc = p["_score"]
        if not p.get("evidence_dir"):
            why = "按要求跳过"
        elif sc["applicable"] < MIN_APPLICABLE:
            why = f"本类标准只有 {round(sc['applicable']*100)}% 适用，不属于本类产品"
            if p.get("suggested_category"):
                why += f"，建议归 {CATS[p['suggested_category']]['name']}"
        else:
            why = f"已验证 {round(sc['verified']*100)}%，低于 {int(MIN_VERIFIED*100)}%"
        rows.append(f"| [{p['name']}](https://github.com/{p['repo']}) | {why}：{p['delivered']['summary']} | [卡片]({page}#{slug(p['repo'])}) |")
    return "\n".join(rows)


def criteria_table(cat: dict) -> str:
    rows = ["| 标准 | 权重 | 怎么判 |", "|---|---:|---|"]
    for c in cat["criteria"]:
        rows.append(f"| {c['id']} {c['name']} | {c['weight']} | {c['test']} |")
    return "\n".join(rows)


def render_category(cat_id: str, products: list[dict], all_products: list[dict]) -> Path:
    cat = CATS[cat_id]
    page_dir = EVAL / CAT_DIR[cat_id]
    page_dir.mkdir(exist_ok=True)
    page = page_dir / "README.md"
    ranked = sorted([p for p in products if p["_score"]["ranked"]], key=rank_key)
    unranked = [p for p in products if not p["_score"]["ranked"]]
    stage_names = "、".join(f"{s['n']} {s['name']}" for s in STAGES if s["id"] in cat["stages"])
    rounds = sorted({p["evidence_dir"].rsplit("/", 1)[0] for p in products if p.get("evidence_dir")})
    moved_out = [p for p in all_products if p["catalog_category"] == cat_id and p["evaluated_as"] != cat_id]
    moved_in = [p for p in products if p["catalog_category"] != cat_id]

    out = [GEN_NOTE, f"# {cat['name']} · 评测", "", f"**目标：** {cat['objective']}", "", f"**环节：** {stage_names}", ""]
    out.append(f"[评测框架](../FRAMEWORK.md) · [Pipeline 总览](../README.md) · [返回目录](../../README.md)")
    out.append("")
    out.append("评级：✅ 做到 · 🟡 部分 · ❌ 未做到 · ⬜ 未验证 · — 不适用。分数 = Σ(权重 × 评级值) ÷ Σ适用权重 × 100；已验证 = 做到、部分、未做到三种评级占适用权重的比例。环节：● 实测跑通 · ◐ 源码可见未实测 · ○ 无 · · 不在其角色内；排名表的环节列按 1 获取到 10 看板的顺序排列。")
    out.append("")
    out += ["## 评判标准", "", criteria_table(cat), ""]
    out += ["## 排名", ""]
    if cat.get("reading_note"):
        out += [f"**怎么读这个排名：** {cat['reading_note']}", ""]
    if ranked:
        out.append(ranking_table(ranked, page_dir, "README.md"))
    else:
        out.append("本类本轮没有达到排名门槛的产品。")
    out.append("")
    if unranked:
        out += ["### 证据不足，不排名", "", unranked_table(unranked, "README.md"), ""]
    if moved_in or moved_out:
        out += ["## 分类说明", ""]
        for p in moved_in:
            out.append(f"- **{p['name']}** 目录归 {CATS[p['catalog_category']]['name']}，按本类标准评测并参与本类排名。")
        for p in moved_out:
            if p["evaluated_as"] == "knowledge-and-collections":
                out.append(f"- **{p['name']}** 目录归本类，建议归 Knowledge & Collections，不评分；实测记录见 {product_link(p, page_dir)}。")
            else:
                out.append(f"- **{p['name']}** 目录归本类，按 {CATS[p['evaluated_as']]['name']} 标准评测，见 {product_link(p, page_dir)}。")
        out.append("")
    out += ["## 产品卡片", ""]
    for i, p in enumerate(ranked, 1):
        out.append(card(p, i, page_dir))
    for p in unranked:
        out.append(card(p, None, page_dir))
    if rounds:
        out += ["## 原始证据", ""]
        for r in rounds:
            out.append(f"- [{r}](../../{r}/README.md)：该轮的实测记录、截图与首轮人工分，保留供复核。")
        out.append("")
    page.write_text("\n".join(out).rstrip() + "\n")
    return page


def render_hub(products: list[dict]) -> None:
    page = EVAL / "README.md"
    by_cat: dict[str, list[dict]] = {}
    for p in products:
        by_cat.setdefault(p["evaluated_as"], []).append(p)
    out = [GEN_NOTE, "# Trading · Pipeline 评测总览", ""]
    out.append("每个库放到交易 pipeline 的对应环节，按该环节的标准评判它是否做到了自己声称的用途，证据是首轮实测的截图与记录。标准与分数推导见 [评测框架](FRAMEWORK.md)。")
    out.append("")
    out += ["## Pipeline 十个环节与已实测跑通的产品", ""]
    out += ["| # | 环节 | 输入 → 输出 | 实测跑通 ● | 源码可见 ◐ |", "|---:|---|---|---|---|"]
    for s in STAGES:
        run = [p for p in products if p["stages"][s["id"]] == "run" and not p.get("stub")]
        code = [p for p in products if p["stages"][s["id"]] == "code" and not p.get("stub")]
        run.sort(key=lambda p: -(p["_score"]["score"] or 0))
        run_txt = "、".join(product_link(p, EVAL) for p in run) or "—"
        code_txt = "、".join(p["name"] for p in code) or "—"
        out.append(f"| {s['n']} | {s['name']} | {s['io']} | {run_txt} | {code_txt} |")
    out.append("")
    out += ["## 按类别", ""]
    out += ["| 类别 | 目标 | 评测数 | 已排名 | 类内首位 | 页面 |", "|---|---|---:|---:|---|---|"]
    for cid in CATALOG_ORDER:
        cat = CATS[cid]
        ps = [p for p in by_cat.get(cid, []) if not p.get("stub")]
        if cid == "knowledge-and-collections":
            names = "、".join(product_link(p, EVAL) for p in ps)
            out.append(f"| {cat['name']} | {cat['objective']} | — | — | 不评测{'；建议归入：' + names if names else ''} | — |")
            continue
        ranked = sorted([p for p in ps if p["_score"]["ranked"]], key=rank_key)
        top = f"[{ranked[0]['name']}]({CAT_DIR[cid]}/README.md#{slug(ranked[0]['repo'])}) · {ranked[0]['_score']['score']}" if ranked else "—"
        out.append(f"| {cat['name']} | {cat['objective']} | {len(ps)} | {len(ranked)} | {top} | [打开]({CAT_DIR[cid]}/README.md) |")
    out.append("")
    moved = [p for p in products if p["catalog_category"] != p["evaluated_as"] and not p.get("stub")]
    suggested = [p for p in products if p.get("suggested_category") and p["suggested_category"] != p["catalog_category"] and p["evaluated_as"] == p["catalog_category"]]
    if moved or suggested:
        out += ["## 分类建议", "", "评测意见，不改 canonical 目录。", "", "| 产品 | 目录类别 | 建议类别 | 说明 |", "|---|---|---|---|"]
        for p in moved + suggested:
            target = p["evaluated_as"] if p in moved else p["suggested_category"]
            note = p.get("notes") or p["delivered"]["summary"]
            link = product_link(p, EVAL)
            out.append(f"| {link} | {CATS[p['catalog_category']]['name']} | {CATS[target]['name']} | {note} |")
        out.append("")
    out += ["## 全部产品", "", "环节列按 1 获取、2 清洗、3 存档、4 指标、5 策略、6 回测、7 管理、8 风控、9 执行、10 看板的顺序排列：● 实测跑通 · ◐ 源码可见 · ○ 无 · · 不在角色内。", ""]
    out += ["| 产品 | 评测类别 | 分数 | 已验证 | 环节 1–10 | 实测 |", "|---|---|---:|---:|---|---|"]
    allp = sorted([p for p in products if not p.get("stub")], key=lambda p: (CATALOG_ORDER.index(p["evaluated_as"]), -(p["_score"]["score"] or -1), p["name"].lower()))
    for p in allp:
        sc = p["_score"]
        score_txt = str(sc["score"]) if sc["score"] is not None else "—"
        ver_txt = f"{round(sc['verified']*100)}%" if sc["score"] is not None else "—"
        out.append(f"| {product_link(p, EVAL)} | {CATS[p['evaluated_as']]['name']} | {score_txt} | {ver_txt} | {stage_compact(p)} | {short_status(p)} |")
    out.append("")
    out += ["## 原始证据轮次", ""]
    rounds = sorted({p["evidence_dir"].rsplit("/", 1)[0] for p in products if p.get("evidence_dir")})
    for r in rounds:
        out.append(f"- [{r}]({r.split('/',1)[1]}/README.md)")
    out.append("")
    page.write_text("\n".join(out).rstrip() + "\n")


def render_root(products: list[dict]) -> None:
    readme_path = ROOT / "README.md"
    readme = readme_path.read_text()
    # retire the two first-round blocks
    readme = re.sub(r"\n*<!-- EVALUATION:START -->.*?<!-- EVALUATION:END -->\n*", "\n\n", readme, flags=re.S)
    readme = re.sub(r"\n*<!-- EVALUATION:DATA:START -->.*?<!-- EVALUATION:DATA:END -->\n*", "\n\n", readme, flags=re.S)
    readme = re.sub(r"\n*<!-- HUB:START -->.*?<!-- HUB:END -->\n*", "\n\n", readme, flags=re.S)
    by_cat: dict[str, list[dict]] = {}
    for p in products:
        if not p.get("stub"):
            by_cat.setdefault(p["evaluated_as"], []).append(p)
    lines = ["<!-- HUB:START -->", "## 按交易 pipeline 评测", ""]
    lines.append("每个库回答三个问题：在交易 pipeline 的哪一环、是否做到了自己声称的用途、证据是什么。标准按环节事先定义，分数从标准评级机械推导，只在同类内可比；不代表盈利能力或生产成熟度。")
    lines.append("")
    stage_txt = " → ".join(f"{s['n']} {s['name']}" for s in STAGES)
    lines.append(f"Pipeline：{stage_txt}")
    lines.append("")
    lines.append("[Pipeline 总览](evaluations/README.md) · [评测框架与标准](evaluations/FRAMEWORK.md)")
    lines.append("")
    lines += ["| 类别 | 目标 | 评测数 | 类内首位 | 页面 |", "|---|---|---:|---|---|"]
    for cid in CATALOG_ORDER:
        cat = CATS[cid]
        ps = by_cat.get(cid, [])
        if cid == "knowledge-and-collections":
            lines.append(f"| {cat['name']} | {cat['objective']} | — | — | — |")
            continue
        ranked = sorted([p for p in ps if p["_score"]["ranked"]], key=rank_key)
        top = f"[{ranked[0]['name']}](evaluations/{CAT_DIR[cid]}/README.md#{slug(ranked[0]['repo'])}) · {ranked[0]['_score']['score']}" if ranked else "—"
        lines.append(f"| {cat['name']} | {cat['objective']} | {len(ps)} | {top} | [打开](evaluations/{CAT_DIR[cid]}/README.md) |")
    lines.append("")
    lines.append("<!-- HUB:END -->")
    block = "\n".join(lines)
    readme = readme.replace("</div>\n\n", "</div>\n\n" + block + "\n\n", 1)
    # per-row card links
    for p in products:
        url = "https://github.com/" + p["repo"]
        pat = r"(\| \[[^\]]+\]\(" + re.escape(url) + r"\))(?: · \[(?:首轮评测|评测)\]\([^\n|]+\))?"
        target = f"evaluations/{CAT_DIR[p['evaluated_as']]}/README.md#{slug(p['repo'])}"
        if p.get("stub") or (p["evaluated_as"] == "knowledge-and-collections"):
            continue
        readme = re.sub(pat, lambda m: m.group(1) + f" · [评测]({target})", readme)
    readme = re.sub(r"\n{3,}", "\n\n", readme)
    readme_path.write_text(readme)


def main() -> None:
    products = load_products()
    for p in products:
        p["_score"] = score(p) if not p.get("stub") else {"score": None, "verified": 0.0, "applicable": 0.0, "ranked": False, "counts": {}}
    by_cat: dict[str, list[dict]] = {}
    for p in products:
        if not p.get("stub"):
            by_cat.setdefault(p["evaluated_as"], []).append(p)
    for cid in CATALOG_ORDER:
        if cid == "knowledge-and-collections":
            continue
        render_category(cid, by_cat.get(cid, []), [p for p in products if not p.get("stub")])
    render_hub(products)
    render_root(products)
    n = len([p for p in products if not p.get("stub")])
    print(f"Rendered {n} product cards across {len(by_cat)} categories")


if __name__ == "__main__":
    main()
