import numpy as np
import matplotlib.pyplot as plt

# 创建 _t 值范围，避免包含0以避免除以零错误
x = np.linspace(0.1, 2, 100)  # 生成从0.01到5的400个均匀分布的点

# 计算对应的 y 值
y = 1 / (50 * x)

# 创建图形
plt.figure(figsize=(8, 6))

# 绘制反比例函数的图像
plt.plot(x, y, label='y = 1/_t')

# 添加标题和标签
plt.title('反比例函数图像')
plt.xlabel('_t')
plt.ylabel('y')

# 添加图例
plt.legend()

# 显示图像
plt.grid(True)
plt.show()
