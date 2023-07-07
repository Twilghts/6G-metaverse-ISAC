import matplotlib.pyplot as plt
import numpy as np

import emoji

print(emoji.emojize(' :合:', language='zh'))

# 生成正态分布的数据
x = np.linspace(-4, 4, 100)  # x轴的取值范围
y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x ** 2)

# 绘制图像
plt.plot(x, y, color='blue', linewidth=2)

# 设置图像标题和轴标签
plt.title('Standard Normal Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')

# 显示图像
plt.show()
