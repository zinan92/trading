# TradingView-API · 78/100 · 建议移到 Trading Data

## 角色判断

该仓库是 Node/WebSocket 数据客户端，不是终端或 Dashboard。它把 TradingView chart/quote session、周期、指标与历史回放能力封装为 JS API，适合 Trading Data 下的第三方 WebSocket data adapter。README 明确称其为非官方库。它没有订单、账户持仓管理或独立图形界面。

## 本轮实际验证

- 锁定 commit 5baea86c8c7e576f13464919c86c3b4c4b0ecf4c，安装 npm lockfile 的 326 个包。
- 在 env-i 隔离环境中运行仓库自带 SimpleChart.js 示例，无 SESSION/SIGNATURE。WebSocket 成功加载 BINANCE:BTCEUR 日线，再切换到 BINANCE:ETHEUR、15 分钟和 Heikin Ashi，示例按时关闭 chart/client。
- 完整 Vitest：9 个文件通过、1 个认证文件跳过；50 tests passed、16 skipped。3 个 authenticated account/private-indicator 测试因没有 session cookie 跳过；没有读取或写入用户 cookies。
- 本轮未覆盖 private/invite-only indicators、账户 API、登录、证券标的的完整列表或服务 SLA。一次公开 WS 样例成功不代表该非官方接口持续可用。
- 13 张截图来自锁定版本源代码、文档、示例和测试页；API library 没有原生 UI/dashboard。运行时结果摘要和测试计数见 verification.json。

## 五维评分

| 维度 | 分数 | 证据与限制 |
|---|---:|---|
| 核心结果实测 | 31/35 | 无凭证 WebSocket 取到 daily bars，可切换 15m 和 Heikin Ashi |
| 数据可信度与时效 | 17/25 | 响应实时更新但没有独立来源/完整交易所授权合同；本轮只观察一个公开加密市场样例 |
| 覆盖与深度 | 14/15 | 图表、quote、indicator、回放、区间历史、search 和 quote session API 较广；需要 cookies 的 private 功能未测 |
| 上手与复现 | 9/15 | npm install 与公开图表样例直接；私有指标等能力依赖 SESSION/SIGNATURE |
| 运行稳定性 | 7/10 | 50 tests passed；16 跳过（含认证路径），一次实时公开请求成功 |

## 分类建议

将它从 Dashboard 移至 Trading Data / third-party WebSocket market-data client。若要显示图表，应由 Dashboard/Trading System 消费它的结果；不要因为库示例能建 chart session 就把 SDK 本身描述成完整交易界面。
