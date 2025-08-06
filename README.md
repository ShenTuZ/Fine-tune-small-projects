# 微调模型聊天界面

这是一个简单的 Web 应用，允许您通过网页界面与您的微调模型进行交互。

## 功能特性

- 简洁美观的聊天界面
- 实时流式响应显示
- 支持 Enter 键快速发送消息

## 安装依赖

在运行应用之前，请确保安装所需的依赖包：

```bash
pip install -r requirements.txt
```

## 配置

在 `app.py` 文件中，您需要更新以下配置：

1. 将 `api_key` 替换为您从 [硅基流动用户系统](https://cloud.siliconflow.cn/account/ak获取) 获取的实际 API 密钥。
2. 将 `model` 参数替换为您实际训练好的微调模型名称。

## 运行应用

运行以下命令启动 Web 服务器：

```bash
python app.py
```

应用将在 `http://127.0.0.1:5000` 上运行。打开浏览器并访问该地址即可开始与您的微调模型聊天。

## 使用说明

1. 在输入框中输入您的问题或消息。
2. 点击“发送”按钮或按 Enter 键发送消息。
3. 模型的回答将实时显示在聊天历史中。

## 文件结构

- `app.py`: 后端 Flask 应用程序
- `templates/index.html`: 前端 HTML 模板
- `requirements.txt`: 项目依赖列表
- `convert_to_chat_jsonl.py`: 数据转换脚本（与本应用无关）

## 技术栈

- 后端：Python, Flask
- 前端：HTML, CSS, JavaScript
- API：OpenAI 兼容接口

## 上传到 GitHub

要将此项目上传到 GitHub，请按照以下步骤操作：

1. 在 GitHub 上创建一个新的仓库
2. 在本地项目目录中初始化 Git：
   ```bash
   git init
   ```
3. 添加所有文件到 Git：
   ```bash
   git add .
   ```
4. 提交更改：
   ```bash
   git commit -m "Initial commit"
   ```
5. 将本地仓库与 GitHub 仓库关联：
   ```bash
   git remote add origin https://github.com/yourusername/your-repo-name.git
   ```
6. 推送到 GitHub：
   ```bash
   git push -u origin main
   ```

确保在执行这些命令之前已经安装了 Git。