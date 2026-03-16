# 案例：用for循环实现用户登录
#
# ① 输入用户名和密码
#
# ② 判断用户名和密码是否正确（username='admin'，password='admin888'）
#
# ③ 登录仅有三次机会，超过3次会报错

for i in range(0,3):
    username = input("输入用户名")
    password = input("输入密码")
    if username == 'admin':
        if  password == 'admin888':
            print("success")
            break
        else:
            print(f"password fail, 你还有{2-i}次机会")
    else:
        print(f"username fail, 你还有{2-i}次机会")



