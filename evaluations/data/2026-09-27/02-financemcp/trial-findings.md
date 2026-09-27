# FinanceMCP · Data 类第 2 个首轮试用

- 原仓库：https://github.com/guangxiangdebizi/FinanceMCP
- 实际试用源码：`6fbaceb77c197f3cf9798db1fc4bf54e0a874487`，包版本 `4.11.2`；Trading catalog 锁为较早的 `784c6176647aad35d6a25a715b62b333db95df90`。结论绑定本轮实际源码。
- 本机隔离 `npm ci --ignore-scripts` 与 `npm run build` 通过；仅在回环地址运行 Streamable HTTP MCP 服务。所有 Tushare、Qveris、Twingly 等凭证从本轮进程环境移除，项目目录无 `.env`。
- 官方 README 说明公网托管 `/mcp` 暂停；本轮使用本机入口，未测试远程托管。
- [`evidence/probes.json`](evidence/probes.json) 记录 14 次实际 HTTP/MCP 调用和返回；[`evidence/index.html`](evidence/index.html) 与 [`evidence/screenshots/`](screenshots.md) 是 Product Lab 辅助证据页及 14 张不同场景截图，**不是上游原生 Web 界面**。

## 实际有结果

1. `/health`、`initialize` 通过；无凭证 `tools/list` 只公开 4 个 Tool：`current_timestamp`、`finance_news`、`stock_data`、`stock_data_minutes`。
2. Binance 公共接口返回 BTCUSDT、ETHUSDT 的历史日线；ETH 日线响应含 `RSI(14)` 和 `MA(5)` 字段。BTC 一分钟线返回 31 条，ETH 五分钟线返回 25 条。这里只核对了返回结构与数值存在，没有独立复算指标或对账价格。
3. 无凭证新闻查询通过公开百度新闻路由，人工智能与美联储查询分别取得非空结果。返回含标题、来源与链接；**未核实新闻事实真伪**。
4. 14 个探针中 11 个有结果、2 个属于凭证限制、1 个未知 Tool 返回 HTTP 400。性能是单次样本，不能推断稳定性。

## 限制与具体问题

- 无凭证 A 股和美股查询只返回“没有已配置且支持该请求的数据源”。完整多市场覆盖取决于上游凭证；这轮没有验证 Tushare/Qveris/Twingly 的授权路径，也没有把它们标成不可用。港股在本轮同样未实测。
- 上述两次受限的直接 `tools/call` 返回 HTTP 200，正文却写“数据查询失败”，而不是明确的 JSON-RPC 错误；只看 HTTP 状态的客户端可能误判成功。`tools/list` 已正确把不可用的 Tool 能力裁剪到当前 4 个，但直接调用仍需读正文判断。
- `npm audit --omit=dev` 在试用当天报告 4 项 `moderate` 生产依赖告警（body-parser、express、hono、qs）；本轮没有确认可利用性，也未改上游依赖。
- 初次试用脚本错误地用了不合 schema 的 `YYYY-MM-DD` 日期和无参数指标名；原始记录保留在 `probes-initial-invalid-date.json` 与 `probes-second-invalid-indicators.json`。修正为 `YYYYMMDD` 和 `ma(5) rsi(14)` 后成功，最终判断使用修正后的 `probes.json`。

推荐定位：**面向 AI Agent 的多源金融数据 MCP 路由层；无凭证时实际可用的是加密资产历史日/分钟线、公开新闻及本地时间。A 股/美股/港股是依赖授权上游的扩展能力，待凭证与真实返回另行验收。**

结论：作为无需上游凭证的 MCP 数据工具，本地部署容易且公共加密/新闻通路确实出结果；直接调用受限工具的失败表达需要客户端仔细处理。Data 类统一分数和排名在 14 项全部试完后给出。
