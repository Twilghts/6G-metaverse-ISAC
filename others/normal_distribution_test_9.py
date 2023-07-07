import time

from scipy.stats import norm
import numpy as np

# 正态分布的均值和标准差
std_dev = 1


def calculate_area(_y):
    if _y >= norm.pdf(0, 0, std_dev):
        return 0
    elif _y <= 0:
        return 1
    else:
        _x = np.sqrt(-2 * np.square(std_dev) * np.log(np.sqrt(2 * np.pi) * std_dev * _y))
        return norm.cdf(_x, 0, std_dev) - \
            norm.cdf(-_x, 0, std_dev) - 2 * \
            _x * norm.pdf(_x, 0, std_dev)


# print(calculate_area(0.35))
start_time = time.perf_counter()
for i in range(10000):
    calculate_area(0.15)
print(time.perf_counter() - start_time)

# 计算以 e 为底数的对数值
x = np.array([1, 2, 3])  # 输入数组
log_values = np.log(x)

print("Natural logarithm values:", log_values)

# 计算平方根
y = np.array([4, 9, 16])  # 输入数组
sqrt_values = np.sqrt(y)

print("Square root values:", sqrt_values)
