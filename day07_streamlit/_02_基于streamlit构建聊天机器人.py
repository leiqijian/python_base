# 1- 导入 streamlit的包
import streamlit as st

# 2- 构建聊天界面
# 2.1 添加标题
st.title('智聊机器人')

# 2.2 添加一条横线
st.divider()

# 2.3 设置欢迎词
st.chat_message('assistant').write('你好,我是智聊机器人, 有什么可以帮助您的吗!')


# 2.4 用户输入的框
prompt = st.chat_input('请输入您的问题')

# 2.5 将用户输入的内容写入到聊天区中
if prompt:
    st.chat_message('user').write(prompt)
    # 2.6 调用AI大模型, 获取机器人返回结果
    st.chat_message('assistant').write('我是智聊机器人,很高兴为您服务!') # 替换为大模型结果