# OctoBot · Trading Infra 首轮试用记录

## Trading Infra 类内评分：第 6 名 · 30/100

| 核心结果实测 | 数据可信度与时效 | 覆盖与深度 | 上手与复现 | 运行稳定性 | 总分 |
|---:|---:|---:|---:|---:|---:|
| 5/35 | 5/25 | 9/15 | 7/15 | 4/10 | **30/100** |

**评分依据：** package/CLI install works, but clean simulated UI cannot start because default tentacles are unavailable as a verifiable signed package; no trading workflow was proven.


**定位建议：独立加密自动交易机器人 / Full Trading System，当前 commit 显示 Beta。** 它的产品自述包括 UI、DCA/Grid、TradingView、AI 与 15+ 交易所；本轮没有把 README 功能当成通过证据。Trading Infra 类内分数待本类最后统一评定。

## 安装与 CLI

按 catalog 锁定 commit `d63148e57627ea622fb14401bfe778d1a9b06183` 安装 `OctoBot 3.0.0-beta2` 到隔离 Python 3.13 环境。默认解析需要 prerelease 依赖；无 `--prerelease=allow` 时 PyPI 解不出 `starfish-protocol==3.0.0a29`，加上允许预发行后 199 个依赖成功解析/安装。`OctoBot --version` 和 `OctoBot --help` 可用，CLI 有 `--simulate`、`--standalone`、`--user-folder` 等选项。

## 首次模拟 UI 启动阻断

使用全新 trial 用户目录，以 standalone + simulator + no Telegram 模式启动。OctoBot 发现缺少 default tentacles 和 profile。公开默认 tentacles ZIP（约 2.93 MB）下载成功；tentacles manager 的默认签名校验拒绝该 bundle，因为相邻 `.signature` 文件缺失；检查同源签名 URL 返回 HTTP 404。OctoBot 随后报告缺少 default profile，因此 Web UI 没有启动，`5001/18501` 没有监听。

程序建议用 `ALLOW_UNSIGNED_TENTACLES=true` 绕过；本轮没有采用该方式，保留完整性门。模拟模式虽不需要交易所 API key，但干净部署仍被这个插件包签名路径挡住。通过静态参数/市场配置或 README 截图无法替代产品实际运行。

## 边界

没有配置或读取交易所 API key、账户，没有请求交易所行情、没有启动 Docker、没有下单。OctoBot 发布仓库的 Docker entrypoint 会调用 `tunnel.sh`；该脚本只在提供 Cloudflare token 时启动 tunnel，本轮完全没有运行 Docker。

因此本轮只验证了 Python 安装、CLI 和安全失败路径；**DCA/Grid、模拟撮合、回测、Web UI、15+ 交易所连接均未验证**。17 张截图里大部分是锁定源码/官方说明页面，另有 CLI/help 与签名阻断的辅助截图；不是 live UI。

[17 张截图](screenshots.md) · [机器可读启动结果](verification.json)
