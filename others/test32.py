import matplotlib.pyplot as plt

# 示例数据
x_data = [1000, 2000, 3000, 4000]
y1_data = [2.629, 3.862, 11.615, 27.793]
y2_data = [2.625, 3.195, 9.74, 21.766]
y3_data = [3320, 26937.43, 89640, 263587.891]

# 创建图形和坐标轴
plt.figure(figsize=(8, 6))
plt.plot(x_data, y1_data, label='Kernel1', marker='o')
plt.plot(x_data, y2_data, label='Kernel2', marker='s')
plt.plot(x_data, y3_data, label='CPU time', marker='^')

# 添加标题和标签
plt.title('矩阵规模和CPU/Kernel1/Kernel2 time之间的关系')
plt.xlabel('矩阵规模')
plt.ylabel('运行时间/ms')

# 添加图例
plt.legend()

# 显示图形
plt.show()
