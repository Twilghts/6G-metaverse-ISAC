import numpy as np
import matplotlib.pyplot as plt

# 创建 x 值范围
x = np.linspace(0, 0.1, 100)  # 生成从-10到10的400个均匀分布的点

# 定义二次函数 y = ax^2 + bx + c 的系数
a = 80 / 3
b = - 16 / 3
c = 1

# 计算对应的 y 值
y = a * x ** 2 + b * x + c

# 创建图形
plt.figure(figsize=(8, 6))

# 绘制二次函数的图像
plt.plot(x, y, label='y = {}x^2 + {}x + {}'.format(a, b, c))

# 添加标题和标签
plt.title('二次函数图像')
plt.xlabel('x')
plt.ylabel('y')

# 设置纵横比为1，使y轴和x轴的单位长度相等
plt.axis('equal')
# 添加图例
plt.legend()

# 显示图像
plt.grid(True)
plt.show()
