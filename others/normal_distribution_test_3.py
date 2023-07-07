import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 创建正态分布对象
norm_dist = stats.norm()

# 直线方程
c = 1

# 计算交点
y1 = norm_dist.pdf(c)

# 创建 y 值的范围
y = np.linspace(0, y1, 1000)

# 创建正态分布的横坐标范围
x = norm_dist.ppf(y)


# 计算被曲线和直线所围成的面积
def integrand(y):
    return norm_dist.pdf(norm_dist.ppf(y)) - norm_dist.pdf(c)


area, _ = quad(integrand, 0, y1)

# 绘制正态分布曲线
plt.plot(x, y)

# 绘制直线
plt.axvline(x=c, color='red')

# 显示图形
plt.show()

print("被直线截得的面积: ", area)
