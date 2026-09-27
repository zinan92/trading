# TA-Lib · Trading Strategy 类阶段试用记录

**建议定位：跨市场技术指标计算引擎／Python+C 分析库组件，不是完整交易系统。**它接收调用方准备的 OHLCV/价格数组并返回指标值；不提供行情采集、策略编排、组合回测、风控工作台或下单界面。类内分数与名次待本类所有条目完成后统一决定。

## 类内评分：第 1 名 · 84/100

| 核心结果实测 | 数据可信度与时效 | 覆盖与深度 | 上手与复现 | 运行稳定性 | 总分 |
|---:|---:|---:|---:|---:|---:|
| 32/35 | 17/25 | 14/15 | 13/15 | 8/10 | **84/100** |

**建议定位：跨市场技术指标计算引擎／Python+C 分析库组件。** 分值奖励了 80 项通过的仓库测试、201 个可枚举指标和三类数据接口；stream EMA/RSI/MACD/ATR/ADX 的实测差异与 C 核心安装门槛已扣分。

## 已验证

按 catalog 锁定提交 `fd6089b183fc23b0e87512c455153043400efff6` 在隔离 Python 3.13 环境编译 Cython 扩展，并链接本机已安装的 TA-Lib C 核心 0.8.1。源码编译成功。完整仓库测试为 **80 passed**。库可以枚举 201 个指标和 10 个组；对固定种子合成的 500 根 OHLCV，SMA、RSI、MACD、BBANDS 计算成功；NumPy Function API、Pandas Series/DataFrame、Polars Series/DataFrame 适配通过，Pandas 索引保留；SMA 对首段缺失值的传播与 README 示例一致。

## 关键差异：Streaming API

我把同一批输入的 Streaming API 最新值与批量 API 最后一项逐个核对。10 个指标里 5 个递归类结果不一致：EMA 批量 `78.186676` / stream `77.936696`；RSI `52.964078` / `60.511352`；MACD 三项批量 `0.503904 / 0.390154 / 0.113750` / stream `0.825443 / 0.848885 / -0.023442`；ATR `1.539549` / `1.614580`；ADX `18.265048` / `18.837694`。SMA、MOM、MAXINDEX、BBANDS、STOCH 对得上。

Streaming API 在 README 中标为 experimental，但面向递归指标的输出差异没有被现有测试捕获；现有 streaming tests 覆盖 MOM、蜡烛形态和 MAXINDEX。把 stream EMA/RSI/MACD/ATR/ADX 用作实时最新信号前，需要先针对目标指标加同输入批量对账。完整数值见 `verification.json` 和截图 22。

## 评测边界

TA-Lib 是计算库，没有原生界面或命令行。截图 01–18 是准确固定提交上的 GitHub 源码/文档页；截图 19–22 是辅助评测页展示真实库输出，并非产品自带 dashboard。样例行情完全合成，不证明数据质量、指标预测能力或策略收益。安装此次成功是因为试用机已装有匹配的 Homebrew C library；该锁定提交的源码安装仍需要 TA-Lib C 核心和 Cython 编译环境。

- [22 张截图](screenshots.md) · [可复验记录](verification.json)
