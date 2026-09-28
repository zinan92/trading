# Day1 Global Skills · not ranked

**Repository:** `star23/Day1Global-Skills`

**Evidence:** 15 screenshots.

## First-round result

核对 5 个技能包和 BTC 评分 API；API 有 14 项指标，文档描述为 13 项；本轮未产生完整新研报。按你的范围要求不纳入本类评分，定位建议为 Knowledge & Collections。

## Detailed findings

# Day1Global-Skills · Equity Research 类第 3 个首轮试用

- 上游：[`star23/Day1Global-Skills`](https://github.com/star23/Day1Global-Skills)，源码 `562c14b0c0bc84abff755181ead30ebea613d063`。本轮未全局安装到 Codex／Claude 配置，只在隔离 checkout 阅读并核对 5 个 `.skill` ZIP 安装包；每个包内唯一 `SKILL.md` 与仓库同名目录逐字节一致。
- **定位建议：多主题投资研究 Agent Skills 集合／Knowledge & Collections**，而不是一个可部署的个股研究应用。五个 Skill 分别覆盖科技财报、价值投资、美股情绪、宏观流动性和 BTC 周期；前两项属于 Equity Research，其余涉及宏观和加密。没有原生 Web、API 服务器或可直接点击的报告工作台。
- 证据：包结构与文档契约核对摘要 保存包结构、文档契约、显式合成的价值投资评分演练与 BTC 公共接口核对；BTC 公共接口请求结果摘要 是 2026-09-27 实际请求结果；[截图清单](screenshots.md) 有 **15 张不同截图**，全部为清楚标注的 Product Lab 辅助证据页。仓库附带 5 个 PDF 报告示例，但这些是作者样例，**不是本轮运行生成的研究报告**。

实际可用：5 个 Skill 入口和压缩包完整，文本总计 1,349 行。BTC Skill 指定的 `https://brief.day1global.xyz/api/btc-score` 本轮返回 HTTP 200、时间戳、BTC 价格和各指标分数；按返回的每个 `score × weight / 100` 重新计算为 **41.3**，与 API 的 `score=41.3`、`dailyScore=14.7 + weeklyScore=26.6` 一致。价值投资 Skill 的 4 项 0–3 评分可用显式合成数据演算为 10/12、A 档；这只证明规则可按文字执行，不是针对真实股票的结论。

明确缺口：BTC Skill 文档反复称 **13 指标、每日 4／周级 9**，当前实际 API 返回 **14 指标、每日 5／周级 9**，新增 `AHR999`；总权重仍为 32+68=100。文档描述 `totalScore` 字段，实际响应为 `score`。响应只有整体时间戳，14 个指标缺逐项来源与独立 `asOf`，所以复算总分不等于验证了 ETF 流、链上与杠杆数据的真实性和同步性。美股情绪 Skill 把 **0 个过热警告**直接映射成“Panic”，逻辑上不能由“没有过热”推断“恐慌”；这会影响仓位建议。

本轮没有生成新的 16 模块科技财报、4 维真实公司估值、美股情绪或宏观流动性完整报告；这些路径依赖 Agent 联网搜集多源事实并执行判断，不能仅凭 `SKILL.md` 和 PDF 示例宣布功能已验。阶段判断是“包装和一条 BTC 数据路径可用、评分算术正确；跨主题分析质量与时效需继续逐份验证”。Equity Research 类全部测完后统一打分定位。
