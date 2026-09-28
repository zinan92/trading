# fmzquant/strategies · 首轮试用记录

## 类内评分：第 7 名 · 60/100

| 核心结果实测 | 数据可信度与时效 | 覆盖与深度 | 上手与复现 | 运行稳定性 | 总分 |
|---:|---:|---:|---:|---:|---:|
| 20/35 | 10/25 | 14/15 | 9/15 | 7/10 | **60/100** |

**建议定位：多语言策略源码参考库。** 评分依据：规模与跨语言覆盖大，但没有统一包、运行器或回测；抽查暴露 Python 2 语法失败，授权与策略质量需逐篇确认。


**结论：** 这是一个很大的策略源码和说明集合，不能当成可直接启动的策略系统。本地 clone 在只读隔离下浏览；该项目没有 standalone server、包管理配置或回测入口，因此没有可部署的应用进程。截图覆盖 README、19 个代表策略文件和 2 个 FMZ 原始页面，共 20 张不同画面。

- 上游版本：`7853bb2bf262c4567ac238d3552d97f0e50cb801`；最近提交时间为 2025-04-30。
- 目录规模：5,806 份 Markdown；README 列出 5,810 个 FMZ 原始策略链接。源码说明以 PineScript 为主（5,283），另有 JavaScript（362）、Python（131）、MyLanguage（27）和 C++（3）。本轮检查的 5,806 个文档都有非空代码块。
- 索引缺口：4 个 README 外链没有对应本地文档；另有 1 个本地文件的 FMZ source ID 没出现在 README。README 里的条目基本都指向 fmz.com 原页，没有指向本地 Markdown 文件。
- 三个抽查的 FMZ 原始页均 HTTP 200，证明公开源页可打开。原页中附的回测曲线和收益并非本轮重跑所得。
- Python 静态语法抽查：5 个示例中 4 个按 Python 3 语法解析通过，R-Breaker 样例因 Python 2 式 `except` 语法失败；未执行任何会连接交易所或下单的策略。
- Pine 20 EMA 样例的文档说清策略方向、震荡风险与无止损，但代码默认 100% 仓位。其胜率计数器控制流静态看起来无法在普通开/平仓后递增。这只是代码静态判断；本机未安装 TradingView/FMz 的 Pine 执行环境，没有声称回测通过。
- 仓库根目录没有 LICENSE 文件，单个上游代码片段里的许可证不等于整个翻译集合拥有统一许可。

**建议定位：** `Trading Strategy / Strategy Library`，用于查找跨策略、指标和语言的参考源码；不负责数据、参数验证、统一回测或实盘执行。

完整统计见 [`evidence/probes.json`](evidence/probes.json)，Python 语法抽查见 [`evidence/python-syntax-probes.json`](evidence/python-syntax-probes.json)，20 EMA 静态审查见 [`evidence/sample-code-static-review.json`](evidence/sample-code-static-review.json)。[20 张截图](screenshots.md) · [截图图库](evidence/index.html)。
