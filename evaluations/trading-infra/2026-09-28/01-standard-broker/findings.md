# standard-broker · Trading Infra 首轮试用记录

## Trading Infra 类内评分：第 2 名 · 80/100

| 核心结果实测 | 数据可信度与时效 | 覆盖与深度 | 上手与复现 | 运行稳定性 | 总分 |
|---:|---:|---:|---:|---:|---:|
| 29/35 | 21/25 | 10/15 | 12/15 | 8/10 | **80/100** |

**评分依据：** canonical broker contracts with 348 tests passed; narrow runtime domain and external Nautilus cases remain optional/skipped.


**上游入口已归档；本轮测试 `trading-system` 中迁移后的 `packages/standard-broker`。** 定位为 **Trading Infra / canonical broker contract and adapter package**。它是提供 broker-neutral 接口与适配边界的库，不是完整交易系统，也不是第二个交易/匹配引擎。类内评分与排序等 Trading Infra 全部六项完成后统一给出。

## 安装和实际使用

在隔离 Python 3.13 环境中从迁移后的包构建并安装 `standard-broker==0.1.0`。不依赖密钥或外部 Python runtime 即可导入。实际创建 `PaperBrokerAdapter`，核对六个 canonical ports，并调用 local preflight/read：结果标记 `network_io=false`、`real_money_eligible=false`、`credential_required=false`，receipt provenance 为 `paper_fixture/local_fixture`。

同一 fixture 上再发起未授予能力的 `order_execution.submit`，返回 `capability_gap`，transport 调用数保持不变；把身份换成 Testnet 或给 Paper 身份附 signer 都在 adapter construction 时被拒绝。这个过程证明的是 Paper boundary 和 fail-closed capability gate；`InMemoryPaperTransport` 只确认本地请求并返回 accepted receipt，没有撮合、成交、账户余额变化或外部执行。

包级完整测试为 **348 passed, 5 skipped**。跳过的五项依赖可选 `nautilus_trader` extra；它们涉及 Nautilus 集成映射，本轮未安装该 extra。测试目录与 Hyperliquid proof script 没有发现直接 HTTP/Socket 客户端调用模式；proof script 本身未运行。

## 评测边界

产品没有原生 UI 或独立常驻服务。本轮用安装后的 Python API 和项目测试验证，截图 01–18 为锁定提交上的 GitHub package/source/test 页面；截图 19 是实际 fixture 输出的辅助呈现页，明确标记为非原生界面。

本轮没有测试真实行情、券商账户、Testnet 网络、账户密钥、下单、取消或实盘能力。仓库 ADR 将 Testnet 与 Live 作为不同环境，并说明本地 Paper 不是 Testnet。完整测试与 smoke 的摘要见 [verification.json](verification.json)。

[19 张截图](screenshots.md) · [本地 Paper 操作详情](results/paper-smoke.json)（trial 目录）
