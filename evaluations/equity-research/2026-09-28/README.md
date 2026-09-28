# Trading · Equity Research 首轮试用、排序与定位

**首轮实测，不是完整功能认证。** 评分看本轮是否实际得到可用研究结果、来源和时效是否可靠、功能覆盖、上手复现与运行表现，不评估未来收益。完整方法见 [methodology.md](methodology.md)。

同类的前两项分别代表两种路径：Maverick MCP 擅长按需调取研究数据并管理研究对象；UZI 能产出更完整的个股报告，但本轮发现报告里的数据与来源叙述需要复核。其余工具更适合估值计算或研究流程支持。

| 排名 | 产品 / 原仓库 | 分数 | 建议定位 | 本轮判断 | 证据与截图 |
|---:|---|---:|---|---|---|
| 1 | [Maverick MCP](https://github.com/wshobson/maverick-mcp) | **79** | 多市场个股研究 MCP 工具层 | 行情、基本面、技术分析与组合/自选/日志操作真实可用；研报深度和数据源时效需按场景核实。 | [判断](01-maverick-mcp/findings.md) · [22 张截图](01-maverick-mcp/screenshots.md) |
| 2 | [UZI Skill](https://github.com/wbh604/UZI-Skill) | **73** | 生成式个股研究报告 Skill | 报告确实生成，数据覆盖 72%；币种、ROE 和工具调用记录的关键不一致削弱结论可信度。 | [判断](06-uzi-skill/findings.md) · [49 张截图](06-uzi-skill/screenshots.md) |
| 3 | [Equity Research Skill](https://github.com/rollingSirius/equity-research-skill) | **70** | 个股估值和报告检查 Skill | 估值与检查器可跑，聚焦测试通过；作者 NVDA 案例触发自身 P1，未生成新的真实报告。 | [判断](05-equity-research-skill/findings.md) · [17 张截图](05-equity-research-skill/screenshots.md) |
| 4 | [Serenity Skill](https://github.com/muxuuu/serenity-skill) | **68** | 有来源约束的主题研究 Skill | 检查规则和一手资料样本可用；没有从头生成并核对完整主题研究。 | [判断](07-serenity-skill/findings.md) · [13 张截图](07-serenity-skill/screenshots.md) |
| 5 | [Equity Research](https://github.com/zinan92/equity-research) | **50** | 个股报告界面原型 / DEMO | 前端可体验；当前 fresh clone 被 DEMO 门禁限制，不能产出真实完整报告。 | [判断](04-equity-research/findings.md) · [29 张截图](04-equity-research/screenshots.md) |

## 分类建议

| 原目录条目 | 本轮处理 | 建议角色 |
|---|---|---|
| [A Share Heatmap](https://github.com/wenyuanw/a-share-heatmap) | 已在原分类实测，24 张图，不参与 Equity Research 排名 | Dashboard / A 股市场热力图与自选观察 |
| [Day1 Global Skills](https://github.com/star23/Day1Global-Skills) | 已在原分类初测；按用户要求 Knowledge & Collections 不再测、不评分 | Knowledge & Collections / 市场研究知识 Skill 包 |
| [Qlib](https://github.com/microsoft/qlib) | 已测，12 张图，不参与本类排名 | Trading Strategy / 离线量化研究与模型训练引擎 |
| [Dexter](https://github.com/virattt/dexter) | 用户要求跳过；无凭证时未部署或运行 | 暂不评分 |

本轮原目录的 8 个实测产品共留存 **181 张截图**：5 个 Equity Research 候选共 130 张，另有 24 张 Heatmap、15 张 Day1 和 12 张 Qlib 截图；Dexter 按要求跳过。逐项来源、结论与截图 SHA-256 见每个产品目录。
