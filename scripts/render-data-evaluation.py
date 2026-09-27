#!/usr/bin/env python3
"""Render the Data category evaluation without changing the canonical catalog."""
from pathlib import Path
import json
import re
import yaml

ROOT=Path(__file__).resolve().parents[1]
REL='evaluations/data/2026-09-27'
BASE=ROOT/REL
DATA=json.loads((BASE/'data.json').read_text())
WEIGHTS=DATA['weights']
PRODUCTS=sorted(DATA['products'],key=lambda p:(-sum(p['score_parts'].values()),p['repo']))
SNAP=yaml.safe_load((ROOT/'snapshot.yaml').read_text())
CAT={e['repo']:e for e in SNAP['entries'] if e['primary_category']=='data'}
assert len(PRODUCTS)==len(CAT)==14
LABELS={'core':'核心结果实测','quality':'数据可信度／时效','coverage':'覆盖与深度','usability':'上手与复现','operations':'运行稳定性'}
NOTICE=('**首轮试用，不是完整功能认证。** 分数衡量这次实际取得的核心结果、数据质量、覆盖、上手与运行表现，'
        '不是盈利评级，也不等于生产环境或商业许可验收。不同角色的元数据库、行情 SDK、新闻管线不可仅凭几分之差互换；'
        '无 Key、周末、空隔离库造成的未验证能力单独说明。目录原分类和锁定版本保持不变。')
OVERVIEW=('**怎么选：** FinanceDatabase 适合查证券代码与分类，不提供价格；AKShare 的已验证历史接口覆盖最广，但必须逐个检查来源时戳；'
          'watchlist 是高可靠的静态研究名单；Datafeed 更适合需要标准化多市场 OHLCV 与来源标记的程序。'
          '这四项排名靠前的原因不同。`trump-code` 的主要用途是事件信号研究，建议在后续目录整理时移往 Trading Strategy／Event Signals。')


def score(p):
    return sum(p['score_parts'].values())


def table(prefix=''):
    lines=['| 排名 | 产品／原仓库 | 分数 | 本轮实际定位 | 实测结论 | 证据 |',
           '|---:|---|---:|---|---|---|']
    for rank,p in enumerate(PRODUCTS,1):
        name=p['repo'].split('/')[-1]
        lines.append(f"| {rank} | [{name}](https://github.com/{p['repo']}) | **{score(p)}/100** | {p['role']} | {p['verdict']} | [判断]({prefix}{p['slug']}/README.md) · [截图]({prefix}{p['slug']}/screenshots.md) |")
    return '\n'.join(lines)


method=f'''# Data 类评分与证据口径

本轮采集于 2026-09-27；评测对象是当天 Trading 目录 Data 栏原有的 14 个仓库。推荐定位只是评测意见，不直接修改 Park OS canonical 分类；`trump-code` 仍计入原 14 项，以免静默删除样本。

{NOTICE}

| 维度 | 上限 | 解释 |
|---|---:|---|
| 核心结果实测 | 35 | 是否亲自取得该产品承诺的主要数据或研究结果；HTTP 200、可见界面或源码函数数量不能代替数据结果。 |
| 数据可信度／时效 | 25 | 原始日期、空值、来源、身份、交叉核对和失败契约；旧价或全空表不得视作实时可用。 |
| 覆盖与深度 | 15 | 已验的市场、数据类型和时间级别；广度只按实测或可核对的静态数据给分。 |
| 上手与复现 | 15 | 安装、文档、搜索、调用、原生 UI／CLI、可追溯版本与失败说明。 |
| 运行稳定性 | 10 | 本轮启动、重复调用、隔离、错误恢复和后台服务表现。 |

分项是人工判断，各产品页保留五项分数与本轮证据；合计必须等于 100 分制总分。排名用于**这轮 Data 产品选择**。FinanceDatabase、watchlist 是静态参考数据，不能替代报价；AKShare 与 Datafeed 可比较历史取数，但接口、许可和可靠性不同。凭证门槛记为“未验证”，不推断上游授权产品自身坏；然而本轮没有数据结果就不能给“核心任务通过”的分数。

## 证据层级

1. **亲自调用有结果**：记录源码版本、输入、返回、来源日期和必要的独立交叉核对。
2. **原生 UI／CLI 可见**：证明入口可运行，不自动证明后台业务结果。
3. **Product Lab 辅助证据页**：用于 SDK、Skill、MCP 和 API 的可读截图，不能冒充上游 UI。
4. **失败、空值、超时和未授权**：保留原状态，不把没有 Key 或周末未验证等同于“不支持”。

每项最少十张不同截图；复杂项目多留图。本轮公开 **297 张**，其中两张因包含本机 checkout 路径而在辅助页重截、原图仍留本地。每张来源和公开 SHA 见 [图片清单](screenshot-inventory.json)。截图数量不等于 297 个功能通过。

## 维护

本目录 `data.json` 是评分、排序和定位的公开源文件。`python3 scripts/render-data-evaluation.py` 可重建 README 区块和所有评测页；`python3 scripts/check-data-evaluation.py` 检查分数、覆盖、图片哈希、路径与 Markdown 链接。Park OS 更新 Trading 目录后，应先运行 Full Trading System 的 `render-evaluations.py`，再运行此脚本，以恢复两个评测区；当前上游目录 exporter 不在此仓库中。
'''
(BASE/'methodology.md').write_text(method)

