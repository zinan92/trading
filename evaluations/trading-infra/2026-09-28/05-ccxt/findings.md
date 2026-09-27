# CCXT · Trading Infra 首轮试用记录

## Trading Infra 类内评分：第 4 名 · 68/100

| 核心结果实测 | 数据可信度与时效 | 覆盖与深度 | 上手与复现 | 运行稳定性 | 总分 |
|---:|---:|---:|---:|---:|---:|
| 22/35 | 9/25 | 15/15 | 14/15 | 8/10 | **68/100** |

**评分依据：** 104 adapter IDs and mocked ticker/order-book/OHLCV normalization work; no exchange network, freshness, auth or order path was exercised.


**建议定位：多交易所统一 API/数据与订单适配库（Python/JavaScript 多语言）；不是完整交易系统或行情终端。** Trading Infra 全类完成后再评分排序。

## 隔离安装与本地试用

按 catalog 锁定 commit `c781a2437d88b9b983de1eb7b3c6c0e0f86f0e03` 的 `ccxt==4.5.78` 在 Python 3.13 隔离 venv 安装，`uv pip check` 通过。实例可列出 104 个交易所适配器；在没有 API key 的条件下，Binance 实例可声明 `fetchTicker`、`fetchOrderBook`、`fetchOHLCV` 和 `createOrder` 能力。缺密钥时私有凭据预检返回 `AuthenticationError`。

没有请求任何交易所。为了验证解析和统一数据结构，我先安装 fixture market，再把 CCXT 实例自己的 `request` 替换为进程内测试函数；调用真实库的 `fetch_ticker`、`fetch_order_book` 和 `fetch_ohlcv`，分别解析出 last/bid/ask、订单簿和两根合成 K 线。产生的 HTTP 请求数为 **0**，下单调用数为 **0**。这证明 adapter 请求组装后的 parse/normalization 链路，不证明真实网络、市场新鲜度、限流、各交易所兼容性或成交。

## 边界与定位

CCXT 自身没有原生 Dashboard。本轮源码/文档截图来自锁定提交，结果截图来自 mocked public response 和辅助评测页。`createOrder=True` 只是能力元数据，本轮从未调用；没有连接账户、密钥、Testnet 或 Live。用户自行提供数据与密钥后，仍需逐个 Broker 验证市场映射、限额、精度、手续费、签名和错误处理。

建议留在 Trading Infra / 多交易所 Broker API adapter；如果后续目录只放策略研究工具，则应迁到 Broker/Data integration，而非 Trading Strategy。

[11 张截图](screenshots.md) · [fixture 回执](results/mock-api-probe.json)
