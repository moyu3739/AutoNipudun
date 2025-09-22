# 使用 trigger 分支触发充电脚本

本项目设置了一个专用的 `trigger` 分支，用于通过简单的推送操作来触发自动充电脚本。

## 使用方法

1. 首次设置：如果 `trigger` 分支不存在，需要先创建它

   ```bash
   # 基于主分支创建 trigger 分支
   git checkout main
   git checkout -b trigger
   git push -u origin trigger
   ```

2. 每次需要手动触发脚本时，执行以下命令：

   ```bash
   # 切换到 trigger 分支
   git checkout trigger
   
   # 创建一个空提交
   git commit --allow-empty -m "触发自动充电脚本 - $(date)"
   
   # 推送到远程仓库
   git push origin trigger
   ```

3. 推送完成后，GitHub Actions 将自动执行充电脚本

## 其他触发方式

除了通过 `trigger` 分支触发外，脚本还可以通过以下方式触发：

- 每天早上 7:30 自动执行（通过 cron 计划任务）
- GitHub 网页界面中手动触发（通过 Actions 页面的 workflow_dispatch）

## 提示

在使用 `trigger` 分支触发脚本前，请确保已正确设置了所需的 GitHub Variables 和 Secrets。
