# tvscreener · 73/100 · 建议移到 Trading Data

## 角色判断

主体产品是 Python 客户端：向 TradingView 的非官方公开 screener 端点请求股票、加密、外汇、债券、期货和 Coin/DEX 数据，再转为 DataFrame。仓库附带的静态 Code Generator 能在浏览器里构造查询并生成 Python 代码，但没有仪表盘式行情工作区。因此建议从 Dashboard 移到 Trading Data，标注为“第三方公开 screener client”，而不是独立市场数据源。

## 本轮实际验证

- 锁定 commit 737c9764c1e58f364972a9106108b77e9fc1d6c0；在隔离 Python 3.13 环境安装 0.4.1 非 editable wheel，依赖检查通过。
- 运行离线单元测试：129 passed，另报告 2 个子测试通过。
- 本地启动仓库自带静态 Code Generator。切换 Stock、Crypto、Forex、Bond、Futures、Coin 六种类型；添加 Price > 50、RSI > 60、市值区间、S&P 500 index、输出字段、排序与行数；生成的 StockScreen 查询代码可以构造成有效请求配置。
- 使用无凭证的 StockScreener 发起一次只读公开查询：S&P 500、Price > 50、limit 10，约 0.74 秒返回 10 行，列包含 Symbol、Name、Price、Change %、Volume、Update Mode。只验证了美股股票路径，其他五类没有各自实取数据。
- Valuation 字段预设生成 PE_RATIO_TTM、PRICE_TO_BOOK_FY、PRICE_TO_SALES_FY 及 EV_TO_EBITDA_TTM，但已安装版本的 StockField 没有 EV_TO_EBITDA_TTM；照生成代码执行会在请求前报 AttributeError。这是本轮明确复现的代码生成缺陷。
- README 声明项目为 TradingView 非官方库；本轮没有用户账号、API key 或授权账户，也未测试真实持续行情/刷新时效。

## 五维评分

| 维度 | 分数 | 证据与限制 |
|---|---:|---|
| 核心结果实测 | 27/35 | 一次真实无凭证股票筛选成功；本地 UI 构建多条件查询，但不是 Dashboard |
| 数据可信度与时效 | 17/25 | 数据响应来自公开 TradingView screener；只测一类，未给独立来源链与可靠新鲜度合同 |
| 覆盖与深度 | 14/15 | 六类 screener、搜索字段、过滤、index、排序与 DataFrame；只对美股 stock 实取 |
| 上手与复现 | 9/15 | pip 和代码生成容易开始；后端依赖非官方端点与其可用性/条款边界 |
| 运行稳定性 | 6/10 | 129 单元测试通过；Valuation preset 存在生成代码与包导出不一致 |

## 建议

将仓库从 Dashboard 移到 Trading Data。保留代码生成器作为查询工具；修复 preset 中缺失的 StockField 名称，并补一项“所有 preset 生成代码在同版本包中可 import/build”的离线测试。正式使用时应自行核查 TradingView 对公开 screener 的使用规则和数据再分发边界。
