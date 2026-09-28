# A Share Heatmap · not ranked

**Repository:** `wenyuanw/a-share-heatmap`

**Evidence:** 24 screenshots.

## First-round result

原生热力图、9 种市场范围、日/周/月/年视图、过滤、主题和自选操作通过；数据快照止于 2026-09-24。推荐移到 Dashboard，暂不纳入本类排名。

## Detailed findings

# a-share-heatmap · Equity Research 类第 2 个首轮试用

- 上游：[`wenyuanw/a-share-heatmap`](https://github.com/wenyuanw/a-share-heatmap)，源码 `6b4b6744ad16f44fcf1cff17d8813af29aad66f0`、Next.js 16.3.3。隔离 checkout 运行 `pnpm install --frozen-lockfile` 和本机 `127.0.0.1:3001` Next dev；试后停止。
- **定位建议：A 股市场可视化 Dashboard／市场概览组件**，更适合 Trading 的 Dashboard 类，不是以个股财报、估值、研究报告为核心的 Equity Research。原目录仍保留本轮样本，类内统一排序时标清定位差异。
- 证据：本轮 13 个 API 场景摘要 保存 13 个原生 HTTP API 场景；页面 Site tools 场景核对结果 保存页面 Site tools 的排行与最终状态；[截图清单](screenshots.md) 有 **24 张不同原生 UI 截图**，包括九种市场范围、四种涨跌周期、板块/涨跌/涨幅筛选、成交额面积与缩略图、个人自选增删、主题和截图预览。

真实数据和交互：`/api/heatmap/treemap?market=all&period=day` 返回 5,917 只股票、32 个板块；源标 `direct`、行情时间 **2026-09-24 15:30/16:15 中国时区**（本轮为休市周末，不把 9 月 27 日打开页面说成新交易数据）。上证、深证分别 2,467／3,093；沪深 300 精确 300、中证 A50 精确 50，A500 为 500。热力图色块可视化清晰，近 5 日、近 20 日和年内模式均有独立结果。接口对非法 period 返回 HTTP 400。

Site tools 实际可用：`get_heatmap_state` 返回当前市场、周期、筛选、来源和时间；`set_heatmap_view`、`set_heatmap_filters` 真的改变原生页面；搜索“贵州茅台”命中 `600519.SH`，加入本地自选后读取报价 **1237 元**、涨幅 -1.14%，自选视图只有该股票；移除后数量归零。股票和板块排行各返回 10 条。内置柔和主题和自定义配色都可创建/应用。截图分享成功生成可见的 PNG 预览；内置浏览器没有观察到下载事件，所以“下载图片保存到本机”**未单独确认**。

边界：源为网站聚合的市场快照，非交易所直连或券商账户；数据许可与盘中真实时延未在休市日验证。页面核心任务是看市场宽度、板块涨跌和权重结构，缺少针对单家公司完整的财务、估值和研究结论。当前日期和实际行情日分开显示是必要的；本轮页面和 API 已提供来源与 `updatedAt` 字段。Equity Research 类全部测完后再统一评分。
