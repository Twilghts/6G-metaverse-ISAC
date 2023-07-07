from scipy.stats import norm
from scipy.optimize import root
import numpy as np

# 正态分布的均值和标准差
mean = 0
std_dev = 1

# 给定的概率密度函数值
target_pdf = 0.15


# 定义目标函数
def objective(_x):
    return norm.pdf(_x, loc=mean, scale=std_dev) - target_pdf


def calculate_area(_x):
    return norm.cdf(_x, loc=mean, scale=std_dev) - \
        norm.cdf(-_x, loc=mean, scale=std_dev) - \
        norm.pdf(_x, loc=mean, scale=std_dev) * 2 * _x


# 将初始估计值包装在数组中
x0 = np.array([0])

# 使用 root 函数求解目标函数的根
sol = root(objective, x0)

if sol.success:
    x = sol.x[0]
    print("x =", x)
    # print(f"累计值:{}")
    print(f"面积:{calculate_area(-x)}")
else:
    print("无法找到解")

print(norm.pdf(0, 0, 1))