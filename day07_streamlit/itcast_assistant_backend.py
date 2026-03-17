# 访问ollama后台服务
# 1- 导入ollama库
import ollama

# 2- 构建一个函数, 传入用户输入的提示词, 返回大模型给出的结果
def get_chat_response(prompt:str):
    content = ''
    try:
        # 2.1 构建ollama的客户端
        client = ollama.Client(host='http://127.0.0.1:11434')

        # 2.2 通过客户端向ollama发起请求获取大模型的结果
        response = client.chat(model='qwen2:1.5b',messages=[{'role':'user','content':prompt}])

        # 2.3 返回响应的消息内容
        content = response.message.content
    except:
        # 出现未知的异常
        content = '服务器繁忙, 请稍后尝试......'
    finally:
        return content


# 测试:
if __name__ == '__main__':
    content = get_chat_response("人工智能的发展如何呢?")
    print(content)