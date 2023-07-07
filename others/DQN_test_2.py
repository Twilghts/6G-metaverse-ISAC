import numpy as np
import tensorflow as tf

if __name__ == '__main__':
    # 定义输入形状
    input_shape = (3, 6)

    # 定义输入层
    inputs = tf.keras.Input(shape=input_shape)
    # 展平输入
    inputs_flat = tf.keras.layers.Flatten()(inputs)
    print(inputs_flat)

    # 用于深度q学习模型的神经网络
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(3, 6)))
    model.add(tf.keras.layers.Dense(18, units=64, activation=tf.nn.relu))
    # model.add(tf.keras.layers.Dense(128, input_dim=3, activation='relu'))
    model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(learning_rate=0.001))
    # 假设我们有一个3x6的二维列表
    my_list = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18]
    ]
    result = model(np.array(my_list))
    print(result)