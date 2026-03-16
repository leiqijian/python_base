# range(stop)
# range(start, stop[, step])
#
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0，5） 是 [0, 1, 2, 3, 4] 没有 5
# step：步长，默认为1。例如：range（0，5） 等价于 range(0, 5, 1)

# 演示 range函数
# 作用: 帮我们生成一个连续的数字, 例如 0~10
# 语法:  range(起始值,结束值,步长)
#  起始值: 默认为  0   结束值: 必填的  在生成序列的时候, 不含结束值  步长: 默认为1 表示 数字与数字之间的间隔
# 需求: 生成 5以内的序列, 并且将每一个值打印出来
for e in range(0,5):
    print(e)

# 使用for循环，求1 ~ 100之间所有偶数的和
sum = 0

for e in range(0,101):
    if e % 2 == 0:
        sum = sum + e
print(sum)