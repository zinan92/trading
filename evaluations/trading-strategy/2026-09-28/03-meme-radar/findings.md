# Meme Radar · 首轮试用记录

## 类内评分：第 8 名 · 58/100

| 核心结果实测 | 数据可信度与时效 | 覆盖与深度 | 上手与复现 | 运行稳定性 | 总分 |
|---:|---:|---:|---:|---:|---:|
| 15/35 | 10/25 | 11/15 | 13/15 | 9/10 | **58/100** |

**建议定位：多链 Meme 候选发现与风险复核。** 评分依据：安装、doctor 与 360 项测试通过；无 AVE Key 时核心候选扫描不可用，UI 显示清晰授权空态。


**上游：** `nhovongoc0-max/meme-radar` · commit `dbe1fa27cb5735c6fb7b6060ef80bae4f06cc7b6` · v0.1.10 · `AGPL-3.0-only`。

## 实际安装与使用

- `npm run setup` 和 `npm run doctor` 均通过；Node v26.8.1 满足项目要求。`npm test`：360 passed，0 failed，0 skipped。测试是本地自动化测试，不等于 AVE 实际扫描结果。
- README 声明这是本地只读多链 Meme 候选雷达；核心行情来自 AVE。由于用户没有 AVE API Key，本轮将 key 留空。
- 使用应用自己的 Node 入口在 `127.0.0.1:3981` 启动。健康接口返回 HTTP 200，但状态是 `ready=false`、`degraded=true`、`AVE_AUTH_REQUIRED`、`execution=false`。网页显示“尚无成功数据 / 等待授权”，候选数 0。
- 点空白 AVE Key 的“保存 / 测试”仅返回本地 `400 AVE_KEY`；启动进程和浏览器都加了外网拦截，外部请求数为 0。候选页、5 条链选择、过滤选项、授权设置、额度说明、连接诊断、语言和窄屏 UI 均可看。
- 无 key 时不能扫描真实行情。**空列表是因缺少授权，不是扫描通过，也不是市场没有候选。** 本轮没有伪造行情、风险分或收益。

## 判断与定位

**定位建议：** `Trading Strategy / 只读多链 Meme 候选发现与风险筛选雷达`。它有真实可启动的本地 UI、链选择、数据授权控制、预算展示和清晰空态；但没有 AVE Key 时无法验证核心扫描结果。源码明确不包含钱包私钥、签名、swap 或下单接口，因此不是交易执行系统。

本轮验证了安装、健康页、无 key 空态和本地授权表单；未验证 AVE 连接、候选发现、合约/LP 深审、K 线行为过滤或影子表现。

证据：[本地界面截图图库](evidence/index.html) · [健康状态](evidence/health.json) · [测试和外呼摘要](evidence/verification.json) · [截图清单](screenshots.md)。
