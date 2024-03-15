import random

step = 10000  # 设置迭代次数为10000
x0 = random.randint(-10, 10)  # 随机初始化一个数值
lr = 0.001  # 设置学习率为0.001
for i in range(step):
    x1 = x0 - lr * (-10 + 2 * x0)  # 梯度下降迭代
    x0 = x1
print('梯度下降法求解结果：', x0)
