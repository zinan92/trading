# WyckoffTradingAgent · 首轮试用记录

## 类内评分：第 6 名 · 69/100

| 核心结果实测 | 数据可信度与时效 | 覆盖与深度 | 上手与复现 | 运行稳定性 | 总分 |
|---:|---:|---:|---:|---:|---:|
| 24/35 | 13/25 | 12/15 | 11/15 | 9/10 | **69/100** |

**建议定位：Wyckoff 研究与候选管理工作台。** 评分依据：无 Key 时本地 UI、历史记录读取及合成候选删除/恢复已实测；AI、实时行情、云同步仍未验证。


**上游：** `YoungCan-Wang/WyckoffTradingAgent` · commit `1819aa74f3e55822681675f7f4c37fb3c9ccd509` · version `0.9.234` · license `AGPL-3.0-only`。

## 无 API 的试用范围

README 所说的本地 Dashboard 可以在没有模型/API key 时启动。我们安装 locked base runtime，并从真实 CLI 入口运行 `wyckoff dashboard --port 8951`。机器上已有服务占用默认 8765，所以测试使用隔离端口。该 Dashboard 的本地 SQLite 重定向到本次 trial 目录，不读取或改写用户的 `~/.wyckoff`。AI 对话、TickFlow 实时/完整数据和云端同步均未调用。

使用仓库 `integrations.local_db` 的真实写入接口在隔离库中放入合成素材：2 条候选、2 条信号、1 个组合/持仓、1 条记忆、1 条后台任务和 1 个明确标为 synthetic 的对话历史。Dashboard 主视图正确显示数量和记录；8 个导航页、深浅主题、语言切换、390px 窄屏视图均打开。首轮 26 个本地 API 请求都返回 HTTP 200，页面无 JS 错误；所有请求只发往 `127.0.0.1:8951`。

额外操作候选页删除 `DEMO001`：本地 `DELETE /api/recommendations/DEMO001` 返回 `200 {ok:true, deleted:1}`，列表从 2 条变为 1 条。之后通过同一产品存储接口恢复了演示行。此操作只改动 trial SQLite；合成值也明确标在名称和结果中。

## 结论

在没有 API key 的条件下，**本地 Dashboard 的只读浏览、本地历史数据展示和候选删除路径可用**；空模型状态清楚可见。AI 分析、实时/完整市场数据、云同步未验证。Dashboard 没有把模拟数据错误呈现成真实推荐，但 portfolio 标识固定显示 `USER_LIVE`，浏览截图必须结合页面中的 `【合成演示数据】`标识理解。

**定位建议：** `Trading Strategy / Wyckoff 研究与策略工作台（CLI + MCP + 本地 Dashboard）`。它的本地产品外壳与知识/策略能力较完整，但主要 AI/行情链路依赖外部服务；无 API 时仍能作为本地历史数据浏览和记录管理面板。不是只有策略代码的静态库。

本产品比 `fmzquant/strategies` 多出可实际启动的工作流、状态存储和本地界面；最终评分与类内排序等本类全项结束后再给。

证据：[本地 Dashboard 截图图库](evidence/index.html) · [操作结果与本地 API 状态](evidence/screenshots/pages.json) · [候选删除与恢复回执](evidence/local-write-probe.json) · [截图清单](screenshots.md)。
