import matplotlib.pyplot as plt

# 示例数据
x_data = [1, 2, 3, 4]
y1_data = [1, 5.6596 / 2.9386 / 2, 5.6596 / 2.9405 / 3, 5.6596 / 2.1835 / 4]
y2_data = [1, 2.7235 / 2.2075 / 2, 2.7235 / 1.5542 / 3, 2.7235 / 1.1717 / 4]
y3_data = [1, 1.7112 / 1.0765 / 2, 1.7112 / 0.7878 / 3, 1.7112 / 0.4255 / 4]
y4_data = [1, 6.8663 / 5.3701 / 2, 6.8663 / 3.0783 / 3, 6.8663 / 2.3086 / 4]

# 创建图形和坐标轴
plt.figure(figsize=(8, 6))
plt.plot(x_data, y1_data, label='2048', marker='o')
plt.plot(x_data, y2_data, label='4096', marker='s')
plt.plot(x_data, y3_data, label='8192', marker='^')
plt.plot(x_data, y4_data, label='16384', marker='D')

# 添加标题和标签
plt.title('矩阵规模和进程数量与效率的关系')
plt.xlabel('进程数量')
plt.ylabel('加速比')

# 添加图例
plt.legend()

# 显示图形
plt.show()
