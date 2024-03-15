import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 生成模拟数据
num_steps = 10
input_size = 3
hidden_size = 3

# 随机生成输入序列和目标序列
input_sequence = np.random.randn(1, num_steps, input_size).astype(np.float32)
target_sequence = np.array([6*n for n in input_sequence])

# 定义LSTM模型
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(hidden_size, return_sequences=True),
])

# 定义损失函数和优化器
loss_fn = tf.keras.losses.MeanSquaredError()
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001, clipvalue=1.0)  # 调整 clipvalue 的值

# 编译模型
model.compile(optimizer=optimizer, loss=loss_fn)

# 记录每个epoch的损失
losses = []

# 执行训练过程
epochs = 300

for epoch in range(epochs):
    # 在每个epoch中遍历训练序列
    for step in range(num_steps):
        x = input_sequence[step:step+1, :]
        target = target_sequence[step:step+1, :]

        # 前向传播
        with tf.GradientTape() as tape:
            predicted_sequence = model(input_sequence, training=True)
            loss = loss_fn(target, predicted_sequence)

        # 计算梯度并更新参数
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    average_loss = loss.numpy()
    losses.append(average_loss)
    print(f"Epoch {epoch + 1}/{epochs}, Loss: {average_loss}")

# 绘制损失值的图表
plt.plot(losses)
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training Loss Over Epochs')
plt.show()
