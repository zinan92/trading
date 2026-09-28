# Trading · Trading Infra 首轮试用、排序与定位

**首轮实测，不是完整生产认证或盈利评价。** 本类六项已依 catalog 顺序逐一安装/启动/操作或记录阻断；每项至少 11 张独特截图，整体留存 **140 张不同截图**。产品角色差异很大，分数按每个产品自己的声明职责评估，完整评分口径见 [methodology.md](methodology.md)。

## 排序

| 排名 | 产品 | 分数 | 实测角色 | 本轮判断 | 截图与证据 |
|---:|---|---:|---|---|---|
| 1 | [NautilusTrader](https://github.com/nautechsystems/nautilus_trader) | **83** | Rust/Python 事件驱动回测与执行引擎 | 锁定 SHA 对应的 2.0.0rc5 wheel 可用；官方 10,000 bar quickstart 和 4,000 bar 本地 EMA 回测通过，产出 65 个仓位、130 笔模拟 fill。只测 SIM，不代表实盘准备度。 | [判断与分项](02-nautilus-trader/findings.md) · [22 张截图](02-nautilus-trader/screenshots.md) |
| 2 | [trading-system / standard-broker](https://github.com/zinan92/trading-system/tree/main/packages/standard-broker) | **80** | Provider-neutral broker port/adapter 组件 | 348 测试通过、5 项可选 Nautilus 测试跳过；本地 Paper preflight、六个 port、capability-gap 阻断已验。InMemory fixture 不撮合/成交。 | [判断与分项](01-standard-broker/findings.md) · [19 张截图](01-standard-broker/screenshots.md) |
| 3 | [vectorbt](https://github.com/polakowo/vectorbt) | **77** | 向量化组合回测与策略研究引擎 | 两资产合成小时线与 Portfolio API、统计和 Plotly 图成功；默认解析到 Plotly 7.1.0 时 vectorbt 导入失败，锁到声明范围内的 6.3.0 才可用。 | [判断与分项](04-vectorbt/findings.md) · [21 张截图](04-vectorbt/screenshots.md) |
| 4 | [CCXT](https://github.com/ccxt/ccxt) | **68** | 多交易所统一数据/订单 API client 库 | 104 个 exchange IDs；Binance ticker/book/OHLCV 在本地 fixture 响应下统一解析通过。没有访问交易所网络或发单，故 freshness/限流/订单语义未验。 | [判断与分项](05-ccxt/findings.md) · [11 张截图](05-ccxt/screenshots.md) |
| 5 | [trading-system](https://github.com/zinan92/trading-system) | **65** | Paper-first 集成交易平台（Dashboard + Desk） | 本地 UI 与 `/trade` 代理可打开，88 个聚焦测试通过；市场 read-model `blocked`、bar count 0，系统保持 stopped/fail-closed。建议将整体 repo 移入 Full Trading System。 | [判断与分项](03-trading-system/findings.md) · [50 张截图](03-trading-system/screenshots.md) |
| 6 | [OctoBot](https://github.com/Drakkar-Software/OctoBot) | **30** | 独立加密自动交易机器人候选 | 3.0.0-beta2 包和 CLI 可用；首次模拟 UI 因官方 tentacles 包缺少必需签名而拒绝安装，未启动 UI。没有降低签名门或连交易所。 | [判断与分项](06-octobot/findings.md) · [17 张截图](06-octobot/screenshots.md) |

分项表与每一条测得的结果写在各产品页面。分数衡量“首轮证据”，不是跨角色的净值表现。

## 分类建议

| Catalog 项 | 建议位置 | 处理判断 |
|---|---|---|
| `zinan92/standard-broker`（已归档） | Trading Infra / canonical broker adapter package | 当前代码在 `trading-system/packages/standard-broker`；是 provider-neutral 适配边界，不是第二个引擎。 |
| `nautechsystems/nautilus_trader` | Trading Infra / event-driven backtest and execution engine | 保留；它是底层 Rust/Python 引擎。2.0.0rc5 是预发布版本，本轮只验证本地 SIM。 |
| `zinan92/trading-system` | **Full Trading System / Agent** | 这是完整 Paper-first 产品（GridMind + Desk + strategy/broker/kline），Infra 目录不适合承载整个应用；建议主类迁出，组件继续留在各子类。 |
| `polakowo/vectorbt` | **Trading Strategy / vectorized backtesting engine** | 建议从 Infra 移到 Strategy。它主要评估策略和组合，不提供 broker/行情连接产品。依赖兼容问题修复前应锁 Plotly 上限。 |
| `ccxt/ccxt` | Trading Infra / multi-exchange API adapter library | 保留。统一 REST/异步 client；需逐交易所和具体账户/市场类型做有密钥的受控验收后，才能宣称订单路径可用。 |
| `Drakkar-Software/OctoBot` | **Full Trading System / crypto bot candidate** | 建议转 Full Trading System。它有策略、界面和交易自动化定位，但当前 pinned install 的签名插件缺口阻断干净启动，未能实测产品 UI。 |

以上都是分类建议，本轮没有更改 catalog 的 canonical 分组。

## 先用什么

如果要做 event-driven 回测与模拟，NautilusTrader 的核心路径覆盖最好，但目前是 2.0.0rc5，样例耗时约 151 秒；如果是快速扫参数/组合，vectorbt 的计算路径更轻，但 fresh resolver 的 Plotly 7.1.0 会导致 `import vectorbt` 失败，使用兼容 Plotly 6.3.0 后才通过。standard-broker 更适合作为系统内接口契约与适配层，别把本地 fixture receipt 当成 broker fill。CCXT 负责统一请求形态，不替你保证数据新鲜或交易语义。

trading-system 的本地控制 UI 在没有可信行情时显示 unavailable 并阻止新开仓；这是预期的安全状态，但本轮没有完整 Paper 数据链路。OctoBot 的安装和 CLI 已验证，runtime 被 tentacles 签名包阻断。

本轮没有任何真钱、Testnet 下单、账户密钥或真实策略收益验证。OctoBot 拉取的公开软件插件包已在安装前由其官方签名校验拒绝；未关闭该校验。
