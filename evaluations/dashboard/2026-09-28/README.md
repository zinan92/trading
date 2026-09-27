# Trading · Dashboard 首轮试用、排序与定位

截至 **2026-09-28**，本目录原有 7 个 Dashboard catalog 项都已逐个评测。另把刚从 Equity Research 识别出的 A Share Heatmap 带入同类比较（此前实测，不重复运行）。本轮保存 140 张不同产品画面；各产品截图数量均超过 10 张。完整评分方法见 [methodology.md](methodology.md)。

## Dashboard 适配度排名

| 名次 | 产品 | 分数 | 建议定位 | 实测摘要 | 证据 |
|---:|---|---:|---|---|---|
| 1 | [A Share Heatmap](https://github.com/wenyuanw/a-share-heatmap) | **84** | A 股市场广度与板块 Dashboard | 九类市场范围、日/周/月/年视图、筛选、自选、主题和分享预览已实测；行情快照止于 2026-09-24。此证据从 Equity Research 复用。 | [判断](08-a-share-heatmap/findings.md) · [24 张截图](08-a-share-heatmap/screenshots.md) |
| 2 | [Gloomberb](https://github.com/gloom-sh/gloomberb) | **82** | 多市场研究终端（TUI/桌面） | 无 key 的延时 AAPL quote 可用；内置 pane screenshot 15 张中 14 张可用，包含图表、估值、宏观与 SEC 页面。Portfolio Analytics 没显示单独添加的测试组合。 | [判断](05-gloomberb/findings.md) · [15 张截图](05-gloomberb/screenshots.md) |
| 3 | [OpenStock](https://github.com/Open-Dev-Society/OpenStock) | **78** | 开源股票研究与市场总览网页 | 首页、数据说明和注册校验可用；dashboard 与 SPY 详情匿名访问被重定向到登录，watchlist/alerts 未验。 | [判断](01-openstock/findings.md) · [17 张截图](01-openstock/screenshots.md) |
| 4 | [Human K-line Review](https://github.com/zinan92/human-kline-review) | **76** | 人工宏观 K 线复盘工作台 | 隔离 synthetic fixture 可完成标注、周期复盘、显式跳过缺周期、确认和 mock 汇总；未接 Macro Source/DeepSeek。已复现 autosave 与 complete 竞态。 | [判断](03-human-kline-review/findings.md) · [21 张截图](03-human-kline-review/screenshots.md) |

## 代表界面

| A Share Heatmap · 84 | Gloomberb · 82 |
|---|---|
| ![A Share Heatmap 市场总览](08-a-share-heatmap/images/01-01-native-all-day.jpg) | ![Gloomberb Quote Monitor](05-gloomberb/images/01-quote-monitor.png) |
| A 股全市场日视图；截图数据源时间为 2026-09-24。 | TUI pane 的 AAPL delayed quote；EVAL 水印表示无账户隔离评测。 |

| OpenStock · 78 | Human K-line Review · 76 |
|---|---|
| ![OpenStock 官方公开页](01-openstock/images/01-landing-hero.jpg) | ![Human K-line Review synthetic chart](03-human-kline-review/images/01-initial-overview.jpg) |
| 官方公开部署；登录后的 dashboard 未验。 | 明确标为 synthetic 的复盘图；不是真实市场数据。 |

### 榜单说明

分数为各产品角色内的首轮证据分，不是市场收益。A Share Heatmap 的源数据比评测日早四天；Gloomberb 的主数据路径是 Gloomberb Cloud delayed quote；OpenStock 的公开页面无法代表账户内 dashboard；Human K-line Review 在本轮只用本地 synthetic source。因此本榜说明了界面与工作流价值，不能视作行情准确率或生产认证。

## 目录项重分类建议

这四项已经逐个测试和留存截图，但不应作为 Dashboard 产品参与上面的同角色榜单。

| 原 Dashboard catalog 项 | 角色分 | 建议归属 | 实测/证据 |
|---|---:|---|---|
| [standard-kline](https://github.com/zinan92/trading-system/tree/main/packages/standard-kline) | **79** | Trading Infra / provider-neutral chart component | 21 个单测通过；浏览器 fixture 覆盖 candles、EMA/MACD、markers、空/加载状态、缩放。它是组件，不是独立看板。 [判断](06-standard-kline/findings.md) · [14 张有效截图](06-standard-kline/screenshots.md) |
| [TradingView-API](https://github.com/Mathieu2301/TradingView-API) | **78** | Trading Data / TradingView WebSocket client | 无 session cookie 的公开图表连接可用；50 测试通过、16 跳过；private indicators 未验。 [判断](07-tradingview-api/findings.md) · [13 张截图](07-tradingview-api/screenshots.md) |
| [tvscreener](https://github.com/deepentropy/tvscreener) | **73** | Trading Data / unofficial screener client | 一次公开股票 query 成功；六类 screener 的代码生成可用，Valuation preset 生成缺失的 StockField 名。 [判断](04-tvscreener/findings.md) · [17 张截图](04-tvscreener/screenshots.md) |
| [trading-desk](https://github.com/zinan92/trading-desk) | **70** | Full Trading System / integrated Desk UI module | 已归档迁入 trading-system；本地只读界面和空 read model 已在 Trading Infra 评测中测试。没有独立部署价值。 [判断](02-trading-desk/findings.md) · [19 张截图](02-trading-desk/screenshots.md) |

不要把 CLI、TUI、API library、chart widget 统统当作“完整 Dashboard”。其中 Gloomberb 虽由 CLI 启动，实际提供可视研究终端，适合本类；tvscreener/TradingView-API 是数据客户端，standard-kline 是图表组件；trading-desk 已并入完整交易平台。

## 首轮成熟度观察

目前在 Dashboard 角色中证据最完整的是 A Share Heatmap 与 Gloomberb：前者有清楚的 A 股范围、周期、筛选与自选操作，后者有广泛 pane 目录和真实公开数据/内置截图流程。OpenStock 外观完成度高，但认证后的主产品区本轮不可验。Human K-line Review 的人工工作流结构完整，但自动保存计时器在“完成周期”后可能再落一条空草稿，导致进度回退；这一问题要先修。

所有真实数据只通过公开只读查询；没有输入真实 API key、登录私人账户、连接券商或下真实订单。Human K-line 的 4H missing、standard-kline、DeepSeek 都用隔离 fixture/mock 明确标注。
