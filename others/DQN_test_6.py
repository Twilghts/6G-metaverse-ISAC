import time

import numpy as np
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, fully_connected
from tflearn.layers.estimator import regression

if __name__ == '__main__':
    # Define the input layer
    network = input_data(shape=[None, 3, 3, 1])  # Input shape: (batch_size, 3, 6, 1)

    # Add a convolutional layer
    network = conv_2d(network, 16, 5, activation='relu')

    # Add a max pooling layer
    network = max_pool_2d(network, 2)

    # Add another convolutional layer
    network = conv_2d(network, 32, 5, activation='relu')

    # Add another max pooling layer
    network = max_pool_2d(network, 2)

    # Flatten the network
    network = tflearn.flatten(network)

    # Add a fully connected layer
    network = fully_connected(network, 64, activation='relu')

    # Add the output layer
    network = fully_connected(network, 10, activation='linear')

    # Define the regression layer
    network = regression(network, optimizer='adam', loss='mean_square', learning_rate=0.001)

    # Create the model
    model = tflearn.DNN(network)

    # 假设我们有一个3x6的二维列表
    my_list = [
        [1, 2, 3],
        [7, 8, 9],
        [13, 14, 15]
    ]
    x_test = np.array(my_list).reshape([-1, 3, 3, 1])
    start_time = time.perf_counter()
    for i in range(100000):
        result = model.predict(x_test)
    print(time.perf_counter() - start_time)
