from flask import Flask, render_template, request, jsonify, Response, session
import openai
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # 用于会话加密

# 配置OpenAI客户端
client = openai.OpenAI(
    api_key="your key",  # 从 `https://cloud.siliconflow.cn/account/ak获取`
    base_url="https://api.siliconflow.cn/v1"
)

@app.route('/')
def index():
    # 初始化会话中的消息历史
    if 'messages' not in session:
        session['messages'] = []
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': '消息不能为空'}), 400

    # 获取会话中的消息历史
    messages = session.get('messages', [])
    # 添加用户消息
    messages.append({"role": "user", "content": user_message})

    # 将用户消息添加到会话中
    session['messages'] = messages
    
    def generate():
        try:
            response = client.chat.completions.create(
                model="ft:LoRA/Qwen/Qwen2.5-72B-Instruct:eyyydwxlnn:JH1:qxoxkqzsreloevfarkma-ckpt_step_14",
                messages=messages,
                stream=True,
                max_tokens=4096
            )
            assistant_message = ""
            for chunk in response:
                content = chunk.choices[0].delta.content
                if content:
                    assistant_message += content
                    yield f"data: {content}\n\n"
            # 将助手的回复添加到消息历史中
            messages.append({"role": "assistant", "content": assistant_message})
            # 更新会话中的消息历史
            session['messages'] = messages
        except Exception as e:
            yield f"data: 错误: {str(e)}\n\n"
    
    return Response(generate(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)