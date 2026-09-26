<div align="center">

# Trading

**Trading 的 capability-first catalog：先按功能分类，再按加入时间从新到旧浏览。**

[![Snapshot](https://img.shields.io/badge/snapshot-66%20repos-0969DA.svg)](snapshot.yaml)
[![Source](https://img.shields.io/badge/source-Park%20OS-8250DF.svg)](https://github.com/zinan92/park-operating-system)

</div>

---

```text
in  canonical Park OS snapshot + source provenance + fixed commit locks
out 66-repo Trading catalog, grouped by function and ordered newest-added first

fail snapshot checksum mismatch → stop before publishing
fail missing created_at / starred_at → stop; do not guess ordering
fail unclassified placement → keep needs_review; do not guess
```

Snapshot: `github-universe-2026-09-26-finance-skills-knowledge-01` · canonical source: [Park OS](https://github.com/zinan92/park-operating-system)

## How to read this page

- **Category first** — repos stay in the established functional taxonomy.
- **Newest first** — inside each category, later additions appear first.
- **Added** — Park-owned repos use GitHub `created_at`; external repos use Park's `starred_at`.
- **Lock** — external sources are pinned to commit SHAs, not live branches.

## Browse by function

### Data (14)

| Repo | Capability / description | Source | Added | Lock / flags |
|---|---|---|---|---|
| [tickflow-org/tickflow](https://github.com/tickflow-org/tickflow) | Professional financial data API for China A-shares, US & HK stocks. Python SDK with real-time quotes, K-line data & financial reports. | Starred | `2026-09-18` | `c27f23c50386` |
| [guangxiangdebizi/FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP) | 这是一个金融领域相关的mcp,本项目通过集成 Tushare API 和 Binance API 为语言模型（如Claude）提供全面的实时金融数据访问能力，支持股票、基金、债券、宏观经济指标、稳定币、虚拟货币等多维度金融数据分析。其中也包含了金融数据查询、财经新闻查询、国家统计局数据查询等 | Starred | `2026-09-13` | `784c6176647a` |
| [atilaahmettaner/tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp) | TradingView MCP server — real-time market data, technical analysis, screeners & backtesting for Claude, ChatGPT, Cursor & any MCP client. Stocks, crypto, forex & futures across global exchanges. Hosted or self-host. | Starred | `2026-09-12` | `a1e54b07e5c2` |
| [zinan92/watchlist](https://github.com/zinan92/watchlist) | Park Exposure Registry — 行情与新闻共用的唯一权威名单：6 条宏观主线 / 24 个中观赛道 / 109 个 target | Owned | `2026-09-03` | `owned source` |
| [HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API) | 同花顺官方 A股金融数据服务，提供股票实时行情、历史行情、财务报表、指数、板块、涨停等数据，适用于 AI Agent、量化研究和应用开发，支持 API、MCP、CLI 和 Python。Official Tonghuashun (HiThink) A-share financial data service providing real-time and historical stock market data, financial statements, indices, sectors and limit-up data for AI agents, quantitative research and application development. | Starred | `2026-08-26` | `402574a6221d` · NEEDS_REVIEW |
| [1nchaos/adata](https://github.com/1nchaos/adata) | 免费开源A股量化交易数据库； 专注A股，专注量化，向阳而生； 开放、纯净、持续、为Ai(爱)发电。为个人量化交易而生，保卫3000点，珍惜底部机会......【股票数据，股票行情数据，股票量化数据，股票交易数据，k线行情数据，股票概念数据，股票数据接口，行情数据接口，量化交易数据】【多数据源融合，动态设置代理，保障数据高可用性】 | Starred | `2026-07-15` | `b14f4e57b217` |
| [JerBouma/FinanceDatabase](https://github.com/JerBouma/FinanceDatabase) | This is a database of 300.000+ symbols containing Equities, ETFs, Funds, Indices, Currencies, Cryptocurrencies and Money Markets. | Starred | `2026-07-15` | `a174c97d3bba` |
| [simonlin1212/global-stock-data](https://github.com/simonlin1212/global-stock-data) | US stock market data for AI coding assistants — zero-auth, official sources. CBOE options with full Greeks + 0DTE flow, FINRA market-wide short volume, SEC EDGAR filing stream, and a free market-wide screener. 13 layers, 30+ endpoints, 11 sources. Every source labeled with its compliance tier. | Starred | `2026-07-09` | `fbf0ae47d64e` |
| [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | A股全栈数据工具包 · 十二层架构 · 60端点 · 22数据源 · 零鉴权 \| Full-stack China A-share data toolkit for AI agents — 12 layers, 60 endpoints, 22 sources, zero-auth | Starred | `2026-07-09` | `2012ce7cd0e7` |
| [zinan92/datafeed](https://github.com/zinan92/datafeed) | 行情数据。in ticker+timeframe → out OHLCV candles。A股/美股/加密/商品 | Owned | `2026-03-29` | `owned source` |
| [sstklen/trump-code](https://github.com/sstklen/trump-code) | 🔐 AI decoding Trump's posts × stock market \| AI 解碼川普推文 × 美股 \| AIでトランプ投稿×株式市場を解読 — 31.5M models, 61.3% hit rate, open source | Starred | `2026-03-16` | `296b8e14ee88` |
| [zinan92/intel](https://github.com/zinan92/intel) | 情报采集。in 10+信息源 → out LLM评分+跨源事件聚类 | Owned + Starred | `2026-02-13` | `owned source` |
| [zinan92/quant-data-pipeline](https://github.com/zinan92/quant-data-pipeline) | 多市场量化数据平台 — A股/美股/加密/商品，28组API，感知信号引擎，模拟交易 | Owned + Starred | `2026-02-13` | `owned source` |
| [akfamily/akshare](https://github.com/akfamily/akshare) | AKShare is an elegant and simple financial data interface library for Python, built for human beings! 开源财经数据接口库 | Starred | `2025-09-08` | `8e95744b79ae` |

### Equity Research (9)

| Repo | Capability / description | Source | Added | Lock / flags |
|---|---|---|---|---|
| [wshobson/maverick-mcp](https://github.com/wshobson/maverick-mcp) | MaverickMCP - Personal Stock Analysis MCP Server | Starred | `2026-09-13` | `fb55c84c9a9c` |
| [wenyuanw/a-share-heatmap](https://github.com/wenyuanw/a-share-heatmap) | 免费开源的 A股热力图｜A股大盘云图，各板块涨跌一眼可见 | Starred | `2026-08-26` | `c15f94e616cf` · NEEDS_REVIEW |
| [star23/Day1Global-Skills](https://github.com/star23/Day1Global-Skills) | Day1Global Skills Share: US Stock, Macro Market, Crypto | Starred | `2026-07-21` | `562c14b0c0bc` |
| [zinan92/equity-research](https://github.com/zinan92/equity-research) | A股长期投委会 + 证据快照深度研报平台(Park 产品层) | Owned | `2026-07-20` | `owned source` |
| [rollingSirius/equity-research-skill](https://github.com/rollingSirius/equity-research-skill) | Possibly the deepest AI equity-research skill: nine-chapter single-stock deep dives and earnings deep-dives, with scripted DCF/EPV/EVA and reproducible valuation. Covers US, HK and A-shares. Docs in EN and ZH. | Starred | `2026-07-18` | `3d94e64ff53b` |
| [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | 冰冷的钱就这样流进我温暖的口袋-游资（UZI）Skills — 让我们欢迎，股海贼王！66位投资大佬帮你看盘 · 22维数据 × 180条量化规则 × 17种机构分析方法 · A股/港股/美股 | Starred | `2026-07-09` | `650788c54a9b` |
| [muxuuu/serenity-skill](https://github.com/muxuuu/serenity-skill) | Serenity-inspired Agent Skill for supply-chain bottleneck stock research | Starred | `2026-07-09` | `c2fe93deedfd` |
| [virattt/dexter](https://github.com/virattt/dexter) | An autonomous agent for deep financial research | Starred | `2026-05-09` | `ecaed3011f24` |
| [microsoft/qlib](https://github.com/microsoft/qlib) | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped with https://github.com/microsoft/RD-Agent to automate R&D process. | Starred | `2025-08-11` | `79633dd9506e` |

### Trading Strategy (9)

| Repo | Capability / description | Source | Added | Lock / flags |
|---|---|---|---|---|
| [fmzquant/strategies](https://github.com/fmzquant/strategies) | quantitative trading with Javascript, Python, C++, PineScript, Blockly, MyLanguage(麦语言) | Starred | `2026-09-24` | `7853bb2bf262` |
| [YoungCan-Wang/WyckoffTradingAgent](https://github.com/YoungCan-Wang/WyckoffTradingAgent) | Open-source Wyckoff trading agent and AI stock screener for volume-price analysis, A-share screening, CLI workflows, and MCP tools.灵感来自秋生trader @Hoyooyoo | Starred | `2026-09-18` | `6bdaf1eb3cff` |
| [nhovongoc0-max/meme-radar](https://github.com/nhovongoc0-max/meme-radar) | Meme雷达开源版：本地只读、多链 Meme 候选扫描与人工复核工具 | Starred | `2026-09-13` | `9c41a444b9bc` |
| [Vespa314/chan.py](https://github.com/Vespa314/chan.py) | 开放式的缠论python实现框架，支持形态学/动力学买卖点分析计算，多级别K线联立，区间套策略，可视化绘图，多种数据接入，策略开发，交易系统对接； | Starred | `2026-09-12` | `429d6ed3043e` |
| [neil-pan-s/one-quant-doc](https://github.com/neil-pan-s/one-quant-doc) | 缠中说禅-缠论技术分析 实时自动笔段画线、中枢标识 递归分析整体走势 作为买卖分析参考 | Starred | `2026-09-12` | `7231f5d5353c` |
| [zinan92/trading-strategy](https://github.com/zinan92/trading-strategy) | Engine-neutral Canonical DCA/Grid strategy engine。in plain Python strategy inputs + OHLCV bars → out deterministic plans, previews, replays, and lifecycle receipts | Owned | `2026-08-24` | `owned source` |
| [zinan92/chancode](https://github.com/zinan92/chancode) | No description | Owned | `2026-05-26` | `owned source` · PRIVATE |
| [waditu/czsc](https://github.com/waditu/czsc) | 缠中说禅技术分析工具；缠论；股票；期货；Quant；量化交易 | Starred | `2025-08-11` | `701e480a5450` |
| [TA-Lib/ta-lib-python](https://github.com/TA-Lib/ta-lib-python) | Python wrapper for TA-Lib (http://ta-lib.org/). | Starred | `2024-04-21` | `fd6089b183fc` |

### Trading Infra (6)

| Repo | Capability / description | Source | Added | Lock / flags |
|---|---|---|---|---|
| [zinan92/standard-broker](https://github.com/zinan92/standard-broker) | Provider-neutral broker Ports & Adapters for Paper-safe trading systems | Owned | `2026-08-21` | `owned source` · PRIVATE |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | Production-grade Rust-native trading engine with deterministic event-driven architecture | Starred | `2026-07-09` | `23cb3035dff7` |
| [zinan92/trading-system](https://github.com/zinan92/trading-system) | Gold trading system orchestrator | Owned | `2026-07-03` | `owned source` · PRIVATE |
| [polakowo/vectorbt](https://github.com/polakowo/vectorbt) | The backtesting engine that gives you an unfair advantage. Run thousands of trading ideas before others finish one. | Starred | `2024-04-21` | `34b6d5935e3e` |
| [ccxt/ccxt](https://github.com/ccxt/ccxt) | A unified trading API with more than 100 crypto exchanges and prediction markets in JavaScript / TypeScript / Python / C# / PHP / Go / Java / Rust | Starred | `2024-04-13` | `c781a2437d88` |
| [Drakkar-Software/OctoBot](https://github.com/Drakkar-Software/OctoBot) | Free open source crypto trading bot to automate AI, Grid, DCA and TradingView strategies on Binance, Hyperliquid and 15+ exchanges, with a simple interface. | Starred | `2024-04-13` | `dc0efc8ec36c` |

### Dashboard (7)

| Repo | Capability / description | Source | Added | Lock / flags |
|---|---|---|---|---|
| [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | OpenStock is an open-source alternative to expensive market platforms. Track real-time prices, set personalized alerts, and explore detailed company insights — built openly, for everyone, forever free. | Starred | `2026-09-24` | `87df76a2ce58` |
| [zinan92/trading-desk](https://github.com/zinan92/trading-desk) | No description | Owned | `2026-09-14` | `owned source` · PRIVATE |
| [zinan92/human-kline-review](https://github.com/zinan92/human-kline-review) | Park 人工宏观 K 线复盘与 DeepSeek 汇总：HTML-first，Telegram later | Owned | `2026-08-23` | `owned source` · PRIVATE |
| [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | TradingView Screener API - Stock, Crypto, Forex, Bond, Futures, Coin | Starred | `2026-08-10` | `737c9764c1e5` |
| [gloom-sh/gloomberb](https://github.com/gloom-sh/gloomberb) | Finance terminal, in your terminal. | Starred | `2026-07-21` | `4dc1d5cd2714` |
| [zinan92/standard-kline](https://github.com/zinan92/standard-kline) | 标准 K 线前端组件。in OHLCV bars + provider metadata → out candlestick chart + volume + overlays + synthetic watermark | Owned | `2026-07-07` | `owned source` |
| [Mathieu2301/TradingView-API](https://github.com/Mathieu2301/TradingView-API) | 📈 Get real-time stocks from TradingView | Starred | `2026-07-02` | `5baea86c8c7e` |

### Full Trading System / Agent (13)

| Repo | Capability / description | Source | Added | Lock / flags |
|---|---|---|---|---|
| [ArvinLovegood/go-stock](https://github.com/ArvinLovegood/go-stock) | 🦄🦄🦄AI赋能股票分析：AI加持的股票分析/选股工具。股票行情获取，AI热点资讯分析，AI资金/财务分析，涨跌报警推送。支持A股，港股，美股。支持市场整体/个股情绪分析，AI辅助选股等。数据全部保留在本地。支持DeepSeek，OpenAI， Ollama，LMStudio，AnythingLLM，硅基流动，火山方舟，阿里云百炼等平台或模型。 | Starred | `2026-09-24` | `c26304fafab0` |
| [FinHackCN/finhack](https://github.com/FinHackCN/finhack) | FinHack®，一个易于拓展的量化金融框架，它在当前版本中集成了数据采集、因子计算、因子挖掘、因子分析、机器学习、策略编写、量化回测、实盘接入等全流程的量化投研工作。 | Starred | `2026-09-18` | `dedbbd0b7acc` |
| [nishuzumi/fomomo](https://github.com/nishuzumi/fomomo) | No description | Starred | `2026-09-13` | `a2c6040392e3` · NEEDS_REVIEW |
| [ling-0729/KHunter](https://github.com/ling-0729/KHunter) | KHunter 是一套开箱即用的A股量化交易系统，集数据管理、策略选股、择时交易、风险控制、回测验证于一体，为个人投资者提供从数据到交易的全流程量化解决方案。 | Starred | `2026-09-10` | `ca93f9e05523` |
| [Theclues/TradeGenuis-Options](https://github.com/Theclues/TradeGenuis-Options) | No description | Starred | `2026-09-07` | `a77d13dae84b` |
| [sngyai/Sequoia-X](https://github.com/sngyai/Sequoia-X) | A股自动选股系统 — 多种技术形态自动扫描，收盘后自动运行并推送飞书 | Starred | `2026-08-26` | `444c0db69ff3` · NEEDS_REVIEW |
| [shy3130/tick-stock-panel](https://github.com/shy3130/tick-stock-panel) | TSP自托管、零运维的 A 股「选股 + 监控 + 回测」量化工作台 \| LLM能力驱使策略定制+个股分析+复盘 \| 自由接入第三方数据源与个性化扩展数据 \| 个人开源 | Starred | `2026-08-26` | `bfbccf9c414f` · NEEDS_REVIEW |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Kronos: A Foundation Model for the Language of Financial Markets | Starred | `2026-08-03` | `67b630e67f6a` |
| [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research) | Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录、回测。Vibe-Research 把数据和功能配齐，由你自己的 Agent 驱动投资研究。基于开源的 Codex Harness 打造。 | Starred | `2026-08-03` | `34ed58155ca2` |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | "Vibe-Trading: Your Personal Trading Agent" | Starred | `2026-07-21` | `e476b4ce4c3b` |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | Starred | `2026-06-08` | `1168e316269b` |
| [OpenByteInc/QuantDinger](https://github.com/OpenByteInc/QuantDinger) | Open-source AI Trading OS and commercial-ready multi-tenant SaaS platform — research markets, build Python strategies, backtest, paper/live trade, and monitor crypto, stocks, and forex, with built-in user management, billing, payments, and settlement to launch and operate your own trading service. | Starred | `2026-05-01` | `d8508a85a473` |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | TradingAgents: Multi-Agents LLM Financial Trading Framework | Starred | `2026-02-02` | `be952b8eccb4` |

### Knowledge & Collections (8)

| Repo | Capability / description | Source | Added | Lock / flags |
|---|---|---|---|---|
| [stockServ/chzhshch-108-plus](https://github.com/stockServ/chzhshch-108-plus) | 缠中说禅教你炒股票108课加强版 | Starred | `2026-09-10` | `d2a87d5bd9c8` |
| [lzwme/finance-quant-skills](https://github.com/lzwme/finance-quant-skills) | 一个面向金融量化交易领域的 Agent Skills 技能维护仓库，主要聚焦A股量化交易。 | Starred | `2026-08-26` | `7af066194d8d` |
| [wangzhe3224/awesome-systematic-trading](https://github.com/wangzhe3224/awesome-systematic-trading) | A curated list of insanely awesome libraries, packages and resources for systematic trading. Crypto, Stock, Futures, Options, CFDs, FX, and more \| 量化交易 \| 量化投资 | Starred | `2026-08-10` | `424df5f4acc9` |
| [bwjoke/BTC-Trading-Since-2020](https://github.com/bwjoke/BTC-Trading-Since-2020) | Public BTC trading context since 2020. | Starred | `2026-07-05` | `9ff0d562cffd` |
| [RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) | A collection of Awesome Finance Agent Skills for free and easy to start \| 一系列开源免费的金融分析Agent Skills | Starred | `2026-04-27` | `853f09b4d0ba` |
| [zinan92/copilot](https://github.com/zinan92/copilot) | 方法论路由。in 信号+上下文 → out 44套方法论匹配分析 | Owned + Starred | `2026-03-18` | `owned source` · PRIVATE |
| [LLMQuant/quant-wiki](https://github.com/LLMQuant/quant-wiki) | We are committed to the open-sourcing quantitative knowledge, aiming to bridge the information gap between the domestic and international quantitative finance industries. 我们致力于量化知识的开源与汉化，打破国内外量化金融行业信息差。 | Starred | `2025-08-11` | `f08b94e13425` |
| [wilsonfreitas/awesome-quant](https://github.com/wilsonfreitas/awesome-quant) | A curated list of insanely awesome libraries, packages and resources for Quants (Quantitative Finance) | Starred | `2024-04-12` | `48e48a76b205` |

## Update contract

This README and the generated data are scoped views. Taxonomy, source state, added-time authority and locks remain in Park OS.

```bash
bash scripts/verify-scoped.sh
```

The catalog is not a production-readiness or execution-authorization claim.
