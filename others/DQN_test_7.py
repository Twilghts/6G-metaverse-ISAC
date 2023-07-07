import numpy as np

from DQN.agent import DQN

if __name__ == '__main__':
    agent = DQN((3, 3), 20)
    # 生成一个3x3的随机矩阵
    random_matrix = np.random.rand(3, 3)
    expanded_input = np.expand_dims(random_matrix, axis=1)
    print(expanded_input)  # 在最后一个维度上添加一个维度
    x_test = expanded_input.reshape(1, 3, 3, 1)
    print(x_test)
    x_test_2 = random_matrix.reshape(1, 3, 3, 1)
    print(x_test_2)
    y_test = agent.target_model.predict(np.expand_dims(np.random.rand(3, 3), axis=0).reshape(1, 3, 3, 1))
    print(y_test)
    # y_test = y_test.numpy()
    # print(y_test)
