import numpy as np
import matplotlib.pyplot as plt

# 创建 x 值范围
x2 = np.linspace(0, 0.1, 400)   # 第二个分段区间：0 到 2
x3 = np.linspace(0.1, 2, 400)   # 第三个分段区间：2 到 4

# 定义二次函数 y = ax^2 + bx + c 的系数
a = 80
b = - 16
c = 1
# 计算每个分段上的 y 值
y2 = a * x2 ** 2 + b * x2 + c
y3 = 1 / (50 * x3)

# 创建图形
plt.figure(figsize=(8, 6))

# 绘制每个分段的图像
plt.plot(x2, y2, label='f(x) = a * x2 ** 2 + b * x2 + c (0 <= x < 0.1)')
plt.plot(x3, y3, label='f(x) = 1 / (50 * x3) (x >= 0.2)')

# 添加标题和标签
plt.title('分段函数图像')
plt.xlabel('x')
plt.ylabel('f(x)')

# 添加图例
plt.legend()

# 显示图像
plt.grid(True)
plt.show()
