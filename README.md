# AutoNipudun 自动充电系统

这是一个通过 GitHub Actions 在指定时间自动执行充电操作的项目。

## 设置步骤

1. Fork 本仓库到你的 GitHub 账号
2. 在仓库设置中添加以下 Secrets:
   - `DEV_ADDR`: 设备地址
   - `DEV_PORT`: 设备端口
   - `COOKIE_JSESSIONID`: 登录 cookie
   
## GitHub Secrets 设置方法

1. 进入你的仓库
2. 点击 "Settings" 选项卡
3. 在左侧导航栏中点击 "Secrets and variables" -> "Actions"
4. 点击 "New repository secret" 按钮
5. 添加上述三个 secret

## 工作流程

工作流默认设置为每天早上 7:30 (北京时间) 自动执行充电操作。你也可以在 Actions 页面手动触发工作流。

## 本地运行

如果需要本地运行，可以设置环境变量或直接修改脚本中的默认值：

```bash
export DEV_ADDR="你的设备地址"
export DEV_PORT="你的设备端口"
export COOKIE_JSESSIONID="你的Cookie"
python src/AutoNipudun.py
```
