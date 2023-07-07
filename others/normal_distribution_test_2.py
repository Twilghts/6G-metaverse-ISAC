import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 创建正态分布对象
norm_dist = stats.norm()

# 直线方程
m = 2
c = 1

# 计算交点
x1 = norm_dist.ppf(0.001)
x2 = norm_dist.ppf(0.999)
y1 = m * x1 + c
y2 = m * x2 + c

# 创建 x 值的范围
x = np.linspace(x1, x2, 1000)

# 创建正态分布的概率密度函数（PDF）
y = norm_dist.pdf(x)


# 计算被曲线和直线所围成的面积
def integrand(x):
    return norm_dist.pdf(x) - (m * x + c)


area, _ = quad(integrand, x1, x2)

# 绘制正态分布曲线
plt.plot(x, y)

# 绘制直线
plt.plot([x1, x2], [y1, y2], color='red')

# 显示图形
plt.show()

print("被直线截得的面积: ", area)
