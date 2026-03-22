# 接收用户输入的账号和密码，如果账号为'admin'，密码为'admin888'，则提示用户登录成功，
# 其他情况则提示用户名或密码输入错误，只有3次输入机会。

i = 0
while i < 4:
    if i == 3:
        print("次数用完，请联系管理员")
        break
    username = input("请输入用户账号")
    password = input("请输入用户密码")
    if username == "admin" and password == "admin888":
        print("登录成功")
        break
    elif username != "admin":
            i = i + 1
            print(f"用户名不正确,你还有{3-i}次机会")
    elif password != "admin888":
            i = i + 1
            print(f"密码不正确,你还有{3-i}次机会")



