# trump-code · Data 类首轮试用

- 上游：[`sstklen/trump-code`](https://github.com/sstklen/trump-code)，源码 `fa132e9251cf6f43908fd9855379488709731952`。本轮把原生 `chatbot_server.py` 的 handler 仅绑定本机 `127.0.0.1:8111`，未配置 Gemini key、未调用聊天 POST、未运行实时监控或交易。试完停服务。
- **重新定位建议：事件驱动研究 / 政治发言信号与回测**，不是通用 Data feed。它收集特定人物的 Truth Social/X 帖子并输出美股/预测市场信号；虽提供开放数据与 API，核心价值主张是信号命中率、策略和研究结论，应从 Data 移至 Trading Strategy 或单设 Event Signals。
- 证据：[`evidence/probes.json`](evidence/probes.json) 保存 15 个 HTTP 场景与仓库数据交叉核算；[`evidence/screenshots/`](screenshots.md) 保存 **30 张不同截图**，前 14 张为上游原生首页各区块/日报/分析/洞察/游戏，后 16 张是明确标为辅助核对的场景页（其中一张为仓库 JSON 复算）。

可打开的入口：原生首页、日报、分析页、游戏页以及 `/api/dashboard`、`/api/status`、`/api/signals`、`/api/recent-posts`、`/api/polymarket-trump`、`/api/data` 均返回 200。仪表板显示信号、三套 playbook、预测市场、历史回测摘要，内容丰富。仓库 `predictions_log.json` 有 566 条记录，其中 **564 已验证、2 待验证**；564 中 346 条 `correct=true`，346/564 = **61.3%**，故界面宣称的 61.3% 在现有文件内算术可重现。这不能单独证明模型设计、样本独立性或未来可交易收益。`surviving_rules.json` 实际有 600 条，README 仍写 551 surviving rules、566 verified predictions，说明介绍落后于数据。

关键断裂：`daily_report.json` 日期为 **2026-09-26**，声称当天 18 条帖子、最新 15:58；但 `trump_posts_all.json` 的 `date_range.latest` 和 `/api/recent-posts` 返回的最新帖子均停在 **2026-03-25**。即日报和页面“Recent Posts · LIVE”并非来自同一已更新的归档，用户无法由该页面核对当日源帖。`/api/models` 返回空 `{}` 与 `date="?"`，而仪表板仍展示历史模型和 61.3% 命中率。`health_status.json` 最后更新 **2026-04-04**、状态 degraded；`/api/status` 虽返回 2026-09-26 的摘要，也自报 `needs_attention`。

日报页面本轮显示“此日期尚无分析文章”，归档日期首项 2026-04-04。点击该日期后仍是空状态：前端请求 `/articles/2026-04/04-zh.md` 得到 404，而仓库实际文件名是 `04-flash-2306-zh.md` 等。可见文章文件存在，但页面索引和文件名约定不匹配。`/api/insights` 返回 0，社区反馈价值本轮没有用户数据可验证。预测市场列表来自仓库缓存，不能把页面上的 `LIVE` 字样等同于我们验证了实时更新。

服务日志还明确报 `data/evolution_log.json` 与 `data/opus_briefing.json` 解析失败；独立用 `json.load` 复核为 `JSONDecodeError`。这两个坏文件未阻断首页 200，却会使相关演化/简报区块缺失或退化。

阶段判断：视觉呈现与研究叙事比较完整，历史 61.3% 可按已存预测记录复算；但最核心的“最新发言 → 当日信号 → 模型榜单 → 文章”链条出现跨月份不一致与空页面，现阶段不能视为可靠实时信号产品。最终分数和 Data 类排序待全部 14 项测完；届时会单独标记它的分类偏差。
