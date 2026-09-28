# Trading · Trading Strategy 首轮试用、排序与定位

**首轮实测，不是盈利评级或生产认证。** 本页比较 Trading Strategy 及经前一类测试后建议迁入的 Qlib。评分看各工具能否完成自己声明的核心任务、输入/来源是否可信、角色覆盖、安装复现和运行稳定；不等于“完整交易系统”程度。评分细则：[methodology.md](methodology.md)。

本轮按原目录依次试了 9 个条目，每个至少 12 张不同截图。8 个可定位产品参与评分，one-quant-doc 本身是文档仓库、托管站被浏览器安全页挡住，无法评价 hosted app，因此记 N/A。Qlib 在 Equity Research 实测后建议迁入本类，纳入比较但不计入原目录 9 项。合计留存 **159 张独特截图**。

## 排序

| 排名 | 产品 | 分数 | 建议定位 | 本轮结论 | 截图与证据 |
|---:|---|---:|---|---|---|
| 1 | [TA-Lib](https://github.com/TA-Lib/ta-lib-python) | **84** | 技术指标计算库（Python+C） | 201 个指标、NumPy/Pandas/Polars 与 80 项测试可用；实验性 streaming 的 EMA/RSI/MACD/ATR/ADX 与批量结果不一致。 | [判断与分项](09-ta-lib/findings.md) · [20 张截图](09-ta-lib/screenshots.md) |
| 2 | [chan.py](https://github.com/Vespa314/chan.py) | **78** | 缠论结构分析与策略开发引擎 | 320 根合成 OHLC 的批量与逐根结构结果一致；真实行情、策略收益与交易连接未测。 | [判断与分项](04-chan-py/findings.md) · [13 张截图](04-chan-py/screenshots.md) |
| 3 | [zinan92/trading-strategy](https://github.com/zinan92/trading-strategy) | **76** | DCA/Grid 计划与离线回放组件 | 安装和 12 个确定性场景可跑；纯核心测试 38 通过。仓库已归档并迁入 trading-system，不建议把旧库当独立应用。 | [判断与分项](06-zinan92-trading-strategy/findings.md) · [12 张截图](06-zinan92-trading-strategy/screenshots.md) |
| 4 | [CZSC](https://github.com/waditu/czsc) | **73** | 缠论分析、信号和研究回测 CLI/库 | mock→分析→研究→回测→HTML 图表链路可用；BI 固定基准 3 项失败，1.0.1 wheel 实际 31 笔而仓库基准为 43。 | [判断与分项](08-czsc/findings.md) · [18 张截图](08-czsc/screenshots.md) |
| 5 | [Qlib](https://github.com/microsoft/qlib) · 建议从 Equity Research 迁入 | **70** | 离线量化研究、特征与模型训练引擎 | 训练与 2,094 条样本外预测可复现；数据止于 2021-06-11，组合回测未验证。 | [判断与分项](10-qlib/findings.md) · [12 张截图](10-qlib/screenshots.md) |
| 6 | [WyckoffTradingAgent](https://github.com/YoungCan-Wang/WyckoffTradingAgent) | **69** | Wyckoff 研究与候选管理工作台 | 无 API 本地界面与合成记录 CRUD 可用；AI、真实行情与云同步没有验证。 | [判断与分项](02-wyckoff-trading-agent/findings.md) · [13 张截图](02-wyckoff-trading-agent/screenshots.md) |
| 7 | [fmzquant/strategies](https://github.com/fmzquant/strategies) | **60** | 多语言策略源码参考库 | 5,806 篇源码文档可浏览；没有统一安装、搜索/回测运行器，未验证盈利。根目录缺统一 LICENSE。 | [判断与分项](01-fmzquant-strategies/findings.md) · [20 张截图](01-fmzquant-strategies/screenshots.md) |
| 8 | [Meme Radar](https://github.com/nhovongoc0-max/meme-radar) | **58** | 多链 Meme 候选发现与风险复核工具 | 安装、doctor 与 360 项测试通过；无 AVE Key 时核心扫描明确不可用，本轮没有真实候选结果。 | [判断与分项](03-meme-radar/findings.md) · [12 张截图](03-meme-radar/screenshots.md) |
| 9 | [Chancode](https://github.com/zinan92/chancode) | **45** | Chan 信号 Paper/AI 策略系统候选 | 前端能构建、单次合成回放可跑；干净 clone 的批量回放缺模块/行情路径，API 依赖页有客户端错误，后端离线。 | [判断与分项](07-chancode/findings.md) · [23 张截图](07-chancode/screenshots.md) |

每项五维分数见各自判断页；同一分值是证据强弱与该产品建议角色内的首轮结果，不代表能替代另一类工具。

## 分类建议

| 原目录条目 | 建议定位 | 处理建议 |
|---|---|---|
| fmzquant/strategies | Trading Strategy / 多语言策略源码参考库 | 保留为参考材料，不标成可部署/可回测策略系统。 |
| WyckoffTradingAgent | Trading Strategy / Wyckoff 研究工作台 | 保留；界面与本地记录可用，AI/行情能力单独标未验。 |
| Meme Radar | Trading Strategy / 信号发现与风险复核 | 保留；加 AVE 授权后才能测核心扫描。 |
| chan.py | Trading Strategy / 缠论结构分析引擎 | 保留；可接研究者自定义策略，非成品交易系统。 |
| one-quant-doc | 仓库本身属 Knowledge & Collections / 产品文档；托管应用若可用则属 Dashboard | 不参与本类分数；hosted site 被浏览器拦截，本轮不可评。Knowledge & Collections 按要求未做进一步测试。 |
| zinan92/trading-strategy | Trading System 内的 DCA/Grid 策略组件 | 旧仓库已归档迁入 `trading-system/packages/trading-strategy`，消费迁移后的包，不重复维护旧入口。 |
| Chancode | Trading Strategy / Chan + Paper + AI 策略系统候选 | 可保留候选身份；修复干净环境回放依赖与 API 缺页后再评生产就绪。 |
| CZSC | Trading Strategy / 缠论分析、信号及研究回测 CLI/库 | 保留；先澄清 Rust checkout 与 wheel 的 BI 基准漂移。 |
| TA-Lib | Trading Strategy / Technical Indicators 底层库 | 保留作指标计算依赖；实时使用 stream 递归指标前先和批量 API 对账。 |
| Qlib（迁入候选） | Trading Strategy / 离线量化研究与训练引擎 | 建议从 Equity Research 调到此类；先刷新数据，再补 SimulatorExecutor/交易成本回测证据。 |

## 我会先用哪些

如果要搭研究/策略组件，先看 **TA-Lib**（通用指标计算）和 **chan.py/CZSC**（缠论结构）。如果要研究 ML/横截面模型，Qlib 的训练和预测管线较完整，但它自带的数据很旧，本轮没有验证组合回测。DCA/Grid 包的计算逻辑清晰，却已归档迁入 trading-system。

若想无 API 直接体验可见工作台，WyckoffTradingAgent 的本地历史浏览和候选管理已可用；它的 AI/实时数据不在本轮通过范围。Meme Radar 缺 AVE key 时没有扫描结果。Chancode 当前不能按 README 在干净 clone 完整复现。

**成熟度判断：** TA-Lib 在“基础计算库”角色最成熟（80 项仓库测试通过，但 streaming 递归指标有实测差异）；chan.py 在“缠论结构引擎”上证据扎实；DCA/Grid 是成熟度较好的窄组件但旧库已归档。没有一个产品在本轮被证明为完整、可直接接真实市场数据并安全执行交易的策略系统。

本轮没有任何真实账户、交易密钥、下单或真实收益验证。所有模拟行情和净值结果仅用于检查软件流程。
