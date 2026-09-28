# vectorbt · Trading Infra 首轮试用记录

## Trading Infra 类内评分：第 3 名 · 77/100

| 核心结果实测 | 数据可信度与时效 | 覆盖与深度 | 上手与复现 | 运行稳定性 | 总分 |
|---:|---:|---:|---:|---:|---:|
| 30/35 | 16/25 | 14/15 | 10/15 | 7/10 | **77/100** |

**评分依据：** multi-asset Portfolio.from_signals and per-asset stats/chart run with Plotly 6.3; default Plotly 7.1 resolution breaks import, reducing install/runtime score.


**建议定位：向量化投资组合回测/策略研究引擎（兼具技术指标参数化扫描），不是行情源或 Broker 执行层。** 仓库类别是 Trading Infra；从用户目的看也适合列为 Trading Strategy 的回测组件。Infra 类 6 项全测完后统一评分和排序。

## 安装和实际使用

catalog 锁定 commit `34b6d5935e3ea3eccd549e2592bc0f455b8045f5` 的源码版本为 `vectorbt==1.1.0`。在隔离 Python 3.13 环境安装，使用固定随机种子生成 1,200 根/标的的合成小时价格，对 `SYN_A`、`SYN_B` 计算 MA(12/36) 交叉，用 `Portfolio.from_signals` 加入 0.1% 手续费和 0.05% 滑点。两项组合都得到订单、已平仓交易、费用、收益、回撤、Sharpe 等统计；共 33 个交易记录，Plotly 单资产收益图也能生成。这里的百分比只是人为造出的价格路径结果，不代表真实策略绩效。

## 依赖兼容性缺口

按项目 `pyproject.toml` 声明安装时，Plotly 没有上限（仅 `>=4.12.0`）。当前解析到 Plotly 7.1.0 后，`import vectorbt` 在默认模板创建时失败：Plotly 不再接受 `scattermapbox` 属性。把 Plotly 固定到声明范围内的 6.3.0 后，导入与核心回测/绘图链路成功，`uv pip check` 全部依赖兼容。也就是说，最新依赖下全新安装可能开箱即失败，需要上游收紧兼容范围或升级模板。

多列 Portfolio 的默认 `.plot()` 需要显式选 `column`，否则 `Only one column is allowed`；多资产 `stats()` 默认按列取均值会提示，需逐资产统计或明确 `group_by`。本轮已按 `column`/逐资产方式生成图与统计。没有运行完整上游测试套件，也没有使用 Rust optional extra。

## 试用边界

没有使用 API、行情服务、账户、交易所或订单。vectorbt 接收调用方提供的 Pandas/Numpy 数组并计算结果；本轮不证明行情时效、交易执行或资金安全。截图 19–20 是 vectorbt 实际生成的 Plotly 图，21 是辅助评测页，不是原生 dashboard。

[21 张截图](screenshots.md) · [机器可读运行结果](evidence/smoke-summary.json)
