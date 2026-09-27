# intel · Data 类首轮试用

- 上游：[`zinan92/intel`](https://github.com/zinan92/intel)，源码 `54bd1b3f8bc0459a4ff166afd9811c28b94f0ffe`。隔离 checkout 内安装 Python 依赖、构建 React 前端，以 `127.0.0.1:8112` 启动自带 FastAPI/调度器并生成独立 SQLite；未调用推送脚本、未配置账号或密钥，试完停机。
- 定位：**新闻/情报采集与事件研究平台**，不是证券 OHLCV 行情库。采集 RSS、Google News、Hacker News、Reddit、Yahoo 等来源，提供检索、关键词标签、可选评分及事件聚合。
- 证据：[`evidence/probes.json`](evidence/probes.json) 包含 12 个原生 API 场景及 SQLite 发布时间/采集时间审计，逐项响应见 `evidence/NN-response.json`；[`evidence/screenshots/`](screenshots.md) 有 **23 张不同截图**，10 张为原生前端各页面、筛选/详情/搜索/健康状态，13 张为清楚标注的辅助核对页。

可用能力：隔离实例在数分钟内采集 **4,610 条**文章，来源包括 RSS 3,755、Google News 629、Yahoo Finance 68、GitHub Trending 66、Hacker News 43、Reddit 25、网站监控 24。原生搜索 `OpenAI` 返回 20 条；“全部文章”信息流与文章详情可浏览；来源健康、API 文档、阅读模型都可访问。默认“信号文章”初始为空，切换“全部文章”后有内容。实时 lane 未启用；其 API 空结果符合文档中的 opt-in 约束。

核心限制：本轮运行事件聚合得到 `fresh_articles=580`、`usable_articles=39`、`events_updated=63`，整体状态 **degraded**；63 个活动事件的 `source_count` 全为 **1**，所以没有验证到“两个独立来源聚合为同一事件”的核心结果。多数文章没有可用的评分/叙事标签，`/api/ui/realtime` 无条目。不能仅以采集条数说明 LLM 评分、跨源信号已可用。

数据新鲜度问题：SQLite 4,610 行中，按文章真正的 `published_at` 算，过去 24 小时只 174 行；3,621 行发表已超过 7 天，3,252 行超过 30 天，243 行缺发布时间，2 行日期在未来。一条 Google News 项目的发布时间为 **2007-08-12**，2026-09-27 才被采进库。前端卡片显示的是 `collected_at` 的“几分钟前”，不等于文章发表时间，旧闻容易显得很新。UI 的来源健康页把同一 `rss` source type 的 24h fetched 数重复显示到每个 RSS 来源；总览的 `total_articles_24h` 高达约 196,900，而数据库实际只有 4,610 行。源码 `api/health_routes.py` 先按 source type 聚合 `articles_fetched`，随后逐注册来源复用该值并累加；这个数字是重复计数的 fetch 量，不能当实际 24 小时新文章数。

阶段判断：作为自托管情报采集与搜索工具，第一轮真实运行表明入口和主要来源能用；但“实时新鲜度”“每来源健康”和“跨源可信事件”仍有明显证据缺口。最终分数与 Data 类名次待 14 个项目全部试用后统一给出。
