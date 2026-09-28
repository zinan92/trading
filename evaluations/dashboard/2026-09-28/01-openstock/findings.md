# OpenStock · 78/100 · Dashboard 候选

## 角色判断

OpenStock 更适合归在 Dashboard：面向人的市场总览、行情卡、股票研究页和 watchlist。它并没有在本轮显示订单、成交或持仓闭环，不应因“terminal”文案移入 Full Trading System。数据与部署说明都强调 Finnhub/MongoDB；公开首页称社区版行情每小时刷新，云版更快且仍标为 Coming soon。

## 本轮实际验证

- 在隔离 checkout 安装锁定依赖，npm test -- --reporter=dot：6 个测试文件通过、1 个跳过；99 个测试通过、4 个跳过。
- 本地尝试 Next.js 15.5.7 开发服务器。代码在导入 lib/better-auth/auth.ts 时顶层连接 MongoDB；没有 MONGODB_URI 会抛出缺失错误。Docker daemon 尝试启动官方 Mongo 7 容器时返回 containerd 元数据 I/O error，因此没有本地 DB，也未能进入自托管 app 主屏。没有为继续测试而改源代码或建立远程 DB。
- README 指向的公开部署可匿名打开：首页显示 NYSE 市场状态、指数行情预览、每小时缓存说明；About、Help、Architecture、Sponsor、Terms、Sign in、Sign up 页面均可打开。
- 在注册页点击空表单后，前端给姓名、邮箱、密码显示必填提示；验证停留在客户端，未创建账号或提交个人资料。
- 匿名直接访问 /dashboard 与 /stocks/SPY 都被重定向至 /sign-in。故 watchlist 持久化、提醒创建、证券详情、TradingView 图表及真实账户内数据均未验证。
- 留存 17 张唯一界面截图；其中 1 张为上游仓库来源确认，其余来自公开部署。截图所对应的 Vercel 部署 SHA 未能绑定到 catalog 锁定 commit，故公开界面只作可见产品体验证据。

## 五维评分

| 维度 | 分数 | 证据与限制 |
|---|---:|---|
| 核心结果实测 | 27/35 | 公开市场首页及帮助/数据模式页面可见；登录后的股票研究和 watchlist 被认证门挡住 |
| 数据可信度与时效 | 18/25 | 产品明示共享缓存与 hourly delayed 状态；没有账户内行情或告警触发结果 |
| 覆盖与深度 | 13/15 | 首页承诺图表、热图、情绪、新闻、搜索、财务和提醒；其中账户内模块未验 |
| 上手与复现 | 12/15 | 注册引导与帮助文档清楚；自托管还需要 MongoDB/Finnhub 配置 |
| 运行稳定性 | 8/10 | 99 个单测通过、公开页面加载；本地服务在缺 DB 时阻断，另 4 个测试跳过 |

## 结论

首轮看起来像成熟度较高的公共市场 Dashboard，但本轮只实测了匿名层和注册客户端校验。要给出更高的功能成熟度判断，仍需真实用户账号、Watchlist/告警操作、详情页行情时效和一次端到端部署复验。不能据本次截图判断行情准确、投资建议质量或交易能力。
