# Gloomberb · 82/100 · Dashboard / multi-market research terminal

## 角色判断

Gloomberb 是可交互的 finance terminal，提供 TUI、桌面版和一组 CLI 查询/截图能力。CLI 形态不意味着它是 Trading Engine；本轮没有订单或持仓同步，也没有连接账户。它适合保留在 Dashboard，子定位为终端式市场研究、行情和组合查看界面。

## 本轮实际验证

在锁定提交上用 Bun 1.3.9 安装 363 个包。通过自定义 ConfigStore test host 将应用配置和 SQLite 明确隔离到试用目录，子进程环境不带 HOME、API key 或用户配置，外部插件加载关闭。

- TUI 首次启动进入 Welcome setup；跳过 setup 后主界面可打开。默认 Main Portfolio 是空的；页眉显示 2026-09-25 的 SPY quote 与 CLOSED 状态，另一个 read-only community pane 可见登录边界。没有登录或导入真实账户。
- CLI help 与 provider status 正常。Provider status 列出 Gloomberb Cloud、Yahoo、RSS 等能力；没有读取凭证或 broker account。
- CLI 对 AAPL 的一笔公开只读 quote 查询返回 10 个主要报价字段；providerId 为 gloomberb-cloud、dataSource 为 delayed、sessionDate 为 2026-09-25、marketState 为 CLOSED。请求没有 API key，未测试盘中实时性。
- 在隔离目录建立 EVAL-ONLY 手工 portfolio，添加 10 股 AAPL、每股成本 300 USD；portfolio show 能读回成本、数量和估值，没有真实经纪商仓位或交易。
- 使用产品自身的 shot 命令运行 15 个 pane 场景：Quote Monitor、Graph Price、Comparison Chart、Financial Analysis、Valuation Graph、Fundamental Graph、Intraday Price Graph、Sector Performance、Economic Calendar、Top News、Market Movers、Yield Curve、SEC Filings、Analyst Research、Portfolio Analytics。前 14 张 pane 截图均为非空、complete、usable；Portfolio Analytics 渲染默认 Main Portfolio 空态，报告 rowCount=0、usable=false，未从 EVAL-ONLY 组合生成面板结果。单独的 portfolio show CLI 路径可读。
- 离线定向测试 23 项通过，覆盖 CLI entry、screenshot readiness/凭证脱敏和自动化命令边界。

## 五维评分

| 维度 | 分数 | 证据与限制 |
|---|---:|---|
| 核心结果实测 | 30/35 | 多个研究 pane 的 CLI 截图可用，一笔无 key 报价和本地组合 CLI 流程成功；组合分析 pane 没显示隔离组合 |
| 数据可信度与时效 | 19/25 | quote 明示 delayed、session date 和 market state；没有完整核验多个源的原始时间戳、交易所授权或实时覆盖 |
| 覆盖与深度 | 14/15 | 77 个 pane/capability catalog 条目涵盖股票、宏观、新闻、期权、估值与研究 |
| 上手与复现 | 11/15 | Bun CLI、help、JSON 和隔离安装路径明确；网页版本需 Gloom Cloud 账号，未登录验收 |
| 运行稳定性 | 8/10 | 15 个 pane 生成 14 张 usable 截图，23 项定向自动化测试通过；没跑完整发行包构建和全量测试 |

## 分类建议

保留在 Dashboard，不移入 Full Trading System。它有丰富的研究和组合工作界面，但没有订单生命周期。本轮只测试了 CLI/TUI 与公开市场数据；broker-position sync、账户连接、AI provider 和 web account flow 都未执行。

组合 pane 的空态与 CLI 组合数据不一致，建议复验 Pane selection / portfolio binding 后再对该具体模块给通过结论。
