# Human K-line Review · 76/100 · Dashboard

## 角色判断

建议留在 Dashboard，精确定位为人工宏观 K 线复盘工作台。它以人工分析为先，读取 Macro Source 并保留来源、新鲜度与周期状态；它没有下单、持仓管理或交易执行闭环，不属于 Full Trading System。AI 只做人工记录的派生汇总。

## 本轮实际验证

在 127.0.0.1:8933 启动了独立应用实例，Macro Source 指向本地生成的 400 根确定性 synthetic SPY K 线，review SQLite 也放在独立试用目录。没有读取 127.0.0.1:8932 已有会话，没有访问真实 Macro Source，也没有 DeepSeek 凭证或外网 API 请求。

隔离实例中实际完成：查看周线/日线图及来源信息、进入逐根观察、给单根 K 线加时间戳备注、保存周线和日线 Human Analysis、跳过源中明确不存在的 4H 并记录理由、确认 Asset Review、用本地 mock provider 检查 synthesis draft/确认流程。mock provider 仅用于验证产品契约，不代表 DeepSeek 输出质量。

关键缺陷：点击分析标签或编辑文本会设置 700ms 自动保存。若在 debounce 写入完成前点击“完成”，之后触发的保存请求可追加一条空 draft，把已完成周期重新变成 pending。隔离数据库实测到日线 completed 后约 0.66 秒多出空 draft，API 的 next_timeframe 退回 daily；等自动保存结束再完成，才会推进到 four_hour。该行为与本地 static/review_ui.js 中自动保存定时器及 complete() 未取消定时器的实现一致。此 bug 会让快速操作丢失进度。

另一限制：未确认 synthesis 时，JSON/Markdown/HTML 三个导出接口均返回 409 synthesis_unconfirmed，页面也不显示导出链接。因此没有 DeepSeek API 时，纯人工复盘虽可保存和确认，却无法从产品 UI 导出。本轮用 local mock 确认汇总后，三种导出都返回 200；这不验证真实 DeepSeek 连通性或质量。

## 自动化检查

- Python：57 项通过；1 项失败，test_browser_degrades_insufficient_history_without_rendering_chart 在 Playwright 的 networkidle 等待 30 秒超时。实际页面可通过 DOMContentLoaded 加载且功能可操作，失败更像测试等待条件不适配，但本轮不改测试。
- JavaScript：npm run test:js 中 7/7 失败。chart_config 和 indicators 测试读取到的导出函数均为 undefined，错误发生在断言之前。
- 已留存 25 次 UI 截图、21 张唯一画面；画面只含本地合成标识和 EVAL FIXTURE 文字。
- 工作区没有可用 Git commit；以 source-fingerprint.json 的 SHA-256 固定本轮测试的关键源文件。

## 五维评分

| 维度 | 分数 | 证据与限制 |
|---|---:|---|
| 核心结果实测 | 28/35 | 人工标注、周期顺序、跳过缺失数据、确认和导出契约均跑过；导出必须先确认 synthesis |
| 数据可信度与时效 | 21/25 | 来源身份、freshness、缺失状态清楚；本轮只有 synthetic fixture，真实 Macro Source 未核验 |
| 覆盖与深度 | 13/15 | 图表、标准指标、逐根标注、人工多周期复盘、汇总与导出完整 |
| 上手与复现 | 9/15 | HTML 工作台直接可操作；正式启动依赖 Macro Source，AI 汇总需要外部服务凭证 |
| 运行稳定性 | 5/10 | 发现 autosave/complete 竞态；一个 Python browser test 超时，七个 JS 测试全失败 |

## 结论

产品方向清楚，安全边界也尊重 Macro Source 与人工判断的优先级；手工复盘主体流程可在样例数据上运行。先修正 debounce timer 与完成周期之间的竞态，并让无 AI 的纯人工复盘也能导出，再适合用于常规复盘工作。生产源、真实 DeepSeek、部署版本与此无 commit 的本地源码之间尚未做版本对账。
