# HiThink-Tech/Financial-API · Data 类第 5 个首轮试用

- 原仓库：https://github.com/HiThink-Tech/Financial-API
- 实测源码：`3bca7805a4127ece8d81961917e740d2effac6ec`；Trading catalog 锁在较早的 `402574a6221d5e255dba47166df8e5abb7149938`。本轮 CLI 子项目版本 `0.1.13`。
- 按仓库 `AGENTS.md` 和 `hithink-finance` Skill 的入口，使用隔离的 `hithink-finance-cli/` 构建并测试；没有全局安装或写入用户现有凭据。新建独立 profile 与空 DuckDB。环境变量及标准用户级 `credentials.env` 均未发现现成 API Key，本轮未进入任何账户登录。
- [`evidence/probes.json`](evidence/probes.json) 保存 23 个真实 CLI/REST 响应的脱敏摘要；[`evidence/index.html`](evidence/index.html) 和 [`23 张截图`](screenshots.md) 是 Product Lab 辅助试用页面，**不是同花顺原生 AI 客户端或授权后的行情界面**。

## 已实际通过

1. `npm ci --ignore-scripts` 与 TypeScript 构建通过；CLI `version` 返回 `ok=true` 和 `0.1.13`。
2. `capabilities` 返回 **104 个声明的命令能力**，其中 88 个标为远端、16 个本地。标的搜索、A 股行情与历史、财报、指数、基金、期货、期权等 13 个业务契约查询都可读。**契约数量不是 88 个远端接口已经成功取数。**
3. 内置 Skills 状态、隔离 DuckDB 状态以及 `SELECT 1` 和表元数据只读 SQL 查询通过。该空库 `version=0`、表数为 0，不能当作 A 股历史库已经建好。
4. 官方 REST 端点能连接，但无 Key 请求返回 **HTTP 200 + 业务 `code=2003` + `data=null`**；CLI 远端标的搜索与最新行情均以退出码 3、`AUTH_API_KEY_MISSING` 明确失败。客户端必须同时检查业务信封；HTTP 200 本身不是成功。
5. `npm audit --omit=dev` 本轮返回生产依赖漏洞 0 项；安装时 npm 报的 5 项在全依赖树中，不能误写为生产依赖 5 项。

## 未验证与定位

- 没有同花顺统一 API Key，所以 A 股实时行情、日线、财务、估值、指数、板块、基金、期货期权的**线上数据返回均未验证**；本轮实际远端市场数据行数为 0。也没有验证托管 MCP、Python 远端 toolkit 或端内 AI 客户端。
- 项目公开入口的明确范围是 **A 股行情与衍生数据**；README 写明公开 API/CLI/MCP/Python **不提供分钟 K、tick、Level-2、美股或港股行情**。部分端内专用能力属于另一个客户端界面，不能混入这个公开 API 的评分。
- 推荐定位：**需授权的同花顺官方 A 股多域数据服务与本地研究 CLI／DuckDB 工具链**。它既有最新快照，也声明历史日线；本轮只验证本地契约和认证边界，在线实时性与数据质量要在授权后试验。

结论：接入面和本地 CLI 很完整，错误信封清楚；缺 API Key 使核心远端数据能力在本轮不可判定。Data 类所有 14 项完成后统一打分与排序。
