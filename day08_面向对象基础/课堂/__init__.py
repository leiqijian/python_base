class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """用户友好的字符串表示"""
        return f"我叫{self.name}，今年{self.age}岁"

    def __repr__(self):
        """开发者友好的字符串表示，最好能重建对象"""
        return f"Person('{self.name}', {self.age})"


# 创建对象
p = Person("张三", 25)

# 测试 __str__
print("=" * 50)
print("测试 __str__")
print("=" * 50)
print(str(p))  # 我叫张三，今年25岁
print(f"{p}")  # 我叫张三，今年25岁
print(p)  # 我叫张三，今年25岁

# 测试 __repr__
print("\n" + "=" * 50)
print("测试 __repr__")
print("=" * 50)
print(repr(p))  # Person('张三', 25)
print(f"{p!r}")  # Person('张三', 25)  (!r 强制使用 repr)

# 交互式环境
print("\n" + "=" * 50)
print("交互式环境行为")
print("=" * 50)
# 在 Jupyter/IPython 中直接输入 p 会调用 __repr__
# 在列表等容器中也会使用 __repr__
print([p])  # [Person('张三', 25)]