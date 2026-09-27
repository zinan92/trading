# one-quant-doc · 首轮试用记录

## 类内结论：N/A（未排名）

| 核心结果 | 数据可信/时效 | 覆盖深度 | 上手复现 | 稳定性 | 总分 |
|---:|---:|---:|---:|---:|---:|
| — | — | — | — | — | N/A |

仓库本身是文档，不是可部署的产品代码；托管页面安全拦截，不能把嵌入的静态图片算作运行结果。建议把仓库归 Knowledge & Collections；只有托管应用可访问后再按 Dashboard 评。Knowledge & Collections 本轮按要求没有进一步测试。


**上游：** `neil-pan-s/one-quant-doc` · commit `7231f5d5353cf118890de7e186f56c5a7727ea41`（2025-08-20）。仓库主要是 README、用户手册、策略脚本编程指南和产品预览图；Python `__init__.py` 是空模块，没有可安装或启动的应用代码。

## 试用结果

- 直接打开 README 指向的 `https://one-quant.com/#/zen`：HTTP 200 后页面自动转到 `/oops`，显示“请使用PC最新版Chrome浏览器访问 / 您的浏览器版本较低或存在安全风险”。Playwright Chromium、Chrome 通道和 Codex In-app Browser 都出现同一拦截。我没有伪装浏览器、绕过门槛或登录。
- 因此 live 图表、标的切换、K 线回放、规则配置和策略脚本执行本轮均不可验证。可见 GitHub README 与 MANUAL 描述沪深、港美股、期货、加密币与多级别笔段分析；这些是文档自述。
- 本轮留下 12 张不同截图：网站拦截状态，以及 README 不同部分/内嵌产品图片。内嵌图片是静态样例，不是本轮 app 运行结果。

## 定位建议

该 GitHub 仓库本身是 **Knowledge & Collections / 壹缠产品说明与脚本 API 文档**。它指向的托管产品若可用，才适合放进 **Dashboard / 托管缠论图表 SaaS**；本轮 live 页面不可达，因此不给该类功能评分，也不纳入 Trading Strategy 的候选排名。

证据：[截图图库](evidence/index.html) · [网站拦截结果](evidence/live-site-access.json) · [截图清单](screenshots.md)。
