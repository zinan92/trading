#!/usr/bin/env python3
"""Rebuild the first-round evaluation overlay after canonical catalog refreshes."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REL='evaluations/full-trading-system/2026-09-26'
BASE=ROOT/REL
D=json.loads((BASE/'data.json').read_text())
P=sorted(D['products'],key=lambda p:(-p['score'],p['repo']))
LABELS={'coverage':'完整系统能力覆盖','core_results':'本轮核心任务结果','delivery':'部署与操作交付','execution_verified':'实际订单/持仓闭环'}
NOTICE='**首轮试用，非完整功能认证。** 评分为人工的“完整交易产品适配＋本轮已验证可用性”分，不是盈利能力、生产成熟度或 repo-evals 通用分。试用配置与深度不完全一致；未测不等于不支持，几分差距不代表显著优劣。所有产品本轮订单/持仓闭环均未实测通过，该项统一 **0/15**。框架、模型、技能库保留在原样本中；其低分可能源于完整系统定位不匹配，不等于该工具不可用。'
def link(p,prefix=''):
 return prefix+p['slug']+'/README.md'
def table(prefix=''):
 rows=['| 排名 | 产品 · 原仓库 | 分数 | 实际定位 | 本轮结论 | 评测与全部截图 |','|---:|---|---:|---|---|---|']
 for rank,p in enumerate(P,1):
  name=p['repo'].split('/')[-1]
  rows.append(f"| {rank} | [{name}](https://github.com/{p['repo']}) | **{p['score']}/100** | {p['category_assessment']} | {p['status']} | [判断与证据]({link(p,prefix)}) · [图库]({prefix}{p['slug']}/screenshots.md) |")
 return '\n'.join(rows)
method='''# 评分与证据口径

本轮采集于 2026-09-26，整理发布于 2026-09-27。范围是原 Full Trading System / Agent 分组的 14 项，而不是全部 Trading catalog。推荐定位只是评测意见，canonical 分类和版本锁保持不变。

'''+NOTICE+'''

| 分项 | 上限 | 评分依据 |
|---|---:|---|
| 完整系统能力覆盖 | 35 | 数据、研究/策略、回测、模拟或券商执行、持仓风控、监控是否构成可操作系统；源码能力与运行验证分别记录。框架、模型、技能等专用工具此项会低，不表示其领域质量差。 |
| 本轮核心任务结果 | 30 | 真实数据、策略及回测的实际结果；只有界面或模拟适配展示不给同等分。 |
| 部署与操作交付 | 20 | 本轮安装运行、入口、持久化、交互和失败恢复的表现。 |
| 实际订单/持仓闭环 | 15 | 必须实际看到下单、成交与现金/持仓回读。本轮全为 0。 |

分项为评测者人工判断，数据源是 `data.json`，不是自动测量值。各页列出逐项理由，四项相加得到总分。排序优先服务本轮完整产品选型，不能跨类别解释成通用质量榜。Tick Stock Panel、QuantDinger、Vibe-Trading 的分项沿用讨论后的口径；其余项目按相同四项补全。

## 证据分级

- **操作成功并有结果**：本轮亲自执行并记录输出。结果正确性/长期效果仍须单独验证。
- **界面可见 / 源码可见**：只证明界面或实现存在，不等于功能通过。
- **尝试失败**：记录当时版本、环境和失败范围，不推断所有环境都失败。
- **尚未测试**：不当成“不支持”。账户、key 或数据订阅未配置单独说明。

## 图片来源

每张图标明原生产品、原生 CLI、用户手动截图或 Product Lab 辅助页。fomomo 的本轮页面为模拟适配；Sequoia-X、finance-quant-skills、TradingAgents 的网页为辅助试用台，不能当作上游原生 Web UI。空白、加载、错误状态会保留并说明，不能作为功能成功证据。

公开图片按像素去重，适度缩放压缩；本机路径与联系标识使用可见遮盖处理，坐标记录在清单中；手动桌面截图仅保留相关产品区域。上传探针、无关桌面和无法安全分离的私密画面不公开。原始文件及未公开项仍在本地证据档案中。`screenshot-inventory.json` 记录每个原文件的哈希、公开/去重/剔除处置与原因；截图数量不是测试覆盖率。

## 版本与复现

每页分别记录 catalog lock 与实际试用 revision/release，两者可能不同。结论只绑定本轮试用版本。`evidence.json` 为公开清理后的本轮机器记录；删除本机绝对路径、凭据文件位置和环境内部细节，保留运行结果与限制。

## 维护

修改 `data.json` 后执行 `python3 scripts/render-evaluations.py`。Park OS 导出 README 后同样重跑此命令恢复评测区和原表中的详情链接；本地导出工具不属于此仓库，因此这里不声称已改造上游 exporter。运行 `python3 scripts/check-evaluations.py` 和 `bash scripts/verify-scoped.sh` 验证。评测路径按轮次归档，后续轮次不能覆盖本轮证据。
'''
(BASE/'methodology.md').write_text(method)
index='# Trading Systems · 首轮实测与截图\n\n'+NOTICE+'\n\n[评分方法](methodology.md) · [图片处理清单](screenshot-inventory.json) · [返回 Trading](../../../README.md)\n\n'+table()+'\n\n'
for rank,p in enumerate(P,1):
 name=p['repo'].split('/')[-1]; folder=BASE/p['slug']; folder.mkdir(exist_ok=True)
 shots=p['screenshots']; hero=p.get('hero') or (shots[0]['file'] if shots else None)
 p['rank']=rank
 points='\n'.join(f"| {LABELS[k]} | {p['score_parts'][k]}/{D['weights'][k]} | {p['score_reason'][k]} |" for k in LABELS)
 doc=f"# {rank}. {name} · {p['score']}/100\n\n{p['summary']}\n\n[原仓库](https://github.com/{p['repo']}) · [全部 {len(shots)} 张公开截图](screenshots.md) · [证据记录](evidence.json) · [返回排名](../README.md)\n\n"
 if hero:doc+=f"![{name}：{p['interface']}](images/{hero})\n\n"
 doc+=f"**定位判断：** {p['category_assessment']}\n\n**本轮状态：** {p['status']}\n\n**界面来源：** {p['interface']}\n\n**素材与依赖：** {p['materials']}\n\n{NOTICE}\n\n## 本轮得分\n\n| 分项 | 得分 | 依据 |\n|---|---:|---|\n{points}\n\n"
 for label,key in [('操作成功并有结果','verified'),('尝试失败 / 问题记录','issues'),('尚未验证','unverified')]:
  doc+='## '+label+'\n\n'+('\n'.join('- '+x for x in p[key]) if p[key] else ('本轮未取得原生核心任务成功结果。' if key=='verified' else '本轮没有另行确认的运行失败；未配置和未测试不记作产品故障。'))+'\n\n'
 doc+=f"## 下一次最有价值的验证\n\n{p['next_step']}\n\n## 试用版本\n\n- 采集日期：2026-09-26\n- 实际试用：`{p['tested_revision']}`\n- 原目录 lock：`{p.get('catalog_lock','未记录')}`（仅作来源对照，不替代实际试用版本）\n- 公开图库：{len(shots)} 张；包含失败或未配置画面，不代表所有页面功能通过。\n"
 (folder/'README.md').write_text(doc.rstrip()+'\n')
 gallery=f"# {name} · 完整公开图库\n\n[评测判断](README.md) · [总排名](../README.md)\n\n采集于 2026-09-26，共 {len(shots)} 张经去重/公开处理的图片。界面可见不等于功能通过。{p['materials']}。\n\n"
 for i,s in enumerate(shots,1):
  gallery+=f"## {i:02}. {s['caption']}\n\n来源：**{s['kind']}**。{s.get('note','')}\n\n![{s['caption']}](images/{s['file']})\n\n"
 (folder/'screenshots.md').write_text(gallery.rstrip()+'\n')
 index+=f"## {rank}. {name} · {p['score']}/100\n\n{p['summary']}\n\n**{p['category_assessment']}** · {p['interface']}\n\n"
 if hero:index+=f"[![{name} 代表截图]({p['slug']}/images/{hero})]({link(p)})\n\n"
 index+=f"[完整判断]({link(p)}) · [全部截图]({p['slug']}/screenshots.md)\n\n"
(BASE/'README.md').write_text(index.rstrip()+'\n')
# Root README overlay retired 2026-09-28: scripts/render-hub.py owns the README block now.
print('Rendered',len(P),'products (archive pages only)')
