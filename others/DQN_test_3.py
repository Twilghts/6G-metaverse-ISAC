import tensorflow as tf

# 定义输入形状
hidden_units = 64
input_shape = (3, 6)
output_units = 10  # 假设输出有 10 个类别

# 定义输入层
inputs = tf.keras.Input(shape=input_shape)

# 展平输入
inputs_flat = tf.keras.layers.Flatten()(inputs)

# 添加全连接层
hidden_layer = tf.keras.layers.Conv2D(
    16, kernel_size=(8, 8), strides=(4, 4),
    padding="valid", activation='relu'
)(inputs_flat)

# 可选：添加更多全连接层
middle_layer = tf.keras.layers.Dense(units=hidden_units, activation=tf.nn.relu)(hidden_layer)
# 添加输出层
output_layer = tf.keras.layers.Dense(units=output_units)(middle_layer)

# 创建模型
model = tf.keras.Model(inputs=inputs, outputs=output_layer)

# 编译模型
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True))

# 输出模型概要
model.summary()
