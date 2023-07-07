import random

import numpy as np
from numpy import float32, float16

from DQN.agent import DQN
import tensorflow as tf

if __name__ == '__main__':
    action_size = 20
    agent = DQN((3, 3), action_size)
    matrix = np.random.random((64, 9))
    weights = agent.target_model(matrix)
    for i in range(100001):
        agent.remember(_state=np.random.rand(3, 3).reshape(1, 9),
                       _action=random.randint(0, action_size - 1),
                       reward=random.random(),
                       _next_state=np.random.rand(3, 3).reshape(1, 9))
    minibatch = np.array(agent.memory.sample(100000), dtype=float32)
    states = minibatch[:, 0:9]
    actions = minibatch[:, 9:10].astype(int)
    rewords = minibatch[:, 10:11]
    policy_values = agent.target_model(states).numpy()
    policy_next_values = agent.target_model(minibatch[:, 11:]).numpy()
    target_values = agent.target_model(minibatch[:, 11:]).numpy()
    for policy_value, policy_next_value, target_value, action, reward in zip(policy_values, policy_next_values,
                                                                             target_values, actions, rewords):
        policy_action = np.argmax(policy_next_value[0])
        policy_value[action[0]] = reward[0] + 0.95 * target_value[policy_action]
    dataset = tf.data.Dataset.from_tensor_slices((states, policy_values))


    # 定义数据集转换函数，将每个样本的每一行提取出来
    def extract_rows(data, labels):
        return tf.unstack(data), tf.unstack(labels)


    # 对数据集应用转换函数
    dataset = dataset.map(extract_rows)
    # 进行数据预处理、转换等操作
    dataset = dataset.shuffle(4096)  # 随机打乱数据
    dataset = dataset.batch(128)  # 批量化数据
    dataset = dataset.prefetch(1)  # 预取数据以提高性能
    agent.policy_model.fit(dataset, batch_size=128, epochs=100, use_multiprocessing=True, verbose=1)
