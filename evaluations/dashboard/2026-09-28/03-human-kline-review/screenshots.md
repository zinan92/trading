# Human K-line Review screenshots

25 次 UI 截图，21 张唯一画面。所有发布图来自 localhost:8933 的隔离 synthetic fixture；没有截图原有 8932 用户服务，也没有把真实人工笔记写进证据。
- ![隔离合成样例首页与 400 根 K 线](images/01-initial-overview.jpg) — 01-initial-overview.jpg
- ![展开 Macro Source 只读来源、报告截止与状态](images/02-source-provenance-expanded.jpg) — 02-source-provenance-expanded.jpg
- ![切换日线图：合成 OHLC 与标准指标](images/03-daily-chart.jpg) — 03-daily-chart.jpg
- ![切换周线图：EMA20/50/100/200、MACD 与 sRSI](images/04-weekly-chart.jpg) — 04-weekly-chart.jpg
- ![专注模式入口](images/05-focus-mode.jpg) — 05-focus-mode.jpg
- ![创建隔离 SPY Asset Review](images/06-review-created.jpg) — 06-review-created.jpg
- ![逐根观察模式与 K 线日期导航](images/07-focus-candle-observation.jpg) — 07-focus-candle-observation.jpg
- ![添加合成 K 线标注并展示日期关联](images/08-key-candle-marker.jpg) — 08-key-candle-marker.jpg
- ![周线 Human Analysis 草稿与关键标记](images/09-weekly-draft-saved.jpg) — 09-weekly-draft-saved.jpg
- ![周线完成后推进到日线](images/10-weekly-completed.jpg) — 10-weekly-completed.jpg
- ![日线草稿保存状态](images/12-daily-draft-saved.jpg) — 12-daily-draft-saved.jpg
- ![日线完成尝试后状态](images/13-daily-completed.jpg) — 13-daily-completed.jpg
- ![缺失 4H 数据的 fail-closed 状态](images/14-four-hour-unavailable.jpg) — 14-four-hour-unavailable.jpg
- ![700ms 自动保存写入的日线草稿](images/17-daily-autosave-settled.jpg) — 17-daily-autosave-settled.jpg
- ![自动保存稳定后日线推进至 4H](images/18-daily-completed-after-debounce.jpg) — 18-daily-completed-after-debounce.jpg
- ![4H 显式跳过理由表单](images/19-four-hour-skip-form.jpg) — 19-four-hour-skip-form.jpg
- ![含原因的 4H skip receipt](images/20-four-hour-skipped.jpg) — 20-four-hour-skipped.jpg
- ![Asset Review confirmed 状态](images/22-asset-confirmed.jpg) — 22-asset-confirmed.jpg
- ![汇总入口：明确使用本地 mock provider](images/23-summary-entry-mock-enabled.jpg) — 23-summary-entry-mock-enabled.jpg
- ![本地 synthetic summary draft 与证据摘录](images/24-synthetic-summary-draft.jpg) — 24-synthetic-summary-draft.jpg
- ![本地 synthetic summary 确认后出现的导出入口](images/25-synthetic-summary-confirmed.jpg) — 25-synthetic-summary-confirmed.jpg

另有 4 张重复状态截图未重复存储：11-daily-review-open.jpg → 10-weekly-completed.jpg, 15-four-hour-skipped.jpg → 14-four-hour-unavailable.jpg, 16-daily-completion-retry.jpg → 13-daily-completed.jpg, 21-asset-finalization-review.jpg → 20-four-hour-skipped.jpg
