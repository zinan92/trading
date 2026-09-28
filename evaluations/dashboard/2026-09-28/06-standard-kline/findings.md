# standard-kline · 79/100 · reusable chart component

## 角色判断

这是迁入 trading-system/packages/standard-kline 的 provider-neutral 浏览器 K 线组件。它消费统一 OHLCV 与来源元数据，本身不提供行情、Watchlist 或 dashboard shell。建议从 Dashboard catalog 的独立产品位移到 Trading Infra，作为 chart-rendering package；完整用户入口属于 trading-system/Desk。

## 本轮实际验证

- 在锁定 trading-system commit bbdcf9005cbf15860b6a6214a408634925580923 上运行 Node 单测：21 passed、0 failed。
- 使用 Lightweight Charts 5.2.0 和隔离 browser harness 渲染 400 根确定性 synthetic OHLCV；价格蜡烛、成交量、EMA20/50/200、MACD、marker 与价位线均可见，synthetic 水印明确显示非真实价格。
- Zoom、pan、fit、auto-fit 可操作；极端范围保持在数据区间内。输入 121 行（其中 1 行缺少必需 OHLC 字段）后组件保留 120 根有效 bars。
- Empty payload 显示 NO LIVE KLINE DATA；loading 状态显示 LOADING KLINE。stale/blocked payload 若仍带 bars，会继续显示图表并把 quality 状态留在 source metadata；上层系统仍须把不可用行情限制为只读。
- 缺少 Lightweight Charts 时，非 synthetic payload 显示 CHART LIBRARY MISSING。若 payload 同时标记 synthetic，则 synthetic 安全水印占先，依赖缺失错误不再显示；这降低了诊断可见性。
- 本轮所有图表数据都是隔离 synthetic fixture。组件不是数据源，未请求任何交易所或行情 API。

## 五维评分

| 维度 | 分数 | 证据与限制 |
|---|---:|---|
| 核心结果实测 | 28/35 | browser chart、均线/MACD、marker、坏行丢弃和 viewport 控件均通过 fixture smoke |
| 数据可信度与时效 | 20/25 | 规范化保留 provider/source/quality 元数据并显式标识 synthetic；不负责行情来源与时效验证 |
| 覆盖与深度 | 13/15 | 蜡烛/成交量、价位线、标记、EMA/MACD 与受限 zoom/pan/fit |
| 上手与复现 | 11/15 | UMD 和 CommonJS 用法简单，但 Lightweight Charts 是 peer dependency |
| 运行稳定性 | 7/10 | 21 项单测通过；synthetic watermark 会覆盖 peer dependency missing 的诊断态 |

## 结论

作为整套产品里的统一图表模块，功能边界和数据安全提示设计较完整。Dashboard 目录不适合把它当一个单独可用的交易看板评分；真实数据的授权、freshness、bar provenance 和交易准入都由调用它的宿主应用负责。
