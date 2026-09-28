# Equity Research Skill · 70

**Repository:** `rollingSirius/equity-research-skill`

**Evidence:** 17 screenshots.

## First-round result

DCF、PVGO、EPV、EVA、蒙特卡洛与内置示例检查器能运行；7 个聚焦测试通过。作者 NVDA 示例当前检查报 P1；没有本轮新生成的真实研报。

## Score breakdown

| Dimension | Score | Max |
|---|---:|---:|
| 核心结果实测 | 22 | 35 |
| 数据可信度与时效 | 21 | 25 |
| 覆盖与深度 | 9 | 15 |
| 上手与复现 | 11 | 15 |
| 运行稳定性 | 7 | 10 |
| **Total** | **70** | **100** |

## Detailed findings

# equity-research-skill · Equity Research 类第 5 个首轮试用

- 上游：[`rollingSirius/equity-research-skill`](https://github.com/rollingSirius/equity-research-skill)，源码 `3d94e64ff53b325d866ea4bff69ad81a5adca8f5`。这是一个**个股深研 Agent Skill＋本地估值/检查脚本**，不是可部署的原生 Web 产品。美国、香港、A 股均在文档覆盖范围；本轮未生成新的真实公司九章研报。
- 证据：脚本、检查器和上游示例核对摘要 记录脚本 DEMO、检查器、四份上游示例和聚焦测试；运行日志保留在本地试用档案；[截图清单](screenshots.md) 有 **17 张不同的辅助证据页截图**，清楚标注合成 DEMO 和作者示例不是本轮新研究成果。

实际可运行：`scripts/dcf.py --demo` 成功完成三情景概率加权（**57.5/股**，纯合成）、敏感性、反向 DCF、PVGO、EPV、EVA、2,000 次蒙特卡洛和仓位标定；`scripts/check_research_output.py --demo` 返回“未发现可复算异常”；聚焦检查器测试 **7/7 通过**。仓库有 20 个行业附录、11 个参考文档，研究合同对来源与时间戳、预期差、财报可信度、反方论证和可复算估值的要求具体。

示例与当前门槛不一致：用仓库**自己的**检查器检查作者附带的 NVDA 中文／英文示例，分别返回 **1 个 P1 + 7 个 P2** 和 **1 个 P1 + 8 个 P2**。共同的 P1 为半导体必备“库存周期／产能利用率”等 cycle position KPI 缺失；Google 中文／英文示例 exit 0，但仍分别有 4／6 个 P2，涉及 AI capex 拆分、决策三分法、预测验证登记等。示例目录没有相配的估值假设 JSON 或财务 CSV，因而不能从这些 Markdown 样例独立复算作者展示的公司目标价。示例可能早于检查器新规则，但 README 当前称它们是 v2 完整模式示例，访问者会误以为已通过现行合同。

没有联网采集真实披露、没有独立完成最新 NVDA/GOOGL 财务对账，也没有实际产出新 PDF 或进行人工证据审查。脚本 DEMO 和 7 个测试证明计算与规则组件能运行，不证明九章报告会自动取得足够可信的新数据或结论。阶段判断：**研究方法和计算辅助较成熟，端到端实时深研仍未验；示例与检查器漂移需要修复**。Equity Research 类全部测完后统一打分。
