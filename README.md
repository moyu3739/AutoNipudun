# AutoNipudun 自动充电系统

这是一个通过 GitHub Actions 在指定时间自动执行充电操作的项目。

## 设置步骤

1. Fork 本仓库到你的 GitHub 账号
2. 在仓库设置中添加以下 Variables:
   - `DEV_ADDR`: 设备地址（8 位数）
   - `DEV_PORT`: 设备端口（两位数，1-9 号端口需在前补零）
3. 在仓库设置中添加以下 Secrets:
   - `COOKIE_JSESSIONID`: 登录 cookie（目前只能通过抓包获得）

## 工作流程

工作流默认设置为每天早上 7:30（北京时间）自动执行充电操作。你也可以在 Actions 页面手动触发工作流。

## 本地运行

如果需要本地运行，可以设置环境变量：

```bash
export DEV_ADDR="你的设备地址"
export DEV_PORT="你的设备端口"
export COOKIE_JSESSIONID="你的Cookie"
python src/AutoNipudun.py
```

或修改配置文件 `config.json`：
```json
{
   "dev_addr": "你的设备地址",
   "dev_port": "你的设备端口",
   "cookie_jsessionid": "你的Cookie"
}
```
