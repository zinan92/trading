<!-- 本文件由 scripts/render-hub.py 生成，请改 evaluations/assessments/*.json 后重跑 -->
# Trading · Pipeline 评测总览

每个库放到交易 pipeline 的对应环节，按该环节的标准评判它是否做到了自己声称的用途，证据是首轮实测的截图与记录。标准与分数推导见 [评测框架](FRAMEWORK.md)。

## Pipeline 十个环节与已实测跑通的产品

| # | 环节 | 输入 → 输出 | 实测跑通 ● | 源码可见 ◐ |
|---:|---|---|---|---|
| 1 | 数据获取 | 外部源 → 原始行情、基本面、新闻、事件 | [A Share Heatmap](dashboard/README.md#a-share-heatmap)、[Maverick MCP](equity-research/README.md#maverick-mcp)、[FinanceDatabase](data/README.md#financedatabase)、[Gloomberb](dashboard/README.md#gloomberb)、[Vibe AStock](dashboard/README.md#vibe-astock)、[datafeed](data/README.md#datafeed)、[tick-stock-panel](full-trading-system/README.md#tick-stock-panel)、[akshare](data/README.md#akshare)、[KHunter](full-trading-system/README.md#khunter)、[tickflow](data/README.md#tickflow)、[a-stock-data](data/README.md#a-stock-data)、[Qlib](trading-strategy/README.md#qlib)、[FinanceMCP](data/README.md#financemcp)、[adata](data/README.md#adata)、[global-stock-data](data/README.md#global-stock-data)、[quant-data-pipeline](data/README.md#quant-data-pipeline)、[finance-quant-skills](full-trading-system/README.md#finance-quant-skills)、[easy-stock](full-trading-system/README.md#easy-stock)、[UZI Skill](equity-research/README.md#uzi-skill)、[tradingview-mcp](data/README.md#tradingview-mcp)、[intel](data/README.md#intel)、[TradingView-API](data/README.md#tradingview-api)、[daily_stock_analysis](full-trading-system/README.md#daily-stock-analysis)、[OpenStock](dashboard/README.md#openstock)、[Sequoia-X](full-trading-system/README.md#sequoia-x)、[tvscreener](data/README.md#tvscreener)、[go-stock](full-trading-system/README.md#go-stock)、[TradeGenuis-Options](full-trading-system/README.md#tradegenuis-options)、[Day1Global Skills](equity-research/2026-09-28/03-day1global-skills/findings.md) | Human K-line Review、Financial-API、trump-code、finhack、fomomo、Vibe-Research、Vibe-Trading、QuantDinger、TradingAgents、standard-broker、NautilusTrader、trading-system、CCXT、OctoBot、chan.py、CZSC、WyckoffTradingAgent、Meme Radar、Chancode |
| 2 | 清洗与标准化 | 原始数据 → 统一 schema：代码、时区、复权、缺失处理 | [watchlist](data/README.md#watchlist)、[FinanceDatabase](data/README.md#financedatabase)、[datafeed](data/README.md#datafeed)、[tick-stock-panel](full-trading-system/README.md#tick-stock-panel)、[CZSC](trading-strategy/README.md#czsc)、[tickflow](data/README.md#tickflow)、[a-stock-data](data/README.md#a-stock-data)、[adata](data/README.md#adata)、[intel](data/README.md#intel)、[CCXT](trading-infra/README.md#ccxt) | tvscreener、Vibe AStock、Financial-API、global-stock-data、quant-data-pipeline、akshare、UZI Skill、easy-stock、trading-system、Qlib |
| 3 | 数据存档 | 标准数据 → 可回放的历史库：增量、快照、版本 | [watchlist](data/README.md#watchlist)、[FinanceDatabase](data/README.md#financedatabase)、[tick-stock-panel](full-trading-system/README.md#tick-stock-panel)、[KHunter](full-trading-system/README.md#khunter)、[Qlib](trading-strategy/README.md#qlib)、[trump-code](trading-strategy/README.md#trump-code)、[easy-stock](full-trading-system/README.md#easy-stock)、[intel](data/README.md#intel)、[daily_stock_analysis](full-trading-system/README.md#daily-stock-analysis) | Vibe AStock、Financial-API、datafeed、quant-data-pipeline、Maverick MCP、Equity Research、UZI Skill、go-stock、finhack、QuantDinger、NautilusTrader、trading-system、Chancode |
| 4 | 指标与特征 | 历史库 → 指标、因子序列 | [Maverick MCP](equity-research/README.md#maverick-mcp)、[TA-Lib](trading-strategy/README.md#ta-lib-python)、[Gloomberb](dashboard/README.md#gloomberb)、[standard-kline](dashboard/README.md#standard-kline)、[Vibe AStock](dashboard/README.md#vibe-astock)、[tick-stock-panel](full-trading-system/README.md#tick-stock-panel)、[CZSC](trading-strategy/README.md#czsc)、[vectorbt](trading-infra/README.md#vectorbt)、[Human K-line Review](dashboard/README.md#human-kline-review)、[Equity Research Skill](equity-research/README.md#equity-research-skill)、[Qlib](trading-strategy/README.md#qlib)、[NautilusTrader](trading-infra/README.md#nautilus-trader)、[FinanceMCP](data/README.md#financemcp)、[global-stock-data](data/README.md#global-stock-data)、[easy-stock](full-trading-system/README.md#easy-stock)、[chan.py](trading-strategy/README.md#chan-py)、[UZI Skill](equity-research/README.md#uzi-skill)、[tradingview-mcp](data/README.md#tradingview-mcp)、[intel](data/README.md#intel)、[Sequoia-X](full-trading-system/README.md#sequoia-x)、[Kronos](full-trading-system/README.md#kronos)、[Day1Global Skills](equity-research/2026-09-28/03-day1global-skills/findings.md) | TradingView-API、a-stock-data、quant-data-pipeline、Equity Research、go-stock、finhack、KHunter、Vibe-Trading、QuantDinger、TradingAgents、WyckoffTradingAgent、FMZ strategies、Meme Radar、Chancode |
| 5 | 策略与信号 | 指标 → 买卖信号或目标仓位 | [Maverick MCP](equity-research/README.md#maverick-mcp)、[Vibe AStock](dashboard/README.md#vibe-astock)、[tick-stock-panel](full-trading-system/README.md#tick-stock-panel)、[trading-strategy](trading-strategy/README.md#trading-strategy)、[CZSC](trading-strategy/README.md#czsc)、[vectorbt](trading-infra/README.md#vectorbt)、[KHunter](full-trading-system/README.md#khunter)、[Equity Research Skill](equity-research/README.md#equity-research-skill)、[NautilusTrader](trading-infra/README.md#nautilus-trader)、[trump-code](trading-strategy/README.md#trump-code)、[easy-stock](full-trading-system/README.md#easy-stock)、[UZI Skill](equity-research/README.md#uzi-skill)、[Chancode](trading-strategy/README.md#chancode)、[tradingview-mcp](data/README.md#tradingview-mcp)、[Sequoia-X](full-trading-system/README.md#sequoia-x) | quant-data-pipeline、Day1Global Skills、Equity Research、Serenity Skill、go-stock、finhack、fomomo、TradeGenuis-Options、finance-quant-skills、Vibe-Research、Vibe-Trading、daily_stock_analysis、QuantDinger、TradingAgents、trading-system、OctoBot、chan.py、Qlib、WyckoffTradingAgent、FMZ strategies、Meme Radar |
| 6 | 回测 | 策略 + 历史 → 绩效、成交、曲线 | [Vibe AStock](dashboard/README.md#vibe-astock)、[tick-stock-panel](full-trading-system/README.md#tick-stock-panel)、[trading-strategy](trading-strategy/README.md#trading-strategy)、[CZSC](trading-strategy/README.md#czsc)、[vectorbt](trading-infra/README.md#vectorbt)、[KHunter](full-trading-system/README.md#khunter)、[NautilusTrader](trading-infra/README.md#nautilus-trader)、[finance-quant-skills](full-trading-system/README.md#finance-quant-skills)、[Chancode](trading-strategy/README.md#chancode)、[tradingview-mcp](data/README.md#tradingview-mcp) | trump-code、Maverick MCP、finhack、Vibe-Research、Vibe-Trading、daily_stock_analysis、QuantDinger、easy-stock、OctoBot、Qlib |
| 7 | 策略管理 | 回测结果 → 注册、参数版本、paper→live 晋级、下线 | [QuantDinger](full-trading-system/README.md#quantdinger) | trump-code、Equity Research、KHunter、tick-stock-panel、Vibe-Trading、NautilusTrader、trading-system、trading-strategy、Qlib |
| 8 | 风控 | 目标订单 → 通过、拒绝或缩量：仓位、敞口、熔断 | — | quant-data-pipeline、Equity Research、standard-broker、NautilusTrader、trading-system、trading-strategy |
| 9 | 执行与券商 | 通过的订单 → 委托、成交、持仓与资金对账 | [quant-data-pipeline](data/README.md#quant-data-pipeline) | finhack、KHunter、tick-stock-panel、finance-quant-skills、Vibe-Trading、QuantDinger、standard-broker、NautilusTrader、trading-system、CCXT、OctoBot、Chancode |
| 10 | 监控与看板 | 全链路状态 → 人能快速看懂并干预 | [A Share Heatmap](dashboard/README.md#a-share-heatmap)、[Gloomberb](dashboard/README.md#gloomberb)、[standard-kline](dashboard/README.md#standard-kline)、[Vibe AStock](dashboard/README.md#vibe-astock)、[datafeed](data/README.md#datafeed)、[tick-stock-panel](full-trading-system/README.md#tick-stock-panel)、[Human K-line Review](dashboard/README.md#human-kline-review)、[trump-code](trading-strategy/README.md#trump-code)、[quant-data-pipeline](data/README.md#quant-data-pipeline)、[easy-stock](full-trading-system/README.md#easy-stock)、[Trading Desk](dashboard/README.md#trading-desk)、[intel](data/README.md#intel)、[Equity Research](equity-research/README.md#equity-research)、[trading-system](full-trading-system/README.md#trading-system)、[OpenStock](dashboard/README.md#openstock)、[Meme Radar](trading-strategy/README.md#meme-radar)、[WyckoffTradingAgent](trading-strategy/README.md#wyckofftradingagent) | go-stock、KHunter、TradeGenuis-Options、Sequoia-X、Vibe-Research、Vibe-Trading、daily_stock_analysis、QuantDinger、OctoBot、Chancode |

## 按类别

| 类别 | 目标 | 评测数 | 已排名 | 类内首位 | 页面 |
|---|---|---:|---:|---|---|
| Data | 取得正确、及时、完整的交易数据，最好免费，并且下游能直接接入。 | 15 | 14 | [FinanceDatabase](data/README.md#financedatabase) · 80 | [打开](data/README.md) |
| Equity Research | 为买卖决策提供可核验、可复现的研判，而不是一段无法追溯的文字。 | 6 | 5 | [Maverick MCP](equity-research/README.md#maverick-mcp) · 83 | [打开](equity-research/README.md) |
| Trading Strategy | 策略与指标知识库全面（尽量互斥且穷尽）、计算正确、能直接送进回测。 | 11 | 8 | [TA-Lib](trading-strategy/README.md#ta-lib-python) · 80 | [打开](trading-strategy/README.md) |
| Trading Infra | 回测→风控→执行的骨架可靠，组件可以单独替换。 | 5 | 5 | [standard-broker](trading-infra/README.md#standard-broker) · 75 | [打开](trading-infra/README.md) |
| Dashboard | 人能快速、清晰地找到信息，并在需要时干预。 | 7 | 7 | [A Share Heatmap](dashboard/README.md#a-share-heatmap) · 83 | [打开](dashboard/README.md) |
| Full Trading System / Agent | 有完整骨架，各环节先解耦再重耦，能跑通一次 paper 闭环。 | 16 | 13 | [tick-stock-panel](full-trading-system/README.md#tick-stock-panel) · 70 | [打开](full-trading-system/README.md) |
| Knowledge & Collections | 参考资料，不评测。 | — | — | 不评测；建议归入：[Day1Global Skills](equity-research/2026-09-28/03-day1global-skills/findings.md) | — |

## 分类建议

评测意见，不改 canonical 目录。

| 产品 | 目录类别 | 建议类别 | 说明 |
|---|---|---|---|
| [tvscreener](data/README.md#tvscreener) | Dashboard | Data | 目录归 Dashboard，但主体是 Python 数据客户端，17 张截图全部来自仓库自带的本地静态 Code Generator，不含行情画面；本卡按 Data 标准 D1..D5 评，建议改归 Data。离线单测 129 通过。 |
| [TradingView-API](data/README.md#tradingview-api) | Dashboard | Data | 没有原生 UI，13 张截图均为锁定版本的 README、示例、测试与 WebSocket 源码页；运行结果见 verification.json。目录归 Dashboard，本卡按 Data 标准 D1..D5 评，建议改归 Data。 |
| [A Share Heatmap](dashboard/README.md#a-share-heatmap) | Equity Research | Dashboard | 目录归 Equity Research，锁为 c15f94e6；实测源码 6b4b6744 与目录锁不同。24 张截图从 equity-research/2026-09-28/02-a-share-heatmap（2026-09-27 试用）复用，文件哈希一致，本轮未重新运行产品；以市场宽度与板块看板为核心，建议改归 Dashboard。 |
| [trump-code](trading-strategy/README.md#trump-code) | Data | Trading Strategy | 目录归 Data，但角色是事件信号研究，本卡按 Trading Strategy 标准 S1–S5 评；截图 16–30 对应 15 条探针，31 为仓库 JSON 复算。实测源码晚于目录锁。 |
| [Day1Global Skills](equity-research/2026-09-28/03-day1global-skills/findings.md) | Equity Research | Knowledge & Collections | Codex 建议归 Knowledge & Collections；该类不设标准、不评分，本卡只记录事实。 |
| [trading-system](full-trading-system/README.md#trading-system) | Trading Infra | Full Trading System / Agent | 目录归 Trading Infra，但它是完整平台，本卡按 Full Trading System / Agent 的 F1–F5 评；建议主类迁出，standard-broker 等组件留在 Infra。指标与回测环节本轮记录未见，按无计。浏览器只读：0 次写请求、0 个未捕获页面错误。 |
| [Qlib](trading-strategy/README.md#qlib) | Equity Research | Trading Strategy | 从 Equity Research 轮次转入；实测提交 be725493 与目录锁 79633dd9 不同。样本数据来自 Yahoo Finance，日历 3,995 个交易日（2005-01-04 至 2021-06-11）。 |
| [finhack](full-trading-system/README.md#finhack) | Full Trading System / Agent | Trading Infra | 记录定位为量化开发框架 / Trading Infra。实际试用 PyPI 包，源码 SHA 未记录，与目录锁不能直接对应。 |
| [Sequoia-X](full-trading-system/README.md#sequoia-x) | Full Trading System / Agent | Trading Strategy | 记录定位为 CLI 选股引擎 / Trading Strategy；所有网页截图来自辅助试用台，上游无原生 Web UI。 |
| [finance-quant-skills](full-trading-system/README.md#finance-quant-skills) | Full Trading System / Agent | Knowledge & Collections | 记录定位为 Knowledge & Collections / Agent Skills；按框架该类别不评测，F2–F4 记不适用。实际试用 SHA 与目录锁不同。 |
| [Kronos](full-trading-system/README.md#kronos) | Full Trading System / Agent | Trading Strategy | 记录定位为金融预测模型 / Trading Strategy 组件；输入为真实 BaoStock 数据，由试用侧提供，因此 fetch 记不在角色内。 |
| [Vibe-Research](full-trading-system/README.md#vibe-research) | Full Trading System / Agent | Equity Research | 记录定位为个人投研 Agent / Equity Research。图库含 9 张编号 07-0xx 的手动截图，属本产品试用。实际试用 SHA 与目录锁不同。 |
| [daily_stock_analysis](full-trading-system/README.md#daily-stock-analysis) | Full Trading System / Agent | Equity Research | 记录定位为研究报告与自动推送 / Equity Research。目录声称多市场但记录只测了 A 股 600519，markets 只记已见部分。实际试用 SHA 与目录锁不同。 |
| [TradingAgents](full-trading-system/README.md#tradingagents) | Full Trading System / Agent | Trading Strategy | 记录定位为 CLI 研究决策 Agent 框架；所有网页截图为 Product Lab 辅助页，上游只有 CLI/Python 包。超时不能全归于限流。实际试用 SHA 与目录锁不同。 |
| [easy-stock](full-trading-system/README.md#easy-stock) | Full Trading System / Agent | Equity Research | 源码有带费用、滑点、次日成交和涨跌停规则的 inflection 回测，但没有 API 入口和测试；许可证为非商业使用。 |
| [OctoBot](trading-infra/README.md#octobot) | Trading Infra | Full Trading System / Agent | 记录中的实测提交 d63148e5 与目录锁 dc0efc8e 不一致，本卡以记录为准，需复核锁值。记录建议改归 Full Trading System：它是带 UI 与自动交易的整机，不是可复用的 Infra 组件。 |
| [one-quant-doc](trading-strategy/README.md#one-quant-doc) | Trading Strategy | Knowledge & Collections | 首轮记 N/A 未排名。仓库本身属产品说明文档；托管产品若可用更适合按 Dashboard 评。 |

## 全部产品

环节列按 1 获取、2 清洗、3 存档、4 指标、5 策略、6 回测、7 管理、8 风控、9 执行、10 看板的顺序排列：● 实测跑通 · ◐ 源码可见 · ○ 无 · · 不在角色内。

| 产品 | 评测类别 | 分数 | 已验证 | 环节 1–10 | 实测 |
|---|---|---:|---:|---|---|
| [FinanceDatabase](data/README.md#financedatabase) | Data | 80 | 100% | `●●●·······` | ✅ 七类本地数据集合计 305,512 行全部可加载，AAPL / 600519.SS / 0700.HK 精确检索正确；BTC-USD 缺失与 .SH 后缀不匹配是接入边界。 |
| [watchlist](data/README.md#watchlist) | Data | 80 | 100% | `·●●·······` | ✅ YAML 解析与引用校验 7/8 通过：16 资产 / 6 宏观 / 26 赛道 / 119 唯一 target；唯一 finding 是目录摘要（24/109）已过时。 |
| [datafeed](data/README.md#datafeed) | Data | 73 | 100% | `●●◐······●` | ✅ 上证、茅台、AAPL、BTC、美债 10Y、黄金均返回 count=5 的标准蜡烛；健康矩阵 0 单元有数据、ticker 搜索为 0、免费源标 entitlement_unverified。 |
| [akshare](data/README.md#akshare) | Data | 68 | 100% | `●◐○·······` | 🟡 A 股日/分钟、ETF、AAPL、指数、期货、LPR、新闻真实取数至 09-24/25；东财日线 SSL 错误、ETF 现价 502，crypto_js_spot 仍为 2020/2023 旧价，FX 25 行买卖价全为 0。 |
| [tickflow](data/README.md#tickflow) | Data | 60 | 100% | `●●○·······` | 🟡 免费入口取得 A 股、ETF、美股、港股日/周 K 与标的元数据；分钟线与实时行情被 PermissionError 拒绝，财报未测。 |
| [a-stock-data](data/README.md#a-stock-data) | Data | 58 | 100% | `●●○◐······` | 🟡 腾讯/新浪路径真实取得报价、日/周/5 分钟 K、复权因子与财报；百度均线 K 返回空且不报错，87 端点只测样本 16 个。 |
| [adata](data/README.md#adata) | Data | 50 | 100% | `●●○·······` | 🟡 首次取得茅台 18 根日 K / 13 根周 K，补依赖后 ETF、指数分时、盘口有返回；复测茅台日 K 变 0 行、周 K 超时，两只股票现价因腾讯解析条件不匹配返回空表。 |
| [FinanceMCP](data/README.md#financemcp) | Data | 50 | 100% | `●○○●······` | 🟡 无凭证时只公开 4 个工具：Binance 加密日/分钟线与百度新闻有结果；A 股、美股路由返回“没有已配置的数据源”。 |
| [global-stock-data](data/README.md#global-stock-data) | Data | 50 | 100% | `●◐○●······` | 🟡 财政部收益率曲线 185 日、CFTC 20 条、FINRA 单日 12,349 符号有真实结果；主卖点 CBOE 期权、SEC EDGAR 与行情报价本轮未调用。 |
| [quant-data-pipeline](data/README.md#quant-data-pipeline) | Data | 50 | 100% | `●◐◐◐◐··◐●●` | 🟡 商品 4 品种、加密 15 品种实时与 K 线、美股 5 指数、本地纸盘买卖闭环成功；A 股搜索/行情 500、K 线 404、概念为 0，新闻请求超时后拖垮后端。 |
| [intel](data/README.md#intel) | Data | 40 | 100% | `●●●●·····●` | 🟡 隔离实例数分钟采集 4,610 篇、搜索可用、LLM 评分 500 篇；63 个事件 source_count 全为 1，跨源聚类没有通过样本。 |
| [tradingview-mcp](data/README.md#tradingview-mcp) | Data | 40 | 80% | `●○○●●●····` | 🟡 39 个工具中 23 个场景有结果：美/A/港股筛选、BTC 技术分析与回测；双标的报价 SSL 失败，新闻/情绪需 Key，周日无法验证实时。 |
| [TradingView-API](data/README.md#tradingview-api) | Data | 38 | 75% | `●○○◐······` | 🟡 无 SESSION/SIGNATURE 的 SimpleChart 示例加载 BINANCE:BTCEUR 日线，再切换 ETHEUR、15 分钟与 Heikin Ashi 后正常关闭；50 tests passed、16 skipped，私有指标与账户 API 因无 cookie 未测，股票标的也未实取。 |
| [tvscreener](data/README.md#tvscreener) | Data | 28 | 55% | `●◐○·······` | 🟡 无凭证的 S&P 500 公开查询 0.74 秒返回 10 行 DataFrame（含 NASDAQ:NVDA）；其余五类只在本地代码生成器构造了查询，没有实取；Valuation 预设生成了包里不存在的 StockField。 |
| [Financial-API](data/README.md#financial-api) | Data | 10 | 35% | `◐◐◐·······` | ⬜ 无 API Key：CLI 构建通过、104 项能力契约与本地 DuckDB 可读，但远端市场数据行数为 0，核心用途本轮无法判定。 |
| [Maverick MCP](equity-research/README.md#maverick-mcp) | Equity Research | 83 | 100% | `●○◐●●◐····` | 🟡 Core 1.1.0 的 37 个工具真实可用，AAPL 行情/技术/筛选与本地组合、自选、日志闭环跑通；深度研究与回测扩展未装，quote 的 timestamp 是取数时刻而非成交时间。 |
| [Equity Research Skill](equity-research/README.md#equity-research-skill) | Equity Research | 60 | 80% | `○··●●○····` | 🟡 估值脚本与检查器可跑（DCF demo 57.5/股、检查器测试 7/7），但本轮未生成新的真实九章研报，作者 NVDA 示例被仓库自身检查器判 1 个 P1。 |
| [Serenity Skill](equity-research/README.md#serenity-skill) | Equity Research | 50 | 100% | `○··○◐○····` | 🟡 validate_skill.py 返回 OK，8 个参考文档、3 篇示例、6 个手工用例可用，作者 CPO 案例的两处一手来源抽查成立；但本轮未让宿主 Agent 从零完成新主题研究。 |
| [UZI Skill](equity-research/README.md#uzi-skill) | Equity Research | 45 | 100% | `●◐◐●●○····` | 🟡 AAPL lite 真实生成 720KB 自包含 HTML 报告、分享卡与战报，覆盖率 72%；但币种、ROE 与来源叙述有可复验矛盾，critical_missing=true 时仍给精确价位，结论不能按已核验使用。 |
| [Equity Research](equity-research/README.md#equity-research) | Equity Research | 38 | 100% | `○·◐◐◐○◐◐·●` | ❌ fresh clone 只有 DEMO 结构：/api/health 报 data_mode=DEMO、report_count=0，/api/committee 为 0/8 深研、0% 可执行，本轮未产出任何真实研报；门禁按设计拒绝伪造，但组合页仍显示 +4.6% 收益。 |
| [Dexter](equity-research/README.md#dexter) | Equity Research | 0 | 0% | `··········` | ⬜ 按要求本轮跳过，未部署或运行。 |
| [TA-Lib](trading-strategy/README.md#ta-lib-python) | Trading Strategy | 80 | 100% | `···●······` | ✅ 锁定提交源码编译成功，80 项测试通过，201 个指标可枚举，500 根合成 OHLCV 上 SMA/RSI/MACD/BBANDS 经 NumPy/Pandas/Polars 三类接口均出值；实验性 stream 的 5 个递归指标与批量结果不一致。 |
| [trading-strategy](trading-strategy/README.md#trading-strategy) | Trading Strategy | 70 | 100% | `···○●●◐◐··` | ✅ 隔离安装成功，12 个确定性场景按预期输出：6 级 DCA 入场 3994→3920、目标 4040/止损 3880，网格 90–130 五档与数量，同一根 bar 上硬止损优先于新增档；聚焦测试 38 通过。 |
| [CZSC](trading-strategy/README.md#czsc) | Trading Strategy | 68 | 100% | `◐●·●●●····` | 🟡 离线链路 mock→质量检查→分析→研究/replay→回测→HTML 图表跑通；但核心 BI 固定基准 3 项失败，1.0.1 wheel 生成 31 笔而仓库基准为 43。 |
| [Qlib](trading-strategy/README.md#qlib) | Trading Strategy | 58 | 100% | `●◐●●◐◐◐···` | 🟡 隔离安装、CN 简版数据、表达式、Alpha158、LightGBM 训练与 2,094 条样本外预测跑通；数据止于 2021-06-11，SimulatorExecutor 导入超 2 分钟未完成，组合回测未验证。 |
| [chan.py](trading-strategy/README.md#chan-py) | Trading Strategy | 50 | 100% | `◐··●◐○····` | ✅ 320 根合成日线上批处理与逐根 trigger_step 都得到 276 根合并 K 线、25 笔、7 段、2 个中枢、14 个买卖点并成功绘图；真实行情与策略收益未测。 |
| [trump-code](trading-strategy/README.md#trump-code) | Trading Strategy | 50 | 100% | `◐○●·●◐◐··●` | 🟡 历史 564 条已验证预测中 346 条正确，61.3% 可复算；最新帖停在 2026-03-25 而日报写 09-26，模型榜单为空，文章索引 404。 |
| [Chancode](trading-strategy/README.md#chancode) | Trading Strategy | 43 | 100% | `◐·◐◐●●··◐◐` | 🟡 7 根合成蜡烛的单次 replay 跑通（账户 10,000→约 10,201），前端 14 路由构建成功；README 的批量回放在干净 clone 因缺 check_out_param 与 D:/ 写死路径不可复现，后端、AI、行情均未运行。 |
| [FMZ strategies](trading-strategy/README.md#strategies) | Trading Strategy | 40 | 100% | `···◐◐○····` | 🟡 5,806 篇 Markdown 全部含非空代码块、3 个 FMZ 原页 HTTP 200 可开；但无统一安装、运行器或回测，本地没有执行任何一条策略，Python 抽查 5 篇中 1 篇（R-Breaker）是 Python 2 语法。 |
| [Meme Radar](trading-strategy/README.md#meme-radar) | Trading Strategy | 23 | 30% | `◐··◐◐○···●` | ⬜ 安装、doctor 与 360 项测试通过，本地 UI 在 127.0.0.1:3981 启动；无 AVE key 时 /health 返回 ready=false、AVE_AUTH_REQUIRED，候选数 0，核心扫描未验证。 |
| [WyckoffTradingAgent](trading-strategy/README.md#wyckofftradingagent) | Trading Strategy | 8 | 15% | `◐··◐◐○···●` | 🟡 无 API key 时本地 Dashboard 8 个页面与合成记录 CRUD 可用（DELETE /api/recommendations/DEMO001 返回 200，2 条变 1 条）；Wyckoff 分析、AI 选股、实时行情与云同步未验证。 |
| [one-quant-doc](trading-strategy/README.md#one-quant-doc) | Trading Strategy | 0 | 0% | `···○○○····` | ⬜ 仓库只有文档与空的 __init__.py，无可安装代码；托管站 one-quant.com/#/zen 在 Chromium、Chrome 通道与真实浏览器三种方式下均跳转 /oops 安全拦截，未绕过。 |
| [standard-broker](trading-infra/README.md#standard-broker) | Trading Infra | 75 | 100% | `◐······◐◐·` | 🟡 六个 canonical port、Paper preflight 与 capability-gap 阻断在本地实测成立；InMemory fixture 只返回 accepted 回执，不撮合、不成交、不改余额。 |
| [vectorbt](trading-infra/README.md#vectorbt) | Trading Infra | 67 | 100% | `···●●●○○○○` | 🟡 两资产各 1,200 根合成小时线经 Portfolio.from_signals 得到 33 条交易记录、完整统计与 Plotly 图；但按声明依赖新装解析到 Plotly 7.1.0 时 import vectorbt 失败，锁到 6.3.0 才可用。 |
| [NautilusTrader](trading-infra/README.md#nautilus-trader) | Trading Infra | 53 | 85% | `◐·◐●●●◐◐◐○` | 🟡 本地 SIM 回测跑通：官方 10,000 bar quickstart 退出码 0，自建 4,000 bar EMA 回测产出 65 个仓位、130 笔模拟成交；实盘一侧的券商适配器、Testnet/Live 与费用/滑点模型未测。 |
| [CCXT](trading-infra/README.md#ccxt) | Trading Infra | 31 | 62% | `◐●·····○◐○` | 🟡 104 个交易所适配器可枚举，Binance 的 fetch_ticker/fetch_order_book/fetch_ohlcv 在进程内 fixture 下统一解析通过；0 次网络请求、0 次下单，真实交易所路径未验。 |
| [OctoBot](trading-infra/README.md#octobot) | Trading Infra | 10 | 40% | `◐○○○◐◐○○◐◐` | ❌ 3.0.0-beta2 安装与 CLI 可用，但干净的 simulator 启动因官方 tentacles 包缺少 .signature（HTTP 404）被拒绝安装，默认 profile 缺失，Web UI 未启动，任何交易流程都没跑通。 |
| [A Share Heatmap](dashboard/README.md#a-share-heatmap) | Dashboard | 83 | 100% | `●·○······●` | ✅ 隔离运行下全市场 5,917 只股票按 32 个板块成图，九种市场范围、日/周/月/年、板块与涨跌筛选、自选增删、主题与分享预览全部实测可用；行情快照止于 2026-09-24。 |
| [Gloomberb](dashboard/README.md#gloomberb) | Dashboard | 73 | 100% | `●··●·····●` | ✅ 隔离环境无 key 取到 AAPL 延时报价，TUI 可进入主界面，产品自带 shot 命令生成的 15 个研究 pane 中 14 个完整可用；仅 Portfolio Analytics pane 没显示手工建立的 EVAL-ONLY 组合。 |
| [standard-kline](dashboard/README.md#standard-kline) | Dashboard | 73 | 100% | `···●·····●` | ✅ 21/21 单测通过；隔离浏览器 harness 用 Lightweight Charts 5.2.0 渲染 400 根 synthetic OHLCV、EMA20/50/200、MACD、marker，空、加载、坏行、缺库状态与缩放平移全部按组件声明工作。 |
| [Vibe AStock](dashboard/README.md#vibe-astock) | Dashboard | 73 | 100% | `●◐◐●●●○○○●` | 🟡 不接 AI 时盘面、梯队、个股研究、自选和日线回测引擎都跑通，时效基本标注清楚；但两处把 9 月 30 日数据标成休市日 10 月 3 日，复盘、辩论等深度功能必须接入 AI。 |
| [Human K-line Review](dashboard/README.md#human-kline-review) | Dashboard | 65 | 100% | `◐··●·····●` | 🟡 在 400 根 synthetic SPY fixture 上完成周线、日线标注，显式跳过缺失的 4H，确认 Asset Review，用本地 mock 确认汇总后三种导出返回 200；真实 Macro Source 与 DeepSeek 未接，且复现了 autosave/complete 竞态。 |
| [Trading Desk](dashboard/README.md#trading-desk) | Dashboard | 40 | 80% | `·········●` | 🟡 /desk、/trade 页面与 health/assets 只读 API 均 HTTP 200，Overview、System、订单、持仓、成交、复盘、Supervisor 面板可浏览；市场 read model 为 blocked、0 bars，看不到任何行情、持仓或订单结果。 |
| [OpenStock](dashboard/README.md#openstock) | Dashboard | 30 | 80% | `●········●` | 🟡 公开首页显示 NYSE 市场状态与指数行情预览，数据说明与注册校验可用；/dashboard 与 /stocks/SPY 匿名访问被重定向到登录，追踪、提醒、公司详情三项核心声称本轮都没验到。 |
| [tick-stock-panel](full-trading-system/README.md#tick-stock-panel) | Full Trading System / Agent | 70 | 100% | `●●●●●●◐○◐●` | 🟡 选股与回测按声明跑通（65 只、114 笔），监控页面可用但 None 数据模式下无实时行情，LLM 能力未配置。 |
| [KHunter](full-trading-system/README.md#khunter) | Full Trading System / Agent | 63 | 100% | `●○●◐●●◐○◐◐` | 🟡 真实数据、选股与回测都能在原生 Web 里跑，但样本只有 3 个标的、回测 0 笔交易，PTrade 交易闭环未验。 |
| [easy-stock](full-trading-system/README.md#easy-stock) | Full Trading System / Agent | 50 | 100% | `●◐●●●◐○○○●` | 🟡 不接 AI 的量化速览、风控仓位建议、连板和指数页都跑通且数字与独立来源一致；AI 分析、持仓巡检和大 V 复盘因无模型与登录未验证，没有回测入口和下单路径。 |
| [finance-quant-skills](full-trading-system/README.md#finance-quant-skills) | Full Trading System / Agent | 50 | 100% | `●○○○◐●○○◐○` | 🟡 13 项技能隔离安装，BaoStock 与 Backtrader 两项按声明跑通，其余 11 项只盘点未运行。 |
| [daily_stock_analysis](full-trading-system/README.md#daily-stock-analysis) | Full Trading System / Agent | 38 | 100% | `●○●○◐◐○○○◐` | 🟡 数据降级路径拿到 600519 真实日线，但核心 AI 报告与推送未配置未验证，dry-run 进程不退出。 |
| [QuantDinger](full-trading-system/README.md#quantdinger) | Full Trading System / Agent | 38 | 75% | `◐○◐◐◐◐●○◐◐` | 🟡 产品化界面完整、策略可生成验证并保存，但回测被日期选择问题挡住未提交，paper/live 未验。 |
| [trading-system](full-trading-system/README.md#trading-system) | Full Trading System / Agent | 38 | 75% | `◐◐◐○◐○◐◐◐●` | 🟡 Dashboard、Desk 与 /trade 代理本地可开，预部署闸门 pass，88 个聚焦测试通过；但行情 read-model 为 blocked、bar_count=0，系统保持 Paper/stopped，没有跑通一次 paper 闭环。 |
| [Vibe-Trading](full-trading-system/README.md#vibe-trading) | Full Trading System / Agent | 38 | 75% | `◐○○◐◐◐◐○◐◐` | 🟡 结构完整、API 与主要页面可用，但缺模型与券商配置，研究、回测、订单三条核心路径都没有产出。 |
| [Sequoia-X](full-trading-system/README.md#sequoia-x) | Full Trading System / Agent | 30 | 85% | `●○○●●○○○○◐` | 🟡 选股扫描按声明跑通并命中 000333，但收盘后自动运行与飞书推送未验证。 |
| [finhack](full-trading-system/README.md#finhack) | Full Trading System / Agent | 23 | 85% | `◐○◐◐◐◐○○◐○` | ❌ CLI 帮助与项目初始化可用，但因子、回测、交易三条关键命令全部失败，没有拿到任何回测结果。 |
| [TradingAgents](full-trading-system/README.md#tradingagents) | Full Trading System / Agent | 21 | 100% | `◐··◐◐○·○○○` | ❌ CLI、12 节点图构建与本地模型工具调用可用，但一次完整分析都没跑完（240 秒超时、无最终评级）。 |
| [go-stock](full-trading-system/README.md#go-stock) | Full Trading System / Agent | 20 | 65% | `●○◐◐◐○○○○◐` | 🟡 原生 macOS 应用启动、自选股与日 K 可用，AI 分析被 VIP2 会员门槛挡住，AI 完整输出未验证。 |
| [Vibe-Research](full-trading-system/README.md#vibe-research) | Full Trading System / Agent | 20 | 65% | `◐○○○◐◐○○○◐` | 🟡 本地原生界面与主要页面能打开，但 AI 未接入，没有产出任何可核验的研究结论。 |
| [Kronos](full-trading-system/README.md#kronos) | Full Trading System / Agent | 19 | 100% | `···●○○····` | 🟡 Kronos-mini 在 CPU 与 MPS 各生成 120 个预测点，但 Web 日期轴 117/120 点与交易日错位，预测质量未与基线比较。 |
| [TradeGenuis-Options](full-trading-system/README.md#tradegenuis-options) | Full Trading System / Agent | 8 | 65% | `●○○○◐○○○○◐` | 🟡 Electron 能浏览素材、20 个 watchlist 项与 6 个机会，但 AI 分析与检索未配置，4 页素材拒收且更新出现冲突。 |
| [fomomo](full-trading-system/README.md#fomomo) | Full Trading System / Agent | 0 | 0% | `◐○○○◐○○○○○` | ⬜ 本轮只看到明确标注的模拟群消息与价格适配页，原生流程、真实群、行情与钱包都没有接入。 |
| [Day1Global Skills](equity-research/2026-09-28/03-day1global-skills/findings.md) | Knowledge & Collections | — | — | `●··●◐○····` | 🟡 5 个 .skill 包与源码逐字节一致，BTC 评分 API 返回 41.3 且按权重复算一致；但文档写 13 指标、API 实为 14，情绪 Skill 把 0 个过热警告映射成 Panic，本轮未生成任何新研报。 |

## 原始证据轮次

- [evaluations/dashboard/2026-09-28](dashboard/2026-09-28/README.md)
- [evaluations/dashboard/2026-10-04](dashboard/2026-10-04/README.md)
- [evaluations/data/2026-09-27](data/2026-09-27/README.md)
- [evaluations/equity-research/2026-09-28](equity-research/2026-09-28/README.md)
- [evaluations/full-trading-system/2026-09-26](full-trading-system/2026-09-26/README.md)
- [evaluations/full-trading-system/2026-10-04](full-trading-system/2026-10-04/README.md)
- [evaluations/trading-infra/2026-09-28](trading-infra/2026-09-28/README.md)
- [evaluations/trading-strategy/2026-09-28](trading-strategy/2026-09-28/README.md)
