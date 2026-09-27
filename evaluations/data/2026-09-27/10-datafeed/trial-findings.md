# datafeed · Data 类首轮试用

- 上游：[`zinan92/datafeed`](https://github.com/zinan92/datafeed)，源码 `4a2f0cff3878f31caf176e355bd6b58c0458b5d7`，包版本 0.3.0。隔离目录、隔离 SQLite、仅监听 `127.0.0.1:8110`；试完关闭。没有使用现有 `com.wendy.datafeed` 的生产/常驻服务或数据库。
- 定位：**多市场 OHLCV API/数据管线**，按 ticker + timeframe 拉取蜡烛图并标注 provider、source、质量、缓存与来源。A 股、美国股票、加密现货、商品期货、美国国债收益率等有不同适配器；它不提供完整交易终端，也不下单。
- 证据：[`evidence/probes.json`](evidence/probes.json) 有 19 条原生 HTTP 试用摘要，逐条完整响应见 `evidence/NN-response.json`；[`evidence/screenshots/`](screenshots.md) 有 **22 张不同截图**，其中 3 张为上游原生健康看板/Swagger 文档，其余 19 张为明确标注的辅助证据索引。浏览器直开 BTC JSON 时被客户端阻止，BTC 请求成功依据原生 HTTP 响应文件而非该浏览器页。

成功路径：上证指数日线 5 根、周线 3 根，茅台日线 5 根、AAPL 日线与 1 小时各 5 根、BTC 现货 1 小时/1 分钟/原生 4 小时各 5 根、美国国债 10Y 日线 5 根、黄金连续期货日线 5 根，均返回 HTTP 200 且 `count=5`（周线 `count=3`）。BTC 的 1 分钟 strict 请求返回 `fresh=true`；周日无法验证 A 股/美股的交易时段实时性。期货合约 `XAUUSDT` 原生 instrument definition 返回 200。A 股茅台收盘 1237.0，与独立 `a-stock-data`/`adata` 腾讯路径得到的值相同；美国 10Y 2026-09-25 为 5.17%，与官方财政部 CSV 试用一致。

契约与限制：`2m` 周期返回 422；要求执行场所却选择 Binance Spot 返回 400 `execution_venue_required`；`cache_policy=require` 且隔离库无该标的时返回 404 `cache_miss`。默认向指数请求 instrument metadata 时 auto 选 Yahoo 并返回 502 `instrument_definition_unavailable`，显式 Binance USD-M 合约则成功。`/api/sessions/us_stock/AAPL` 缺 `source` 返回 422，补 `yahoo_finance_free` 仍返回 400 `market_sessions_unavailable`，说明该免费源不提供交易时段定义。`/api/tickers?query=AAPL` 返回 0：本轮 Phase 1 来源读取并未自动形成可搜索的持久缓存。

原生 `/health-ui` 在本隔离库报告 1,080 个矩阵单元，当前有 57 个因授权阻塞且 0 个有数据；这是持久化采集/授权状态，**不能用直拉 API 的成功来宣称健康矩阵已可用**。合并矩阵页因未配置 Watchlist 数据库返回 HTTP 503。来源 `yahoo_finance_free` 与 `tencent_stock_free` 响应自带 `entitlement_unverified`，应按研究用途/许可未核实来解释，不能仅凭数据返回 200 宣称商业/交易可用。最终分数与类内排名待 14 个 Data 产品全部试用后再给。
