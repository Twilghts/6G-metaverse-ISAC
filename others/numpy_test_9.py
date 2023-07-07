import numpy as np
import matplotlib.pyplot as plt

# 设置均值和标准差
mu = 0  # 均值
sigma = 1 / np.sqrt(2 * np.pi)  # 标准差

# 生成一组随机数，服从正态分布
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)  # 生成一组从（均值-3倍标准差）到（均值+3倍标准差）的等间隔数据
y = (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)  # 正态分布的概率密度函数

# 绘制正态分布曲线
plt.plot(x, y)
plt.title('Normal Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()
router_storage = [19060, 8763, 16297, 22901, 13735, 13530, 21507, 19683, 3692, 22855, 28427, 12424,
                  13628, 12968, 22011, 10952]
router_storage.sort()
print(router_storage)

router_calculate = [143, 167, 115, 196, 168, 135, 186, 53, 151, 47, 116, 107, 83, 80, 135, 165]
router_calculate.sort(reverse=True)
print(router_calculate)