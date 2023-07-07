import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# 创建标准正态分布对象
norm_dist = stats.norm()

# 直线的方程
c = 0.2

# 计算直线与标准正态分布曲线的交点
x1 = norm_dist.ppf(0.001)
x2 = norm_dist.ppf(0.999)

# 创建 x 值的范围
x = np.linspace(x1, x2, 1000)

# 创建标准正态分布的概率密度函数（PDF）
y = norm_dist.pdf(x)

# 绘制标准正态分布曲线
plt.plot(x, y)

# 绘制直线
plt.axhline(c, color='red')

# 填充被直线截得的面积
plt.fill_between(x, y, where=(y > c), color='gray', alpha=0.5)

# 显示图形
plt.show()
