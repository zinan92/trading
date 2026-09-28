# standard-kline screenshots

15 次 harness 截图，其中 14 张是有效产品状态且互不重复；1 张在全局库已加载后才移除，作为无效试验不发布。全部有效图使用隔离 synthetic fixture；没有行情 API。
- ![400 根合成 OHLCV 标准主图与 synthetic 水印](images/01-synthetic-chart.jpg) — 01-synthetic-chart.jpg
- ![EMA20/50/200、MACD、价位线和 K 线标记](images/02-indicators-markers.jpg) — 02-indicators-markers.jpg
- ![图表 zoom in 控件](images/03-zoom-in.jpg) — 03-zoom-in.jpg
- ![图表 pan right 控件](images/04-pan-right.jpg) — 04-pan-right.jpg
- ![Fit 全部数据窗口](images/05-fit-all-bars.jpg) — 05-fit-all-bars.jpg
- ![Auto-fit 当前可见数据](images/06-auto-fit-visible.jpg) — 06-auto-fit-visible.jpg
- ![输入包含坏 OHLC 行；组件保留 120 根有效 bar](images/07-invalid-ohlc-row-dropped.jpg) — 07-invalid-ohlc-row-dropped.jpg
- ![stale 质量标识和合成数据水印](images/08-stale-source.jpg) — 08-stale-source.jpg
- ![blocked 状态仍保留可视历史 bars 并标记 synthetic](images/09-blocked-source.jpg) — 09-blocked-source.jpg
- ![空 bars 的 NO LIVE KLINE DATA 状态](images/10-empty-payload.jpg) — 10-empty-payload.jpg
- ![显式 loading 状态](images/11-loading-source.jpg) — 11-loading-source.jpg
- ![超范围缩放/平移后的数据视窗](images/13-extreme-range-clamped.jpg) — 13-extreme-range-clamped.jpg
- ![缺少 Lightweight Charts 且 synthetic 输入时的告警优先级](images/14-missing-peer-dependency.jpg) — 14-missing-peer-dependency.jpg
- ![缺少 Lightweight Charts 且非 synthetic 输入时的依赖错误态](images/15-missing-library-error-state.jpg) — 15-missing-library-error-state.jpg
