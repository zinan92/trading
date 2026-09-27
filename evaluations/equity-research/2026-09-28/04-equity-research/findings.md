# Equity Research · 50

**Repository:** `zinan92/equity-research`

**Evidence:** 29 screenshots.

## First-round result

本地 UI 能浏览 8 个 DEMO 股票；全量真实报告被门禁阻断，未生成任何可执行投资报告。组合页展示 +4.6% 但 DEMO/草稿状态标示不清。

## Score breakdown

| Dimension | Score | Max |
|---|---:|---:|
| 核心结果实测 | 8 | 35 |
| 数据可信度与时效 | 14 | 25 |
| 覆盖与深度 | 8 | 15 |
| 上手与复现 | 12 | 15 |
| 运行稳定性 | 8 | 10 |
| **Total** | **50** | **100** |

## Detailed findings

# zinan92/equity-research · Equity Research 类第 4 个首轮试用

- 上游：[`zinan92/equity-research`](https://github.com/zinan92/equity-research)，源码 `62ecceecd2ddfb616c8677266a9f0852740e429d`。只在新克隆的隔离目录以 `127.0.0.1:8877` 运行 `product/server.py`；没有读取用户真实 runtime、账号、会话或付费数据，默认本地身份门关闭。产品自己说明 fresh clone 只给 DEMO 结构与 8 股演示首页，本轮没有据此声称已取得真实深研。
- 定位：**A 股私域投委会与证据快照深度研报平台**，属于 Equity Research；非券商下单系统。UI 将模型观察、研究门、人工审批、正式发布区分开，方向正确。
- 证据：本轮 11 个原生 HTTP API 场景摘要 保存 11 个原生 HTTP API 只读场景，并记录完整请求 URL、响应 SHA 和本地响应体；[截图清单](screenshots.md) 有 **29 张不同截图**，包括原生四个主视图、8 只股票详情、研报门禁和辅助 API 回执。辅助截图明确标注为 Product Lab 证据页。

实测：`/api/health` HTTP 200 明确返回 `data_mode=DEMO`、`canonical_research.status=unavailable`、`report_count=0`。组合首页有 8 股模型观察权重合计 82%、现金 18%；`/api/committee` 返回 **0/8 公司级深研、0% 可复核建议仓位、0% 可执行仓位**，整期状态 blocked。贵州茅台和宁德时代的 `/api/reports/{ticker}` 只返回 `research_status=unverified`、`research_depth=demo_structure`、缺 REAL 快照／质量门／完整覆盖，原生页面也明确拒绝展示正式目标价和执行仓位；`/api/publication-packs/latest` 为 404，未知股票也是 404。茅台详情的行情与财务标为 Missing，证据项把 FACT、INFERENCE、RISK 分列。失败门没有静默伪造正式研报。

明显呈现矛盾：同一 DEMO 数据的 `/api/dashboard` `publication.status=draft`、快照 degraded，却仍含 6 个 `performance` 点；“组合与业绩”原生页面在没有明显 DEMO 标记时显示 **“发布后收益 +4.6%”“相对基准 +2.5%”**，页面副标题反而写“未发布之前不展示伪历史收益”。这会让首次访问的人误把演示曲线当实绩。茅台 `/api/stocks/600519.SH` 暴露 2026-07-16 的 DEMO `reference_price=1488`，虽然抽屉正确隐藏为 Missing；直接消费原始 API 的客户端也必须尊重 `quality_status=demo` 和快照身份。

README 说明仓库另保存历史 live proof（5 deep + 3 quantitative baseline），但真实数据库、批准正文和发布包**不随 Git 分发**。本轮只验证 fresh clone 的 DEMO 入口与 fail-closed 门禁，不能把历史仓库证据当作今天新部署的深研结果。产业图谱在 DEMO 中明确报“产业快照暂不可用”；没有尝试建立私域会员或触发真实刷新／发布。下一轮最有价值的验证，是在明确授权的真实快照上从输入股票到可审计 30–50 页研报和发布包走完一次，同时修正 DEMO 业绩呈现。Equity Research 类全部测完后统一打分。
