# 演示 列表嵌套
# 说明: 容器内部嵌套容器方式
# 需求: 有 三个班级, 分别为 大模型1班 大模型 2班  Java1班, 每个班级分别有5位学生
# 定义 班级列表
llm_class1 = ['张三','李四','王五','赵六','田七']
llm_class2 = ['周八','李九','老张','老李','老王']
java_class1 = ['小赵','小田','小周','小李','小王']

# 定义 学校列表, 学校列表中有三个班级
school_list = [llm_class1,llm_class2,java_class1]

# 以上内容 如果直接使用列表嵌套写法
school_list = [
    ['张三','李四','王五','赵六','田七'],
    ['周八','李九','老张','老李','老王'],
    ['小赵','小田','小周','小李','小王']
]

# 如何 获取里面的数据呢?  比如 我想获取到 老李
llm_class2 = school_list[1]
name = llm_class2[3]
print(name)

# 可以简写
name = school_list[1][3]
print(name)

# 如何遍历打印每一个元素
for classes in school_list:
    for name in classes:
        print(name)
    print("-----------")