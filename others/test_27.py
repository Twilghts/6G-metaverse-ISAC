import matplotlib.pyplot as plt
import numpy as np


def element(_n, _t):
    value = 0
    start = - int(_n / 2)
    for _i in range(start, -start + 1):
        if _i == 0:
            value += 0.5
        else:
            value += (1 / (_i * np.pi)) * np.sin(_i * np.pi / 2) * np.exp(_i * np.pi * _t * 1j)
    return value


# 创建一个原始信号函数 f(_t)
t = np.linspace(-4, 4, 1000)
f_t = np.heaviside(t + 1, 0) - np.heaviside(t - 1, 0)

N = 7
t_values = np.linspace(-2, 2, 400)
fourier_series = []
for i in range(400):
    fourier_series.append(element(N, -2 + 0.01 * i))

# 绘制原始信号和三角形式的傅里叶级数展开
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, f_t)
plt.title('原始信号')

plt.subplot(2, 1, 2)
plt.plot(t_values, fourier_series)
plt.title(f'三角形式的傅里叶级数展开 (前{N}项)')

plt.show()
