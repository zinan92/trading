# trading-desk · 70/100 · 集成交易台 UI 模块

## 角色判断

该项目已于 2026-09-27 归档并迁入 zinan92/trading-system 的 apps/trading-desk。它是 Full Trading System 的交易台 UI 子模块，不能作为可独立部署的 Dashboard 产品重复计算。保留本目录仅为了完整评估 Dashboard catalog 条目，并标出它的归属。

## 本轮实际验证

- 沿用同一轮 trading-system 的隔离试用，不再启动第二份系统：/desk 与同源 /trade 可打开，health/assets/交易台只读导航端点响应正常。
- 本地隔离 SQLite 只含资产 fixture；市场 read model 明确 blocked、bar count 为 0，系统保持 stopped/fail-closed。
- GET-only 检查没有点击启动、确认、执行、平仓等写操作。没有 trusted market data 时，UI 外观和导航可验，成交、持仓、订单和策略执行结果不可验。
- 19 张唯一截图来自前一项集成试用，路径及其 SHA-256 保持一致；详细测试限制参见 [Trading Infra 的完整系统记录](../../../trading-infra/2026-09-28/03-trading-system/findings.md)。

## 五维评分

| 维度 | 分数 | 证据与限制 |
|---|---:|---|
| 核心结果实测 | 23/35 | 页面及只读 API 可用，市场读模型无数据，因此不能看到实盘/纸盘 K 线与交易结果 |
| 数据可信度与时效 | 19/25 | 空数据被标记 blocked，未伪装为模拟行情；暂无 trusted feed |
| 覆盖与深度 | 13/15 | Overview、System、订单、持仓、成交、复盘、Supervisor 等界面丰富 |
| 上手与复现 | 8/15 | 要从交易系统宿主启动，独立归档仓库不能单独安装运行 |
| 运行稳定性 | 7/10 | 隔离服务和主要 GET 路径正常；未接数据时核心面板无法形成交易工作流 |

## 结论

Dashboard 界面覆盖面很广，但整合运行和可信行情是主要边界。它的产品分类应跟随宿主，放在 **Full Trading System / Agent**，而不是作为独立 Dashboard 重复列入可部署工具排名。
