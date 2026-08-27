<div align="center">

# Trading

**Trading 的 capability-first registry：按子分类浏览 owned 与 starred repo。**

[![Snapshot](https://img.shields.io/badge/snapshot-49%20repos-0969DA.svg)](snapshot.yaml)
[![Source](https://img.shields.io/badge/source-Park%20OS-8250DF.svg)](https://github.com/zinan92/park-operating-system)

</div>

---

```text
in  canonical Park OS snapshot + source provenance + fixed commit locks
out 49-repo Trading map, grouped by function and owned/starred source

fail snapshot checksum mismatch → stop before publishing
fail private source inaccessible → preserve name/link and mark PRIVATE
fail unclassified placement → keep needs_review; do not guess
```

Snapshot: `github-universe-2026-08-27-trading-review-01` · canonical source: [Park OS](https://github.com/zinan92/park-operating-system)

## How to read this page

- **Owned** — repo owned by Park.
- **Starred** — external repo selected as a locked reference.
- **Lock** — external source is pinned to a commit SHA, not a live branch.
- **PRIVATE / ARCHIVED** — GitHub visibility or lifecycle flags are preserved.

## Browse by function

### Data (10)

| Repo | Capability / description | Source | Lock / flags |
|---|---|---|---|
| [1nchaos/adata](https://github.com/1nchaos/adata) | 免费开源A股量化交易数据库； 专注A股，专注量化，向阳而生； 开放、纯净、持续、为Ai(爱)发电。为个人量化交易而生，保卫3000点，珍惜底部机会......【股票数据，股票行情数据，股票量化数据，股票交易数据，k线行情数据，股票概念数据，股票数据接口，行情数据接口，量化交易数据】【多数据源融合，动态设置代理，保障数据高可用性】 | Starred | `b14f4e57b217` |
| [akfamily/akshare](https://github.com/akfamily/akshare) | AKShare is an elegant and simple financial data interface library for Python, built for human beings! 开源财经数据接口库 | Starred | `0e7db00cb98a` |
| [HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API) | 同花顺官方 A股金融数据服务，提供股票实时行情、历史行情、财务报表、指数、板块、涨停等数据，适用于 AI Agent、量化研究和应用开发，支持 API、MCP、CLI 和 Python。Official Tonghuashun (HiThink) A-share financial data service providing real-time and historical stock market data, financial statements, indices, sectors and limit-up data for AI agents, quantitative research and application development. | Starred | `9dbef74d2ce5` |
| [JerBouma/FinanceDatabase](https://github.com/JerBouma/FinanceDatabase) | This is a database of 300.000+ symbols containing Equities, ETFs, Funds, Indices, Currencies, Cryptocurrencies and Money Markets. | Starred | `e3c554bb5110` |
| [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | A股全栈数据工具包 · 十一层架构 · 54端点 · 19数据源 · 零鉴权 \| Full-stack China A-share data toolkit for AI agents — 11 layers, 54 endpoints, 19 sources, zero-auth | Starred | `f90d67853b81` |
| [simonlin1212/global-stock-data](https://github.com/simonlin1212/global-stock-data) | US stock market data for AI coding assistants — zero-auth, official sources. CBOE options with full Greeks + 0DTE flow, FINRA market-wide short volume, SEC EDGAR filing stream, and a free market-wide screener. 13 layers, 30+ endpoints, 11 sources. Every source labeled with its compliance tier. | Starred | `c0b3ed8d8a1f` |
| [sstklen/trump-code](https://github.com/sstklen/trump-code) | 🔐 AI decoding Trump's posts × stock market \| AI 解碼川普推文 × 美股 \| AIでトランプ投稿×株式市場を解読 — 31.5M models, 61.3% hit rate, open source | Starred | `ec5e2de1f7a0` |
| [zinan92/datafeed](https://github.com/zinan92/datafeed) | 行情数据。in ticker+timeframe → out OHLCV candles。A股/美股/加密/商品 | Owned | owned source |
| [zinan92/intel](https://github.com/zinan92/intel) | 情报采集。in 10+信息源 → out LLM评分+跨源事件聚类 | Owned + Starred | owned source |
| [zinan92/quant-data-pipeline](https://github.com/zinan92/quant-data-pipeline) | 多市场量化数据平台 — A股/美股/加密/商品，28组API，感知信号引擎，模拟交易 | Owned + Starred | owned source |

### Equity Research (8)

| Repo | Capability / description | Source | Lock / flags |
|---|---|---|---|
| [microsoft/qlib](https://github.com/microsoft/qlib) | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped with https://github.com/microsoft/RD-Agent to automate R&D process. | Starred | `79633dd9506e` |
| [muxuuu/serenity-skill](https://github.com/muxuuu/serenity-skill) | Serenity-inspired Agent Skill for supply-chain bottleneck stock research | Starred | `c2fe93deedfd` |
| [rollingSirius/equity-research-skill](https://github.com/rollingSirius/equity-research-skill) | Possibly the deepest AI equity-research skill: nine-chapter single-stock deep dives and earnings deep-dives, with scripted DCF/EPV/EVA and reproducible valuation. Covers US, HK and A-shares. Docs in EN and ZH. | Starred | `3d94e64ff53b` |
| [star23/Day1Global-Skills](https://github.com/star23/Day1Global-Skills) | Day1Global Skills Share: US Stock, Macro Market, Crypto | Starred | `562c14b0c0bc` |
| [virattt/dexter](https://github.com/virattt/dexter) | An autonomous agent for deep financial research | Starred | `ecaed3011f24` |
| [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | 冰冷的钱就这样流进我温暖的口袋-游资（UZI）Skills — 让我们欢迎，股海贼王！66位投资大佬帮你看盘 · 22维数据 × 180条量化规则 × 17种机构分析方法 · A股/港股/美股 | Starred | `b004d7a988ca` |
| [wenyuanw/a-share-heatmap](https://github.com/wenyuanw/a-share-heatmap) | 免费开源的 A股热力图｜A股大盘云图，各板块涨跌一眼可见 | Starred | `3cfecabff864` |
| [zinan92/equity-research](https://github.com/zinan92/equity-research) | A股长期投委会 + 证据快照深度研报平台(Park 产品层) | Owned | owned source |

### Trading Strategy (4)

| Repo | Capability / description | Source | Lock / flags |
|---|---|---|---|
| [TA-Lib/ta-lib-python](https://github.com/TA-Lib/ta-lib-python) | Python wrapper for TA-Lib (http://ta-lib.org/). | Starred | `a9ff1b47b3dd` |
| [waditu/czsc](https://github.com/waditu/czsc) | 缠中说禅技术分析工具；缠论；股票；期货；Quant；量化交易 | Starred | `701e480a5450` |
| [zinan92/chancode](https://github.com/zinan92/chancode) | No description | Owned | owned source · PRIVATE |
| [zinan92/trading-strategy](https://github.com/zinan92/trading-strategy) | Engine-neutral Canonical DCA/Grid strategy engine。in plain Python strategy inputs + OHLCV bars → out deterministic plans, previews, replays, and lifecycle receipts | Owned | owned source |

### Trading Infra (6)

| Repo | Capability / description | Source | Lock / flags |
|---|---|---|---|
| [ccxt/ccxt](https://github.com/ccxt/ccxt) | A unified trading API with more than 100 crypto exchanges and prediction markets in JavaScript / TypeScript / Python / C# / PHP / Go / Java | Starred | `9e233b6a18ec` |
| [Drakkar-Software/OctoBot](https://github.com/Drakkar-Software/OctoBot) | Free open source crypto trading bot to automate AI, Grid, DCA and TradingView strategies on Binance, Hyperliquid and 15+ exchanges, with a simple interface. | Starred | `dc0efc8ec36c` |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | Production-grade Rust-native trading engine with deterministic event-driven architecture | Starred | `41e178f6bc62` |
| [polakowo/vectorbt](https://github.com/polakowo/vectorbt) | The backtesting engine that gives you an unfair advantage. Run thousands of trading ideas before others finish one. | Starred | `34b6d5935e3e` |
| [zinan92/standard-broker](https://github.com/zinan92/standard-broker) | Provider-neutral broker Ports & Adapters for Paper-safe trading systems | Owned | owned source · PRIVATE |
| [zinan92/trading-system](https://github.com/zinan92/trading-system) | Gold trading system orchestrator | Owned | owned source · PRIVATE |

### Dashboard (5)

| Repo | Capability / description | Source | Lock / flags |
|---|---|---|---|
| [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | TradingView Screener API - Stock, Crypto, Forex, Bond, Futures, Coin | Starred | `38f74a11d4b5` |
| [gloom-sh/gloomberb](https://github.com/gloom-sh/gloomberb) | Finance terminal, in your terminal. | Starred | `cb6dbe6fe5ab` |
| [Mathieu2301/TradingView-API](https://github.com/Mathieu2301/TradingView-API) | 📈 Get real-time stocks from TradingView | Starred | `5baea86c8c7e` |
| [zinan92/human-kline-review](https://github.com/zinan92/human-kline-review) | Park 人工宏观 K 线复盘与 DeepSeek 汇总：HTML-first，Telegram later | Owned | owned source · PRIVATE |
| [zinan92/standard-kline](https://github.com/zinan92/standard-kline) | 标准 K 线前端组件。in OHLCV bars + provider metadata → out candlestick chart + volume + overlays + synthetic watermark | Owned | owned source |

### Full Trading System / Agent (10)

| Repo | Capability / description | Source | Lock / flags |
|---|---|---|---|
| [handsomejustin/easy_tdx](https://github.com/handsomejustin/easy_tdx) | 免费Python量化SDK:通达信协议直连 A股/港股/美股数据,内置技术指标、缠论分析、回测引擎与 Web 可视化,JSON 输出适配 AI Agent | Starred | `7c9e19de9379` |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | "Vibe-Trading: Your Personal Trading Agent" | Starred | `5cd08ee1bd5c` |
| [lzwme/finance-quant-skills](https://github.com/lzwme/finance-quant-skills) | 一个面向金融量化交易领域的 Agent Skills 技能维护仓库，主要聚焦A股量化交易。 | Starred | `b03516e6d6e6` |
| [OpenByteInc/QuantDinger](https://github.com/OpenByteInc/QuantDinger) | AI quantitative trading platform for crypto, stocks, and forex with backtesting, live trading, market data, and multi-agent research.vibe-trading ,trading-agents,ai-trader,ai-trading | Starred | `615d90c823c4` |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Kronos: A Foundation Model for the Language of Financial Markets | Starred | `67b630e67f6a` |
| [shy3130/tick-stock-panel](https://github.com/shy3130/tick-stock-panel) | TSP自托管、零运维的 A 股「选股 + 监控 + 回测」量化工作台 \| 基于 TickFlow 数据源  \| LLM能力驱使策略定制+个股分析+复盘 \| 自由接入第三方数据源与个性化扩展数据 \| 个人开源 ,非第三方官方项目 | Starred | `e346e25101c7` |
| [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research) | Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。 | Starred | `ab4ffa077e0b` |
| [sngyai/Sequoia-X](https://github.com/sngyai/Sequoia-X) | A股自动选股系统 — 多种技术形态自动扫描，收盘后自动运行并推送飞书 | Starred | `444c0db69ff3` |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | TradingAgents: Multi-Agents LLM Financial Trading Framework | Starred | `a33fd4c0f134` |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。  LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | Starred | `fb4735a1055c` |

### Knowledge & Collections (6)

| Repo | Capability / description | Source | Lock / flags |
|---|---|---|---|
| [bwjoke/BTC-Trading-Since-2020](https://github.com/bwjoke/BTC-Trading-Since-2020) | Public BTC trading context since 2020. | Starred | `f02a691c7f7c` |
| [LLMQuant/quant-wiki](https://github.com/LLMQuant/quant-wiki) | We are committed to the open-sourcing quantitative knowledge, aiming to bridge the information gap between the domestic and international quantitative finance industries. 我们致力于量化知识的开源与汉化，打破国内外量化金融行业信息差。 | Starred | `f08b94e13425` |
| [RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) | A collection of Awesome Finance Agent Skills for free and easy to start \| 一系列开源免费的金融分析Agent Skills | Starred | `853f09b4d0ba` |
| [wangzhe3224/awesome-systematic-trading](https://github.com/wangzhe3224/awesome-systematic-trading) | A curated list of insanely awesome libraries, packages and resources for systematic trading. Crypto, Stock, Futures, Options, CFDs, FX, and more \| 量化交易 \| 量化投资 | Starred | `cd4389c9482b` |
| [wilsonfreitas/awesome-quant](https://github.com/wilsonfreitas/awesome-quant) | A curated list of insanely awesome libraries, packages and resources for Quants (Quantitative Finance) | Starred | `0801566f5815` |
| [zinan92/copilot](https://github.com/zinan92/copilot) | 方法论路由。in 信号+上下文 → out 44套方法论匹配分析 | Owned + Starred | owned source · PRIVATE |

## Update contract

This README and the generated data are scoped views. Taxonomy, source state and lock authority remain in Park OS.

```bash
bash scripts/verify-scoped.sh
```

The registry is a catalog, not a production-readiness or execution-authorization claim.
