# NautilusTrader · Trading Infra 首轮试用记录

## Trading Infra 类内评分：第 1 名 · 83/100

| 核心结果实测 | 数据可信度与时效 | 覆盖与深度 | 上手与复现 | 运行稳定性 | 总分 |
|---:|---:|---:|---:|---:|---:|
| 33/35 | 14/25 | 15/15 | 13/15 | 8/10 | **83/100** |

**评分依据：** official quickstart and custom local backtest both completed with deterministic synthetic inputs; RC release and no real provider/account kept the data/runtime components below full.


**建议定位：事件驱动的 Rust/Python 回测与交易执行引擎库。**它提供模拟 venue、策略生命周期、行情处理和订单/持仓模型；自身不是带完整行情、风控策略和用户 Dashboard 的交易产品。Trading Infra 六项全测完后再统一打分和排序。

## 部署与试用

按 catalog 锁定的上游 SHA `23cb3035dff7f3fb28b7f5985a2340b090c3c126` 读取其 `python/pyproject.toml`，版本为 `2.0.0rc5`。在 Python 3.13 arm64 的隔离环境安装了匹配的预编译发行 wheel；本机没有 Cargo/Rust，因此没有从 Git SHA 编译。导入 Rust 核心成功。

实际运行了锁定提交自带 `docs/getting_started/quickstart.py`：10,000 根合成 EUR/USD 1 分钟 bar，无下载，退出码 0，用时约 151 秒。另用 `BacktestEngine` 对 4,000 根确定性合成 bar 跑 EMA(10/20) 策略，SIM venue 结束后生成账户、持仓和成交报告：65 个已平仓 position、130 笔模拟 fill。独立评测 harness 展示最终 balance 1,021,464 USD；此样例没有显式费用/滑点模型，且输入是人为构造的正弦行情，只能证明事件回放与报告链路可用，不能评价收益。

## 安装与功能边界

官方安装资料要求 NautilusTrader 2.x 用 `--pre` 安装（1.x 与 2.x API 不兼容），仓库锁定版本当前是 Beta/RC；本机 wheel 安装可用。使用真实 vendor 数据需另行导入数据、建立 catalog；本轮使用合成价格，没连接 Broker、账户、交易密钥、Testnet 或 Live。没有运行全量仓库测试套件。

截图 01–15 为锁定 commit 的 GitHub 源码/项目文件，16–18 为官方当前安装与回测文档，19–22 为实际 BacktestEngine 输出的辅助评测页面（不是产品自带 UI）。

[22 张截图](screenshots.md) · [机器可读验证摘要](verification.json)
