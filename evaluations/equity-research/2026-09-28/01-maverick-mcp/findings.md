# Maverick MCP · 79

**Repository:** `wshobson/maverick-mcp`

**Evidence:** 22 screenshots.

## First-round result

37 个核心工具；22 个调用场景；AAPL、MSFT、美股与港股行情和基本面查询；自选、组合、日志 CRUD 通过。周末返回的是上个交易日收盘价，深度研报和回测扩展未装。

## Score breakdown

| Dimension | Score | Max |
|---|---:|---:|
| 核心结果实测 | 28 | 35 |
| 数据可信度与时效 | 20 | 25 |
| 覆盖与深度 | 11 | 15 |
| 上手与复现 | 12 | 15 |
| 运行稳定性 | 8 | 10 |
| **Total** | **79** | **100** |

## Detailed findings

# MaverickMCP · Equity Research 类第 1 个首轮试用

- 上游：[`wshobson/maverick-mcp`](https://github.com/wshobson/maverick-mcp)，源码 `a133057d7bfe838f983a53e3c691078d53ac5afc`，Core 安装版 1.1.0。用 `uv sync --no-dev` 隔离安装，在 `127.0.0.1:8773/mcp` 启动原生 Streamable HTTP，数据库仅落在本轮试用目录；未配置 LLM 或 Exa key，不执行真实证券委托。
- 定位：**个人股票研究与持仓跟踪 MCP 服务器**，可供任意 MCP 客户端调用；不是原生网页，也不是真实交易系统。37 个 Core tools 实际注册。`[backtesting]` 和 `[research]` extras 未安装，因此 12 回测工具、3 深度研究工具**没有注册，也未算通过**。
- 证据：本轮 22 个 MCP 场景摘要 记录 22 个 MCP 场景；完整场景摘要见本页；[截图清单](screenshots.md) 有 22 张不同截图，均为明确标注的 Product Lab 辅助证据页，非产品原生 Web。

真实结果：AAPL、MSFT 报价取得，AAPL 2026-09 日 K 18 根，末根 2026-09-25 收盘 **341.07**，与 Data 类 AKShare、datafeed 样本一致；AAPL fundamentals、美国市场概览、RSI/MACD/完整技术分析均有结果。筛选引擎运行后 AAPL 入选 bullish screen；这次只筛了**已查询的 1 只股票**，不能解释为全市场扫描。A 股 `600519.SS` 报价 1237.0、港股 `0700.HK` 报价 436.6，说明 yfinance 标准后缀在本轮可用，未验证其它 A/HK 研究工具精度。

持仓和研究日志在隔离库中形成了实际读写闭环：空组合 → 加 2 股 AAPL、成本价 341.07 → 回读组合成本 682.14 和单一科技板块风险；创建自选表、添加 AAPL、取得 brief；新增一条测试买入日志并从 journal 回读。这些是**本地研究记录**，不是券商订单、成交或真实账户资产。

时戳边界：周日 2026-09-27 的 `get_quote(AAPL)` 回传 `timestamp=2026-09-27T10:37Z`，但历史末根是 2026-09-25，价格也是 9 月 25 日收盘价 341.07。这里的 timestamp 实际为**取数时刻**，若客户端把它当市场成交时间会误判实时性；筛选记录的 `date_analyzed=2026-09-27` 同样是计算日期而非新交易日。上游 README 的“real-time quotes”在本轮周末不能据此算已验实时成交。

阶段判断：Core 对个人股票技术研究和本地组合跟踪已有扎实实测证据，部署简单；深度研究 Agent 与回测属于独立可选层，本轮没有安装、凭证和结果。Equity Research 类全部测完后再统一打分和定位。
