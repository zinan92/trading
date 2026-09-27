# Chancode · 首轮试用记录

## 类内评分：第 9 名 · 45/100

| 核心结果实测 | 数据可信度与时效 | 覆盖与深度 | 上手与复现 | 运行稳定性 | 总分 |
|---:|---:|---:|---:|---:|---:|
| 15/35 | 7/25 | 12/15 | 5/15 | 6/10 | **45/100** |

**建议定位：Chan 信号 Paper/AI 策略系统候选。** 评分依据：单次合成 replay 和 14 路由前端构建通过；干净 clone 的批处理回放缺模块/行情路径，后端离线时多页客户端报错。


**上游：** `zinan92/chancode` · commit `d3c21ecacb99317177b0bd81dbf585c0d2d9d957`（2026-04-07）。README 描述 Binance K 线、缠论信号、策略 A Paper、Claude 过滤策略 B、Supabase 和 Next.js Dashboard；Binance/Supabase/Anthropic 环境变量都是完整产品路径的依赖。

## 可在无密钥环境验证的部分

- 用 7 根合成 1m 蜡烛与 1 个买、1 个做空信号运行仓库真实 `replay.run_backtest`：模拟器生成一笔 buy/sell 和一笔 short/cover，测试账户从 10,000 增至约 10,201。手续费显式设为 0；价格、信号及走势均为人工合成，**不能当成策略收益证据**。
- 重复相同合成输入、只改 Python random seed（42/43），开仓价与结束资金有变化。`Account.buy/short` 使用 `random.uniform()` 在 K 线高低范围抽取成交价；重放结果要可复现，需要控制随机状态。
- `calculate_max_drawdown()` 将 `net_values[index]` 打印在“Index”字段，输出会把净值当成索引。这是显示错误；本次 7 bar 路径最大回撤恰好为零，无法评价实际回撤统计。
- 前端 `npm run build` 使用仅指向 127.0.0.1 的 Supabase/API 占位地址成功，14 个路由完成编译。前端 10 个页面均有截图。后端未启动；dashboard 显示 `Backend offline`、数值为空。`/trades`、`/backtest`、`/logs` 在 API 502 时抛出 `data.map/list.map/logs.map is not a function` 客户端异常；其他页显示空态或本地 API 错误。

## 完整链路阻断

- 仓库跟踪的 `sfz/BTC` 目录中有 4 个信号 CSV，但不含 OHLC 字段或原始 1m 行情。`replay/replay_multi.py` 直接导入本仓库缺失的 `check_out_param.py`，在导入阶段失败；若补上该依赖，脚本仍把行情文件写死在 `D:/code/chancode/sfz/...`，该市场文件也不在 clone 中。因此 README 所称离线多信号回测流程不能在干净 clone 直接复现。
- Claude 判断、Binance 行情、Supabase 持久化与 live 模式没有运行。没有交易所凭证或用户数据库；没有下单/转账操作。

## 定位建议

建议位置 **Trading Strategy / Chan 信号驱动的 Paper + AI 策略系统候选**，不是可直接使用的完整交易系统。Next.js 外壳可构建，回测原语可用合成数据运行；核心部署需要后端、Binance 行情、Supabase 与 Anthropic 配置，并且 README 指向的可复现批处理回测当前受缺失模块和路径阻断。AI 策略、真实行情、费用后收益和 Paper 状态持久化都未验。

证据：[离线 replay 与检查图库](evidence/index.html) · [前端截图图库](evidence/frontend-gallery.html) · [综合机器摘要](evidence/verification.json) · [截图清单](screenshots.md)。
