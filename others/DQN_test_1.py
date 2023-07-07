from DQN.agent import DQN
import numpy as np

if __name__ == '__main__':
    # 定义输入形状
    input_shape = (3, 6)
    # 假设我们有一个3x6的二维列表
    my_list = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18]
    ]
    # my_list = [[1, 2, 3],
    #            [4, 5, 6],
    #            [7, 8, 9]]
    x_test = np.array(my_list).reshape(3, 3)
    agent = DQN(input_shape, 10)
    weights = agent.target_model(x_test)
    print(weights)
    # # 将列表转换成ndarray
    # my_ndarray = np.array(my_list)
    #
    # print(my_ndarray)
