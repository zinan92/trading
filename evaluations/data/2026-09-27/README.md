# Trading · Data 类首轮实测与截图

**首轮试用，不是完整功能认证。** 分数衡量这次实际取得的核心结果、数据质量、覆盖、上手与运行表现，不是盈利评级，也不等于生产环境或商业许可验收。不同角色的元数据库、行情 SDK、新闻管线不可仅凭几分之差互换；无 Key、周末、空隔离库造成的未验证能力单独说明。目录原分类和锁定版本保持不变。

**怎么选：** FinanceDatabase 适合查证券代码与分类，不提供价格；AKShare 的已验证历史接口覆盖最广，但必须逐个检查来源时戳；watchlist 是高可靠的静态研究名单；Datafeed 更适合需要标准化多市场 OHLCV 与来源标记的程序。这四项排名靠前的原因不同。`trump-code` 的主要用途是事件信号研究，建议在后续目录整理时移往 Trading Strategy／Event Signals。

[评分方法](methodology.md) · [图片清单](screenshot-inventory.json) · [返回 Trading](../../../README.md)

| 排名 | 产品／原仓库 | 分数 | 本轮实际定位 | 实测结论 | 证据 |
|---:|---|---:|---|---|---|
| 1 | [FinanceDatabase](https://github.com/JerBouma/FinanceDatabase) | **87/100** | 多市场静态证券标识与分类元数据库 | 元数据核心任务最扎实；没有市场价格 | [判断](07-financedatabase/README.md) · [截图](07-financedatabase/screenshots.md) |
| 2 | [akshare](https://github.com/akfamily/akshare) | **83/100** | A／美股、基金、债券、期货、宏观与新闻 Python 数据接口库 | 广覆盖历史数据强；实时接口须逐个验时效 | [判断](14-akshare/README.md) · [截图](14-akshare/screenshots.md) |
| 3 | [watchlist](https://github.com/zinan92/watchlist) | **81/100** | 资产、赛道和研究对象的静态 reference registry | 静态名单与引用校验通过；不提供行情 | [判断](04-watchlist/README.md) · [截图](04-watchlist/screenshots.md) |
| 4 | [datafeed](https://github.com/zinan92/datafeed) | **80/100** | A／美股、加密、商品与美债的标准化 OHLCV API | 多市场 K 线可用；矩阵采集和授权尚未就绪 | [判断](10-datafeed/README.md) · [截图](10-datafeed/screenshots.md) |
| 5 | [tickflow](https://github.com/tickflow-org/tickflow) | **79/100** | A股／美股／港股历史行情 SDK | 免费历史查询可用；分钟和实时受权限限制 | [判断](01-tickflow/README.md) · [截图](01-tickflow/screenshots.md) |
| 6 | [tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp) | **75/100** | 多市场研究、筛选与技术分析 MCP | 23 个场景有结果，部分源与需 Key 工具失败 | [判断](03-tradingview-mcp/README.md) · [截图](03-tradingview-mcp/screenshots.md) |
| 7 | [a-stock-data](https://github.com/simonlin1212/a-stock-data) | **70/100** | A 股行情、财务与研究代码 Skill | 腾讯／新浪主路径可用；百度均线 K 返回空 | [判断](09-a-stock-data/README.md) · [截图](09-a-stock-data/screenshots.md) |
| 8 | [global-stock-data](https://github.com/simonlin1212/global-stock-data) | **67/100** | 美股／港股研究数据与技术指标 Agent Skill | 官方宏观与本地指标可用；期权主卖点未实测 | [判断](08-global-stock-data/README.md) · [截图](08-global-stock-data/screenshots.md) |
| 9 | [FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP) | **63/100** | AI Agent 金融数据 MCP 路由 | 加密 K 线与公开新闻可用；A／美股需授权 | [判断](02-financemcp/README.md) · [截图](02-financemcp/screenshots.md) |
| 10 | [adata](https://github.com/1nchaos/adata) | **58/100** | A 股历史 K 线与盘口多源 Python SDK | 部分 K 线可取；重复调用与实时解析不稳定 | [判断](06-adata/README.md) · [截图](06-adata/screenshots.md) |
| 11 | [intel](https://github.com/zinan92/intel) | **54/100** | 跨来源新闻采集、搜索和事件研究平台 | 采集与搜索可用；跨源确认尚无通过样本 | [判断](12-intel/README.md) · [截图](12-intel/screenshots.md) |
| 12 | [quant-data-pipeline](https://github.com/zinan92/quant-data-pipeline) | **52/100** | 多资产行情看板＋感知信号＋本地模拟交易 | 商品／加密与纸盘可用；A 股和稳定性缺口大 | [判断](13-quant-data-pipeline/README.md) · [截图](13-quant-data-pipeline/screenshots.md) |
| 13 | [Financial-API](https://github.com/HiThink-Tech/Financial-API) | **49/100** | 需授权的官方 A 股数据 API 与本地 CLI | 本地契约可用；在线行情未获授权验证 | [判断](05-financial-api/README.md) · [截图](05-financial-api/screenshots.md) |
| 14 | [trump-code](https://github.com/sstklen/trump-code) | **42/100** | 政治发言驱动的美股事件信号研究 | 历史命中率可复算；最新帖链路断裂 | [判断](11-trump-code/README.md) · [截图](11-trump-code/screenshots.md) |

## 1. FinanceDatabase · 87/100

元数据核心任务最扎实；没有市场价格

**多市场静态证券标识与分类元数据库** · Python SDK；截图为辅助证据页

[![FinanceDatabase 代表截图](07-financedatabase/images/02-financedatabase.png)](07-financedatabase/README.md)

[判断依据](07-financedatabase/README.md) · [全部截图](07-financedatabase/screenshots.md)

## 2. akshare · 83/100

广覆盖历史数据强；实时接口须逐个验时效

**A／美股、基金、债券、期货、宏观与新闻 Python 数据接口库** · Python SDK；截图为辅助证据页

[![akshare 代表截图](14-akshare/images/05-AKShare.png)](14-akshare/README.md)

[判断依据](14-akshare/README.md) · [全部截图](14-akshare/screenshots.md)

## 3. watchlist · 81/100

静态名单与引用校验通过；不提供行情

**资产、赛道和研究对象的静态 reference registry** · 原生静态页面＋辅助校验页

[![watchlist 代表截图](04-watchlist/images/01-native-tree-y0.png)](04-watchlist/README.md)

[判断依据](04-watchlist/README.md) · [全部截图](04-watchlist/screenshots.md)

## 4. datafeed · 80/100

多市场 K 线可用；矩阵采集和授权尚未就绪

**A／美股、加密、商品与美债的标准化 OHLCV API** · 原生 HTTP API／健康看板＋辅助证据页

[![datafeed 代表截图](10-datafeed/images/03-native-api-docs.png)](10-datafeed/README.md)

[判断依据](10-datafeed/README.md) · [全部截图](10-datafeed/screenshots.md)

## 5. tickflow · 79/100

免费历史查询可用；分钟和实时受权限限制

**A股／美股／港股历史行情 SDK** · Python SDK；截图为辅助证据页

[![tickflow 代表截图](01-tickflow/images/02-tickflow-api.png)](01-tickflow/README.md)

[判断依据](01-tickflow/README.md) · [全部截图](01-tickflow/screenshots.md)

## 6. tradingview-mcp · 75/100

23 个场景有结果，部分源与需 Key 工具失败

**多市场研究、筛选与技术分析 MCP** · MCP 服务器；截图为辅助证据页

[![tradingview-mcp 代表截图](03-tradingview-mcp/images/04-tradingview-mcp.png)](03-tradingview-mcp/README.md)

[判断依据](03-tradingview-mcp/README.md) · [全部截图](03-tradingview-mcp/screenshots.md)

## 7. a-stock-data · 70/100

腾讯／新浪主路径可用；百度均线 K 返回空

**A 股行情、财务与研究代码 Skill** · Python Skill；截图为辅助证据页

[![a-stock-data 代表截图](09-a-stock-data/images/04-a-stock-data.png)](09-a-stock-data/README.md)

[判断依据](09-a-stock-data/README.md) · [全部截图](09-a-stock-data/screenshots.md)

## 8. global-stock-data · 67/100

官方宏观与本地指标可用；期权主卖点未实测

**美股／港股研究数据与技术指标 Agent Skill** · Python Skill；截图为辅助证据页

[![global-stock-data 代表截图](08-global-stock-data/images/02-global-stock-data.png)](08-global-stock-data/README.md)

[判断依据](08-global-stock-data/README.md) · [全部截图](08-global-stock-data/screenshots.md)

## 9. FinanceMCP · 63/100

加密 K 线与公开新闻可用；A／美股需授权

**AI Agent 金融数据 MCP 路由** · MCP 服务器；截图为辅助证据页

[![FinanceMCP 代表截图](02-financemcp/images/03-finance-mcp.png)](02-financemcp/README.md)

[判断依据](02-financemcp/README.md) · [全部截图](02-financemcp/screenshots.md)

## 10. adata · 58/100

部分 K 线可取；重复调用与实时解析不稳定

**A 股历史 K 线与盘口多源 Python SDK** · Python SDK；截图为辅助证据页

[![adata 代表截图](06-adata/images/02-adata.png)](06-adata/README.md)

[判断依据](06-adata/README.md) · [全部截图](06-adata/screenshots.md)

## 11. intel · 54/100

采集与搜索可用；跨源确认尚无通过样本

**跨来源新闻采集、搜索和事件研究平台** · 原生 Web／API＋辅助审计页

[![intel 代表截图](12-intel/images/09-native-feed-all.png)](12-intel/README.md)

[判断依据](12-intel/README.md) · [全部截图](12-intel/screenshots.md)

## 12. quant-data-pipeline · 52/100

商品／加密与纸盘可用；A 股和稳定性缺口大

**多资产行情看板＋感知信号＋本地模拟交易** · 原生 React／API＋辅助证据页

[![quant-data-pipeline 代表截图](13-quant-data-pipeline/images/13-dashboard-section.png)](13-quant-data-pipeline/README.md)

[判断依据](13-quant-data-pipeline/README.md) · [全部截图](13-quant-data-pipeline/screenshots.md)

## 13. Financial-API · 49/100

本地契约可用；在线行情未获授权验证

**需授权的官方 A 股数据 API 与本地 CLI** · CLI；截图为辅助证据页

[![Financial-API 代表截图](05-financial-api/images/03-financial-api.png)](05-financial-api/README.md)

[判断依据](05-financial-api/README.md) · [全部截图](05-financial-api/screenshots.md)

## 14. trump-code · 42/100

历史命中率可复算；最新帖链路断裂

**政治发言驱动的美股事件信号研究** · 原生 Web／API＋辅助数据核对页

[![trump-code 代表截图](11-trump-code/images/01-dashboard-hero.png)](11-trump-code/README.md)

[判断依据](11-trump-code/README.md) · [全部截图](11-trump-code/screenshots.md)
