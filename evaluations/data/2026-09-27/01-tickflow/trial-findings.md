# TickFlow · Data 类第 1 个首轮试用

- 原仓库：https://github.com/tickflow-org/tickflow
- 试用源码：`c27f23c50386c10f2c439cf8345e9aa2c295e0c7`，Python 包 `0.1.25`，与 Trading catalog 锁相同。
- 使用方式：本机隔离 Python 3.12 环境装 `tickflow[all]`；使用 `TickFlow.free()`，未登录、未使用 API key。项目本身是 Python SDK，**没有原生 Web 产品界面**。
- 证据：[`evidence/probes.json`](evidence/probes.json) 保存逐条真实输出与耗时；[`evidence/index.html`](evidence/index.html) 是 Product Lab 的辅助证据页；[`evidence/screenshots/`](screenshots.md) 有 12 张不同调用状态截图，均非 TickFlow 官方页面。

## 已实际通过

1. A 股浦发银行历史日 K（5 根）和沪深 300 ETF 历史日 K（5 根）；周 K（5 根）也返回。A 股最新返回日期为 **2026-09-24**。上海证券交易所公告明确 **9 月 25–27 日休市**，所以这不能被当成免费数据滞后的证据：[上交所公告](https://www.sse.com.cn/disclosure/announcement/general/c/c_20260915_10832273.shtml)。
2. 美股 AAPL 和港股腾讯历史日 K 各返回 5 根，最新市场日期均为 **2026-09-25**。A 股两标的批量查询成功。
3. A、ETF、美股、港股四种标的元数据批量查询成功；标的池列表返回 1015 个条目。异步 A 股历史日 K 返回 3 根。
4. 上述请求 0.42–2.29 秒返回。这里只测一次，不能推断持续可用性或高并发能力。

## 边界与未验证

- 免费入口访问分钟 K、实时行情均得到 `PermissionError`，与官方文档的免费额度边界一致。[官方仓库 README](https://github.com/tickflow-org/tickflow)。完整付费入口的实时、分钟、财务报表没有本轮凭证，不宣称可用或不可用。
- 本轮未做跨数据源价格对账、历史复权正确性或数据可用率测试。
- 推荐定位：**跨 A 股／ETF／美股／港股的历史行情和标的元数据 Python SDK；实时与分钟功能需另行验证授权入口**。它是数据接口，不是供交易员点击操作的 dashboard。

结论：免费历史数据在这次试用中好用，安装与调用直接，跨市场日 K 有实际输出。实时和分钟功能在无账号条件下无法验收。Data 类统一排名将在 14 个产品全部试完后给出。
