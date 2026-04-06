def generate_func():
    for i in range(1_0000):
        print(f"正在生成{ i + 1}个")
        yield i

g2 = generate_func()
print(g2)
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))

for item in g2:
    print(item)