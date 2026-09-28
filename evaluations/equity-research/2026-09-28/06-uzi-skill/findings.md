# UZI Skill · 73

**Repository:** `wbh604/UZI-Skill`

**Evidence:** 49 screenshots.

## First-round result

AAPL lite 真实运行生成完整 HTML 报告、分享卡和战报；72% 数据覆盖。币种、ROE 和来源尝试记录有关键不一致，报告精确入场/止损数字需人工复核。

## Score breakdown

| Dimension | Score | Max |
|---|---:|---:|
| 核心结果实测 | 30 | 35 |
| 数据可信度与时效 | 16 | 25 |
| 覆盖与深度 | 11 | 15 |
| 上手与复现 | 10 | 15 |
| 运行稳定性 | 6 | 10 |
| **Total** | **73** | **100** |

## Detailed findings

# UZI-Skill · Equity Research 类第 6 个首轮试用

- 上游：[`wbh604/UZI-Skill`](https://github.com/wbh604/UZI-Skill)，源码 `650788c54a9b2e042bf7f983f16dbf8d727fce1d`、CLI 自报 v3.9.4。隔离 Python 环境执行 `AAPL --depth lite --no-browser`；没有 MX_APIKEY、没有登录态、没有 Cloudflare 公网暴露。产物复制到本轮试用档案，供本机只读浏览；此试验**不是**全量 deep 档的 66 位评审 agent role-play。
- 定位：A／港／美多市场个股分析 CLI＋Agent Skill，带网页报告、评分、机构模型与分享图；不连接券商下单。其自身区分 lite/medium 规则直跑与 deep 人工/agent 介入。
- 证据：完整 CLI 运行日志保留在本地试用档案 是完整 CLI 日志；质量对账结果已纳入本页判断 将真实输出与原始缓存 `_data_gaps.json`、`raw_data.json`、`synthesis.json` 对账；本轮生成的 AAPL 报告已通过 49 张截图记录 是**本轮实际生成**的自包含 AAPL 报告。分享卡和战报也实际生成。[截图清单](screenshots.md)保存 **49 个不同证据图**：47 张报告页面与 2 张本轮生成的分享卡、战报。

实际跑通：采集波次约 97 秒后，脚本完成评分、HTML 组装和 PNG 分享卡，CLI exit 0。报告使用的 AAPL 价格 **$341.07** 与 Data 类和 MaverickMCP 的 2026-09-25 收盘样本一致；页面在顶部显示“已休市”、已知数据缺口、覆盖率 **72%**。多流派评论、风险、机构模型和可展开的维度卡都有真实生成的结构，而非截图模板。

质量门没有跟上输出力度：本轮 `_data_gaps.json` 明确 `critical_missing=true`，5 个字段未补，包括 ROE 历史、估值分位、护城河评分和行业增速；6 个定性维度在运行日志中记为兜底失败；最初机构建模 dim 20/21/22 还出现 `AttributeError`，虽后续仍写出模型结果。`agent_analysis.json` 缺失，`synthesis.agent_reviewed=false`；自检仍有 3 个 warning，包括未证实的行业景气度、缺 agent 分析和 Apple 产业链描述的证据不足。报告却仍显示精确的买入、止损、目标价数字，这些不能视作已核验投资行动建议。

两处可复验的一致性错误：报告宣称“Agent 已尝试浏览器抓取 / MX API / WebSearch / 逻辑推导”，同一次 lite 日志却明确 `Playwright skip`、`MX_APIKEY` 未设置、`ddgs` 预算 0；这是通用文案与执行事实不符。对美国股票 AAPL，网页现价用 **$341.07**，而模型执行摘要把目标价和现价写成 **¥272.86 / ¥341.07**；原始财务维度已有 `roe='148.8%'`，模型摘要却称“最新 ROE 0.0%”。币种与缺失值映射直接影响结论可信度。

体验边界：自包含网页可浏览和分享，画面覆盖丰富；切换暗色主题后有白底卡片文字变得接近白色、对比度不足。阶段判断是“**报告生成能力强，但本轮结果不能按深度研究已通过来使用**”：lite 在关键缺口和事实矛盾存在时仍输出强烈的精确价位，需先修来源回执文案、跨市场币种、缺失值映射和动作门禁。Equity Research 类全部测完后统一评分。
