# Trading

**用一个可审计的 stage map 浏览 Trading universe。**

---

```text
in  GitHub owned repos + starred repos at a fixed canonical snapshot
out stage catalog + Owned/Starred separation + locked external refs
```

Canonical snapshot: `github-universe-2026-08-26` · entries: `57`

## At a glance

| Stage | Owned | Starred | Total |
|---|---:|---:|---:|
| 01 Market Data & Feeds | 8 | 13 | 21 |
| 02 Research & Analysis | 1 | 6 | 7 |
| 03 Strategies & Trader Methodologies | 0 | 2 | 2 |
| 04 Backtesting & Simulation | 2 | 1 | 3 |
| 05 Execution & Trading Infrastructure | 1 | 7 | 8 |
| 06 Research & Decision Interfaces | 0 | 6 | 6 |
| 07 Full Trading Systems | 2 | 5 | 7 |
| 08 Knowledge & Collections | 0 | 3 | 3 |

## 01 Market Data & Feeds

### Owned

| Repo | Capability | State |
|---|---|---|
| [zinan92/chancode](https://github.com/zinan92/chancode) |  | BUILDING |
| [zinan92/copilot](https://github.com/zinan92/copilot) | 方法论路由。in 信号+上下文 → out 44套方法论匹配分析 | BUILDING |
| [zinan92/datafeed](https://github.com/zinan92/datafeed) | 行情数据。in ticker+timeframe → out OHLCV candles。A股/美股/加密/商品 | BUILDING |
| [zinan92/human-kline-review](https://github.com/zinan92/human-kline-review) | Park 人工宏观 K 线复盘与 DeepSeek 汇总：HTML-first，Telegram later | BUILDING |
| [zinan92/intel](https://github.com/zinan92/intel) | 情报采集。in 10+信息源 → out LLM评分+跨源事件聚类 | BUILDING |
| [zinan92/market-direction](https://github.com/zinan92/market-direction) |  | BUILDING |
| [zinan92/quant-data-pipeline](https://github.com/zinan92/quant-data-pipeline) | 多市场量化数据平台 — A股/美股/加密/商品，28组API，感知信号引擎，模拟交易 | BUILDING |
| [zinan92/standard-kline](https://github.com/zinan92/standard-kline) | 标准 K 线前端组件。in OHLCV bars + provider metadata → out candlestick chart + volume + overlays + synthetic watermark | BUILDING |

### Starred

| Repo | Capability | State / Lock |
|---|---|---|
| [1nchaos/adata](https://github.com/1nchaos/adata) | 免费开源A股量化交易数据库； 专注A股，专注量化，向阳而生； 开放、纯净、持续、为Ai(爱)发电。为个人量化交易而生，保卫3000点，珍惜底部机会......【股票数据，股票行情数据，股票量化数据，股票交易数据，k线行情数据，股票概念数据，股票数据接口，行情数据接口，量化交易数据】【多数据源融合，动态设置代理，保障数据高可用性】 | lock b14f4e57b217 |
| [JerBouma/FinanceDatabase](https://github.com/JerBouma/FinanceDatabase) | This is a database of 300.000+ symbols containing Equities, ETFs, Funds, Indices, Currencies, Cryptocurrencies and Money Markets. | lock e3c554bb5110 |
| [TA-Lib/ta-lib-python](https://github.com/TA-Lib/ta-lib-python) | Python wrapper for TA-Lib (http://ta-lib.org/). | lock a9ff1b47b3dd |
| [akfamily/akshare](https://github.com/akfamily/akshare) | AKShare is an elegant and simple financial data interface library for Python, built for human beings! 开源财经数据接口库 | lock 0e7db00cb98a |
| [bwjoke/BTC-Trading-Since-2020](https://github.com/bwjoke/BTC-Trading-Since-2020) | Public BTC trading context since 2020. | lock f02a691c7f7c |
| [handsomejustin/easy_tdx](https://github.com/handsomejustin/easy_tdx) | 免费Python量化SDK:通达信协议直连 A股/港股/美股数据,内置技术指标、缠论分析、回测引擎与 Web 可视化,JSON 输出适配 AI Agent | lock 7c9e19de9379 |
| [lzwme/finance-quant-skills](https://github.com/lzwme/finance-quant-skills) | 一个面向金融量化交易领域的 Agent Skills 技能维护仓库，主要聚焦A股量化交易。 | lock b03516e6d6e6 |
| [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | A股全栈数据工具包 · 十一层架构 · 54端点 · 19数据源 · 零鉴权 / Full-stack China A-share data toolkit for AI agents — 11 layers, 54 endpoints, 19 sources, zero-auth | lock f90d67853b81 |
| [sstklen/trump-code](https://github.com/sstklen/trump-code) | 🔐 AI decoding Trump's posts × stock market / AI 解碼川普推文 × 美股 / AIでトランプ投稿×株式市場を解読 — 31.5M models, 61.3% hit rate, open source | lock ec5e2de1f7a0 |
| [star23/Day1Global-Skills](https://github.com/star23/Day1Global-Skills) | Day1Global Skills Share: US Stock, Macro Market, Crypto | lock 562c14b0c0bc |
| [tradecatlabs/tradecat-public](https://github.com/tradecatlabs/tradecat-public) | 交易猫数据系统 | lock 71430dee0449 |
| [waditu/czsc](https://github.com/waditu/czsc) | 缠中说禅技术分析工具；缠论；股票；期货；Quant；量化交易 | lock 701e480a5450 |
| [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | 冰冷的钱就这样流进我温暖的口袋-游资（UZI）Skills — 让我们欢迎，股海贼王！66位投资大佬帮你看盘 · 22维数据 × 180条量化规则 × 17种机构分析方法 · A股/港股/美股  | lock b004d7a988ca |

## 02 Research & Analysis

### Owned

| Repo | Capability | State |
|---|---|---|
| [zinan92/equity-research](https://github.com/zinan92/equity-research) | A股长期投委会 + 证据快照深度研报平台(Park 产品层) | BUILDING |

### Starred

| Repo | Capability | State / Lock |
|---|---|---|
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | TradingAgents: Multi-Agents LLM Financial Trading Framework | lock a33fd4c0f134 |
| [anthropics/financial-services](https://github.com/anthropics/financial-services) |  | lock 69cbc81467a5 |
| [microsoft/qlib](https://github.com/microsoft/qlib) | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped with https://github.com/microsoft/RD-Agent to automate R&D process. | lock 79633dd9506e |
| [rollingSirius/equity-research-skill](https://github.com/rollingSirius/equity-research-skill) | Possibly the deepest AI equity-research skill: nine-chapter single-stock deep dives and earnings deep-dives, with scripted DCF/EPV/EVA and reproducible valuation. Covers US, HK and A-shares. Docs in EN and ZH. | lock 3d94e64ff53b |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Kronos: A Foundation Model for the Language of Financial Markets | lock 67b630e67f6a |
| [virattt/dexter](https://github.com/virattt/dexter) | An autonomous agent for deep financial research | lock ecaed3011f24 |

## 03 Strategies & Trader Methodologies

### Owned

| Repo | Capability | State |
|---|---|---|

### Starred

| Repo | Capability | State / Lock |
|---|---|---|
| [RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) | A collection of Awesome Finance Agent Skills for free and easy to start / 一系列开源免费的金融分析Agent Skills | lock 853f09b4d0ba |
| [muxuuu/serenity-skill](https://github.com/muxuuu/serenity-skill) | Serenity-inspired Agent Skill for supply-chain bottleneck stock research | lock c2fe93deedfd |

## 04 Backtesting & Simulation

### Owned

| Repo | Capability | State |
|---|---|---|
| [zinan92/backtest](https://github.com/zinan92/backtest) | 回测验证。in 策略定义 → out 胜率/盈亏比/最大回撤 | BUILDING |
| [zinan92/trading-strategy](https://github.com/zinan92/trading-strategy) | Engine-neutral Canonical DCA/Grid strategy engine。in plain Python strategy inputs + OHLCV bars → out deterministic plans, previews, replays, and lifecycle receipts | BUILDING |

### Starred

| Repo | Capability | State / Lock |
|---|---|---|
| [polakowo/vectorbt](https://github.com/polakowo/vectorbt) | The backtesting engine that gives you an unfair advantage. Run thousands of trading ideas before others finish one. | lock 34b6d5935e3e |

## 05 Execution & Trading Infrastructure

### Owned

| Repo | Capability | State |
|---|---|---|
| [zinan92/standard-broker](https://github.com/zinan92/standard-broker) | Provider-neutral broker Ports & Adapters for Paper-safe trading systems | BUILDING |

### Starred

| Repo | Capability | State / Lock |
|---|---|---|
| [binance/binance-api-postman](https://github.com/binance/binance-api-postman) | Postman collection for Binance Public API, including spot, margin, futures, etc. | lock 1cfce10c2224 |
| [binance/binance-connector-python](https://github.com/binance/binance-connector-python) | Simple connector to Binance Public API | lock bbd692747487 |
| [bmino/binance-triangle-arbitrage](https://github.com/bmino/binance-triangle-arbitrage) | Detect in-market cryptocurrency arbitrage | lock 9051359ade27 |
| [ccxt/ccxt](https://github.com/ccxt/ccxt) | A unified trading API with more than 100 crypto exchanges and prediction markets in JavaScript / TypeScript / Python / C# / PHP / Go / Java  | lock 9e233b6a18ec |
| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | Production-grade Rust-native trading engine with deterministic event-driven architecture | lock 41e178f6bc62 |
| [sammchardy/python-binance](https://github.com/sammchardy/python-binance) | Binance Exchange API python implementation for automated trading | lock 7d7b7fb02963 |
| [vnpy/vnpy](https://github.com/vnpy/vnpy) | 基于Python的开源量化交易平台开发框架 | lock fa5206fe6383 |

## 06 Research & Decision Interfaces

### Owned

| Repo | Capability | State |
|---|---|---|

### Starred

| Repo | Capability | State / Lock |
|---|---|---|
| [Mathieu2301/TradingView-API](https://github.com/Mathieu2301/TradingView-API) | 📈 Get real-time stocks from TradingView | lock 5baea86c8c7e |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Open Data Platform for analysts, quants and AI agents. | lock 3e071fcc2cd9 |
| [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | TradingView Screener API - Stock, Crypto, Forex, Bond, Futures, Coin | lock 38f74a11d4b5 |
| [gloom-sh/gloomberb](https://github.com/gloom-sh/gloomberb) | Finance terminal, in your terminal. | lock cb6dbe6fe5ab |
| [simonlin1212/global-stock-data](https://github.com/simonlin1212/global-stock-data) | US stock market data for AI coding assistants — zero-auth, official sources. CBOE options with full Greeks + 0DTE flow, FINRA market-wide short volume, SEC EDGAR filing stream, and a free market-wide screener. 13 layers, 30+ endpoints, 11 sources. Every source labeled with its compliance tier. | lock c0b3ed8d8a1f |
| [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) | Claude Code skills for equity investors and traders — market analysis, technical charting, economic calendars, screeners, and trading strategy development. | lock 51c790740048 |

## 07 Full Trading Systems

### Owned

| Repo | Capability | State |
|---|---|---|
| [zinan92/gold-trading](https://github.com/zinan92/gold-trading) |  | BUILDING |
| [zinan92/trading-system](https://github.com/zinan92/trading-system) | Gold trading system orchestrator | BUILDING |

### Starred

| Repo | Capability | State / Lock |
|---|---|---|
| [Drakkar-Software/OctoBot](https://github.com/Drakkar-Software/OctoBot) | Free open source crypto trading bot to automate AI, Grid, DCA and TradingView strategies on Binance, Hyperliquid and 15+ exchanges, with a simple interface. | lock dc0efc8ec36c |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | "Vibe-Trading: Your Personal Trading Agent" | lock 5cd08ee1bd5c |
| [OpenByteInc/QuantDinger](https://github.com/OpenByteInc/QuantDinger) | AI quantitative trading platform for crypto, stocks, and forex with backtesting, live trading, market data, and multi-agent research.vibe-trading ,trading-agents,ai-trader,ai-trading | lock 615d90c823c4 |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。  LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | lock fb4735a1055c |
| [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research) | Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。 | lock ab4ffa077e0b |

## 08 Knowledge & Collections

### Owned

| Repo | Capability | State |
|---|---|---|

### Starred

| Repo | Capability | State / Lock |
|---|---|---|
| [LLMQuant/quant-wiki](https://github.com/LLMQuant/quant-wiki) | We are committed to the open-sourcing quantitative knowledge, aiming to bridge the information gap between the domestic and international quantitative finance industries. 我们致力于量化知识的开源与汉化，打破国内外量化金融行业信息差。 | lock f08b94e13425 |
| [wangzhe3224/awesome-systematic-trading](https://github.com/wangzhe3224/awesome-systematic-trading) | A curated list of insanely awesome libraries, packages and resources for systematic trading. Crypto, Stock, Futures, Options, CFDs, FX, and more / 量化交易 / 量化投资 | lock cd4389c9482b |
| [wilsonfreitas/awesome-quant](https://github.com/wilsonfreitas/awesome-quant) | A curated list of insanely awesome libraries, packages and resources for Quants (Quantitative Finance) | lock 0801566f5815 |

## Reading and update rules

- `Owned` = zinan92 repo；`Starred` = external repo。
- 每个 repo 只有一个 primary stage；跨阶段能力用 tags 表达。
- Starred repo 展示 locked commit 短 SHA，不跟随实时 default branch。
- Private link 点不开是允许状态，必须保留 `PRIVATE` 标记。
- Canonical locks and scoped exports live in [Park OS](https://github.com/zinan92/park-operating-system).

## For AI agents

```yaml
name: trading-universe
universe: trading
source_of_truth: https://github.com/zinan92/park-operating-system
snapshot_id: github-universe-2026-08-26
entry_count: 57
external_versioning: locked_commit_sha
```

The registry is a catalog of links and metadata. Validation does not certify product readiness.