index='# Trading · Data 类首轮实测与截图\n\n'+NOTICE+'\n\n'+OVERVIEW+'\n\n[评分方法](methodology.md) · [图片清单](screenshot-inventory.json) · [返回 Trading](../../../README.md)\n\n'+table()+'\n\n'
for rank,p in enumerate(PRODUCTS,1):
    entry=CAT[p['repo']]
    folder=BASE/p['slug']
    shots=json.loads((folder/'screenshots.json').read_text())
    probe_path=folder/'evidence/probes.json'
    if not probe_path.exists():probe_path=folder/'evidence/checks.json'
    manifest=json.loads(probe_path.read_text())
    tested=manifest.get('source_sha') or manifest.get('tested_sha') or p['tested_sha']
    lock=(entry.get('content_lock') or {}).get('locked_ref') or 'owned source（目录未设外部锁）'
    parts='\n'.join(f"| {LABELS[k]} | {p['score_parts'][k]}/{WEIGHTS[k]} |" for k in LABELS)
    name=p['repo'].split('/')[-1]
    detail=(f"# {rank}. {name} · {score(p)}/100\n\n{p['verdict']}\n\n"
            f"[原仓库](https://github.com/{p['repo']}) · [全部 {len(shots)} 张截图](screenshots.md) · "
            f"[实测记录](trial-findings.md) · [机器摘要](evidence/{probe_path.name}) · [返回排名](../README.md)\n\n"
            f"![{name} 本轮代表截图](images/{p['hero']})\n\n"
            f"**实际定位：** {p['role']}\n\n**界面来源：** {p['interface']}\n\n"
            f"{NOTICE}\n\n## 评分\n\n| 维度 | 得分 |\n|---|---:|\n{parts}\n| **合计** | **{score(p)}/100** |\n\n"
            f"**判断依据：** {p['why']}\n\n**下一次最有价值的验证：** {p['next']}\n\n"
            f"## 版本与范围\n\n- 实测日期：2026-09-27\n- 实测源码：`{tested}`\n- 目录锁：`{lock}`\n"
            f"- 公开截图：{len(shots)} 张；含空值、失败、辅助页，不代表全部功能通过。\n")
    (folder/'README.md').write_text(detail)
    gallery=(f"# {name} · 全部 {len(shots)} 张截图\n\n[评测判断](README.md) · [数据排名](../README.md)\n\n"
             f"截图采集于 2026-09-27。原生界面与 Product Lab 辅助页逐张标明；后者不属于上游产品 UI。\n\n")
    for i,s in enumerate(shots,1):
        caption=s['file'].removesuffix('.png').replace('-',' ')
        if s['redacted']:caption+=' · 已去除本机路径'
        gallery+=f"## {i:02}. {caption}\n\n来源：**{s['kind']}**。\n\n![{name} · {caption}](images/{s['file']})\n\n"
    (folder/'screenshots.md').write_text(gallery.rstrip()+'\n')
    index+=(f"## {rank}. {name} · {score(p)}/100\n\n{p['verdict']}\n\n"
            f"**{p['role']}** · {p['interface']}\n\n"
            f"[![{name} 代表截图]({p['slug']}/images/{p['hero']})]({p['slug']}/README.md)\n\n"
            f"[判断依据]({p['slug']}/README.md) · [全部截图]({p['slug']}/screenshots.md)\n\n")
(BASE/'README.md').write_text(index.rstrip()+'\n')

block=(f"<!-- EVALUATION:DATA:START -->\n## Data · 首轮实测排名\n\n{NOTICE}\n\n{OVERVIEW}\n\n"
       f"采集：2026-09-27 · 14 个项目 · 297 张截图。"
       f"[统一评测页]({REL}/README.md) · [评分口径]({REL}/methodology.md)。\n\n"
       +table(REL+'/')+'\n\n### 每项代表画面\n\n')
for p in PRODUCTS:
    name=p['repo'].split('/')[-1]
    block+=(f"**[{name}]({REL}/{p['slug']}/README.md) · {score(p)}/100** — {p['verdict']}\n\n"
            f"[![{name}：{p['interface']}]({REL}/{p['slug']}/images/{p['hero']})]({REL}/{p['slug']}/screenshots.md)\n\n")
block+='<!-- EVALUATION:DATA:END -->\n'
readme=(ROOT/'README.md').read_text()
readme=re.sub(r'\n*<!-- EVALUATION:DATA:START -->.*?<!-- EVALUATION:DATA:END -->\n*','\n\n',readme,flags=re.S)
for p in PRODUCTS:
    url='https://github.com/'+p['repo']
    pat=r'(\| \[[^\]]+\]\('+re.escape(url)+r'\))(?: · \[首轮评测\]\([^\n|]+\))?'
    readme=re.sub(pat,lambda m:m.group(1)+f" · [首轮评测]({REL}/{p['slug']}/README.md)",readme)
anchor='<!-- EVALUATION:END -->'
if anchor in readme:
    readme=readme.replace(anchor,anchor+'\n\n'+block,1)
else:
    readme=readme.replace('</div>\n\n','</div>\n\n'+block+'\n',1)
(ROOT/'README.md').write_text(readme)
print('Rendered Data',len(PRODUCTS),'products and',sum(len(json.loads((BASE/p['slug']/'screenshots.json').read_text())) for p in PRODUCTS),'images')
