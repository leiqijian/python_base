# 智聊机器人的前台界面程序
# 1- 导入相关的库: streamlit  后台服务模块
import streamlit as st
from itcast_assistant_backend import get_chat_response
# 2- 设置页面
# 2.1 设置标题
st.title('Leimen智聊机器人')

# 2.2 添加一条横线 用于分割
st.divider()


# ======================保存聊天对话记录 Start ==============================
if 'messages' not in st.session_state:
    # 如果能进来, 说明 在会话记录中压根没有任何的消息记录
    # 初始化一个空的用于保存对话的 列表
    st.session_state['messages'] = []
    # 设置欢迎语句
    st.session_state['messages'].append({'role':'assistant','content':'你好，我是Leimen，有什么可以帮助您的吗！'})

# 遍历对话列表 用于恢复对话信息
for message in st.session_state['messages']:
    st.chat_message(message['role']).write(message['content'])

# ======================保存聊天对话记录 end  ==============================

# 2.4 设置用户输入的聊天框：
prompt = st.chat_input("请输入您的问题：")
print(prompt)

if prompt:
    # 说明用户已经输入了内容
    # 2.5 将用户输入的内容写入到聊天区
    st.chat_message('user').write(prompt)

    #TODO 将用户输入的内容, 写入到聊天对话记录容器中
    st.session_state['messages'].append({'role': 'user', 'content': prompt})

    # 2.6 将提示词给到ollama后台服务,拿到大模型返回的结果
    with st.spinner("正在思考中,请稍后......"): # 增加用户感受
        content = get_chat_response(prompt)

    # 2.7 将获取的结果内容返回
    st.chat_message('assistant').write(content)

    #TODO 将机器人返回的聊天内容, 保存到聊天对话记录容器中
    st.session_state['messages'].append({'role': 'assistant', 'content': content})