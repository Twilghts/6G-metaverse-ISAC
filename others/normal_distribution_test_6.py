import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 正态分布的均值和标准差
mean = 0
std_dev = 1

# 生成一组 x 值
x = np.linspace(-4, 4, 100)

# 计算对应 x 值处的概率密度函数值
pdf_values = norm.pdf(x, loc=mean, scale=std_dev)

# 绘制概率密度函数图形
plt.plot(x, pdf_values)
plt.xlabel('x')
plt.ylabel('PDF')
plt.title('Normal Distribution PDF')
plt.grid(True)
plt.show()
