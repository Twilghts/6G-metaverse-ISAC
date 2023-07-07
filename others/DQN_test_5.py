import tensorflow as tf
from tensorflow_estimator.python.estimator.estimator import Estimator

if __name__ == '__main__':
    def input_fn():
        # 定义输入特征
        features = {'input': tf.random.normal([None, 3, 6, 1])}  # 输入形状为(batch_size, 3, 6, 1)

        # 定义标签
        labels = tf.random.uniform([None, 10])  # 输出10个值

        # 返回特征和标签
        return features, labels


    def model_fn(features, labels, mode):
        # 定义卷积神经网络模型
        input_layer = features['input']
        conv1 = tf.keras.layers.Conv2D(inputs=input_layer, filters=16, kernel_size=(3, 3), activation=tf.nn.relu)
        pool1 = tf.keras.layers.MaxPool2D(inputs=conv1, pool_size=(2, 2), strides=(2, 2))
        conv2 = tf.keras.layers.Conv2D(inputs=pool1, filters=32, kernel_size=(3, 3), activation=tf.nn.relu)
        pool2 = tf.keras.layers.MaxPool2D(inputs=conv2, pool_size=(2, 2), strides=(2, 2))
        flatten = tf.keras.layers.Flatten(pool2)
        dense = tf.keras.layers.Dense(inputs=flatten, units=64, activation=tf.nn.relu)
        logits = tf.keras.layers.Dense(inputs=dense, units=10)

        # 定义预测输出
        predictions = {
            'classes': tf.argmax(logits, axis=1),
            'probabilities': tf.nn.softmax(logits)
        }

        # 如果是预测模式，则返回预测结果
        if mode == tf.estimator.ModeKeys.PREDICT:
            return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)

        # 定义损失函数
        loss = tf.losses.mean_squared_error(labels=labels, predictions=logits)

        # 定义训练操作
        if mode == tf.estimator.ModeKeys.TRAIN:
            optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=0.001)
            train_op = optimizer.minimize(loss=loss, global_step=tf.compat.v1.train.get_global_step())
            return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op)

        # 定义评估操作
        eval_metric_ops = {
            'accuracy': tf.keras.metrics.Accuracy(labels=tf.argmax(labels, axis=1), predictions=predictions['classes'])
        }
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)


    num_steps = 100

    # 创建Estimator对象
    estimator = Estimator(model_fn=model_fn)

    # 训练模型
    estimator.train(input_fn=input_fn, steps=num_steps)

    # 评估模型
    estimator.evaluate(input_fn=input_fn)
