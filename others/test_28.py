import numpy as np
import matplotlib.pyplot as plt

# 步骤2：创建时间点和函数f(t)
t = np.linspace(0, 10, 1000)  # 时间范围从0到10，创建1000个时间点
f_t = np.exp(-t) * (t >= 0)  # 函数f(t) = e^(-t) * Θ(t)，Θ(t)是单位阶跃函数

# 步骤3：使用傅里叶变换计算频谱
F = np.fft.fft(f_t)  # 计算傅里叶变换

# 步骤4：计算幅度谱和相位谱
magnitude_spectrum = np.abs(F)  # 幅度谱
phase_spectrum = np.angle(F)    # 相位谱

# 步骤5：绘制幅度谱
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, f_t)
plt.title('原始信号')

plt.subplot(2, 2, 3)
plt.plot(t, magnitude_spectrum)
plt.title('幅度谱')

plt.subplot(2, 2, 4)
plt.plot(t, phase_spectrum)
plt.title('相位谱')

plt.tight_layout()
plt.show()
