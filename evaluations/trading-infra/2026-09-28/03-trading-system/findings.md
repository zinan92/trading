# trading-system · Trading Infra 首轮试用记录

## Trading Infra 类内评分：第 5 名 · 65/100

| 核心结果实测 | 数据可信度与时效 | 覆盖与深度 | 上手与复现 | 运行稳定性 | 总分 |
|---:|---:|---:|---:|---:|---:|
| 20/35 | 9/25 | 15/15 | 12/15 | 9/10 | **65/100** |

**评分依据：** Dashboard/Desk and read-only APIs run locally and the predeploy gate passes; there are no trusted bars, so production strategy/market path remains blocked. Scope fits Full Trading System better than Infra.


**定位判断：这不是单一交易基础设施库，而是集成式 Paper 交易平台。** 仓库把 GridMind Dashboard、trading-desk、策略/风险、standard-broker、standard-kline 和 Paper 控制放在同一 monorepo。若按产品角色分类，整个 `zinan92/trading-system` 更适合放在 **Full Trading System / Agent**；Trading Infra 留给 `standard-broker`、`standard-kline` 等可独立复用的底层组件。本类评分与排序待六项全部完成后统一给出。

## 隔离安装、启动与实际浏览

按迁移后的 monorepo commit `bbdcf9005cbf15860b6a6214a408634925580923`，先用项目自己的 `PaperPredeployGate` 检查本机 Python 兼容性和干净 source tree。Gate 在 trial 专属输出目录生成 `pass` 回执，验证代码同时明确 `starts_services/submits_orders/cancels_orders/closes_positions/uses_exchange_credentials` 全为 `false`。随后只从开发 checkout 启动 Dashboard 和 trading-desk，监听本次临时端口 `18765/18890`；没有碰 `trading-platform` 生产 checkout。

市场数据库、desk SQLite、Paper receipts、兼容性回执都指向 trial 私有目录。GridMind 的 datafeed 地址覆盖为隔离的 loopback 空端口，Python 子进程的网络守卫拒绝非本机连接，浏览器也只允许本机页面。Dashboard 主页面、Desk `/desk` 与集成代理 `/trade` 都能打开；本地 read-model、supervisor-history、Desk health/assets 请求返回 HTTP 200。

## 实际结论与阻塞

Dashboard 把系统呈现为 **Paper / stopped**，没有运行策略、挂单或持仓。行情 API 返回 `status=blocked`、`bar_count=0`、`is_synthetic=false`；图表显示 datafeed unavailable，read-model 的市场状态为 blocked。也就是说，无 API/数据源时它会明确阻止新开仓，没有把空数据伪装成可交易行情。大部分主导航、K 线周期、只读持仓/委托/成交/Supervisor/复盘/历史视图、策略配置表单和 Desk 的日报/系统页面可浏览。没有提交预览、执行、启动、停止、撤单或平仓动作。

本机浏览器对 Desk 主页面代理的 `/trade` 请求在 Dashboard 服务同时运行后返回 200。Dashboard 服务被隔离后，Desk 会显示后台暂时不可用，这是它依赖 GridMind 后端的显式状态。Desk `/api/health` 标注执行范围为 Hyperliquid Testnet 且需要人工动作；这是路由能力说明，本轮没有请求任何执行路由。

与启动闸门、read-model/API、Paper-only/桌面静态界面相关的聚焦测试 **88 passed**。本轮没有跑完整 monorepo `make test`，也没有测试市场数据的外部接入、策略收益、Nautilus 在 trading-system 本身的集成、Testnet 或 Live 订单链路。50 张不同截图覆盖 Dashboard 与 Desk；其中一些浏览器控制台资源错误来自评测时主动拦截 Google Fonts 外网和缺省 favicon，不是后端 JavaScript 异常。

## 证据

- [50 张不同截图](screenshots.md) · [浏览器与本地 API 摘要](verification.json) · [截图画廊](evidence/index.html)
- 所有被隔离服务已停止；`18765/18890` 没有监听进程。
