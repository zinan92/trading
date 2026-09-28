# zinan92/trading-strategy · 首轮试用记录

## 类内评分：第 3 名 · 76/100

| 核心结果实测 | 数据可信度与时效 | 覆盖与深度 | 上手与复现 | 运行稳定性 | 总分 |
|---:|---:|---:|---:|---:|---:|
| 27/35 | 18/25 | 10/15 | 13/15 | 8/10 | **76/100** |

**建议定位：DCA/Grid 计划与离线回放组件。** 评分依据：安装及 12 个确定性 DCA/Grid 场景可运行，核心测试 38 通过；完整测试的 2 个失败依赖维护者本机外部 checkout。仓库已归档迁入 trading-system。


**上游：** `zinan92/trading-strategy` · commit `856a80735f40fc4cf2a0fbd1f22cb0b05496bcca` · Python package `trading-strategy==0.1.0`。README 明确标注此仓库于 2026-09-27 归档并迁入 `zinan92/trading-system/packages/trading-strategy`。

## 安装与功能试用

- `uv pip install -e .` 在隔离 Python 3.13 环境成功；从仓库外目录使用 `-I` 仍可导入 `trading_strategy`。包不声明第三方运行时依赖。
- 用项目自身的 `build_deterministic_dca_candidate_payload_v1`、DCA preview / strategy-plan / entry command / mark replay、Grid preview / explicit and conditional replay、cost calculation 跑了 12 个确定性场景。DCA 多次加仓后只维持一个聚合退出单；触发 stop 后结束该轮次；Grid 计算 90–130 的网格级别与数量；hard stop 在同一根 bar 上优先于新增 rung。
- **所有输入都是仓库 golden-test 的固定夹具**（例如 GOLD/XAU、2026 年测试日期、合成 1m/4h/1d bars），不是最新市场数据。本轮只验证策略计划与离线 replay 计算，不是收益证据、回测报告或实盘执行。

## 自动化测试结果

- README 的完整命令 `python3 -m pytest -q`：46 passed、2 failed、0 skipped。失败项是 provenance/package-boundary 检查，依赖维护者本机 `maintainer-specific local trading-system-testnet checkout` 的 pinned Git source object；干净公开 clone 没有那个外部对象。没有修改该外部 checkout。
- 纯 DCA/Grid canonical golden、adaptive characterization、range-adjustment 三组聚焦测试：**38 passed，0 failed**。

## 定位建议

建议分类为 **Trading Strategy / 纯 DCA 与 Grid 计划/回放策略库**。它有真实可安装、可导入的计算代码，能输出版本化计划、仓位尺寸、价格精度、风险边界及确定性离线模拟。它不提供行情、用户界面、持久化执行适配器、broker 或下单能力；integration blocker 文档也明确要求由 Trading System 组合层接入。因此不是 standalone trading app，也不应把模拟收益当成策略表现。

证据：[函数结果图库](evidence/index.html) · [场景输入与输出](evidence/probes.json) · [测试和安装结果](evidence/test-suite-summary.json) · [截图清单](screenshots.md)。
