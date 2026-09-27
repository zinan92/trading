# Qlib · not ranked

**Repository:** `microsoft/qlib`

**Evidence:** 12 screenshots.

## First-round result

隔离安装、简版行情、表达式、Alpha158、LightGBM 训练和 2,094 条样本外预测通过；样本数据止于 2021-06-11。SimulatorExecutor 的 Gym 导入超过两分钟未完成，回测未验证。建议移到 Trading Strategy。

## Detailed findings

# Qlib 试用记录

- 上游：`microsoft/qlib`，锁定 checkout `be725493eb1a6bbb42bf11b37aa7669f59610ff1`。
- 试用形态：隔离 Python 3.12 环境；产品是研究引擎/库，无原生 Web UI。本目录 screenshots 为真实命令及结果的辅助证据页。
- 数据：通过 checkout 自带的 `scripts/get_data.py` 下载 `qlib_data_simple`，51,810,838 字节，解压约 144 MB。下载器明确提示数据采集自 Yahoo Finance。最新交易日为 **2021-06-11**，因此它不能证明当前行情可用。README 说官方数据暂时关闭、指向一个 community dataset；checkout 的下载器默认指向另一个仓库，复现入口有不一致。

## 已实际跑通

- `uv pip install -e .` 成功；`pyqlib 0.1.dev1`、LightGBM 4.7.0 可导入。
- Qlib 初始化本地 CN provider 成功；日历 3,995 个交易日，2005-01-04 至 2021-06-11。`csi300` 的跨期去重名单列出 731 个代码，这不是单日指数成分数。
- 6 只 A 股在 2019-03 至 2021-06 区间查询 3,300 行，收盘价覆盖约 99.64%；原始 OHLCV 与复权因子字段、`Mean($close,5)`、`Ref($close,1)` 均返回值。
- Alpha158 处理器生成 158 个特征和 1 个标签，训练段准备出 5,850 行。
- LightGBM 小样本拟合完成，验证集 early stopping 在第 1 轮；训练 L2=0.825195、验证 L2=0.832564。测试段生成 2,094 条样本外预测。这个结果只验证计算链路，样本窄、数据陈旧、预测表现也不构成可用策略。

## 未验证与限制

- `qlib.backtest.executor.SimulatorExecutor` 首次导入时进入 `gym.wrappers.atari_preprocessing` 的文件读取，等待超过两分钟仍未完成；我停止了该进程。模拟组合和交易成本处理因此未验证。
- Alpha158 的 `calc_ic` 探针传入二维预测，报 `Data must be 1-dimensional`；这是本轮评测脚本调用形状不符，不能记作 Qlib 的产品故障，也没有将其作为通过的 IC 结果。
- 本轮没有使用实时数据、没有做真实账户连接，也没有证明样本外收益或策略盈利。

## 定位建议

Qlib 更像 **Trading Strategy 下的量化研究与回测引擎**，不是面向个股基本面的 Equity Research 应用。它适合能编写 Python 并自行准备数据的量化研究者；易用性低于 GUI 产品，当前试用也没有跑通组合回测。建议把 catalog 主分类改到 `trading-strategy`，角色标为 `offline quant research engine`。

证据页：[index.html](evidence/index.html)；完整机器运行记录保存在本地试用档案中；覆盖：[coverage.json](evidence/coverage.json)。截图：12 张，SHA-256 去重后 12 张。
