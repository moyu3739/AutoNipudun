# AutoNipudun 自动充电系统

这是一个通过 GitHub Actions 在指定日期自动执行充电操作的项目。

## 设置步骤

1. Fork 本仓库到你的 GitHub 账号
2. 在仓库设置中添加以下 Variables:
   - `DEV_ADDR`: 设备地址（8 位数）
   - `DEV_PORT`: 设备端口（两位数，1-9 号端口需在前补零）
   - `TARGET_DATE`: 目标执行日期，格式为 YYYY-MM-DD（例如：2023-12-31）
3. 在仓库设置中添加以下 Secrets:
   - `COOKIE_JSESSIONID`: 登录 cookie（目前只能通过抓包获得）

## 工作流程

工作流会在每天早上 6:01（北京时间）触发，但只有当前日期与设定的目标日期（`TARGET_DATE`）匹配时，才会实际执行充电操作。你也可以在 Actions 页面手动触发工作流。

## 本地运行

如果需要本地运行，可以设置环境变量：

```bash
export DEV_ADDR="你的设备地址"
export DEV_PORT="你的设备端口"
export COOKIE_JSESSIONID="你的Cookie"
export TARGET_DATE="目标日期，格式为 YYYY-MM-DD"
python src/AutoNipudun.py
```

或在 `src` 目录中添加配置文件 `config.json`：
```json
{
   "dev_addr": "你的设备地址",
   "dev_port": "你的设备端口",
   "cookie_jsessionid": "你的Cookie",
   "target_date": "目标日期，格式为 YYYY-MM-DD"
}
```
