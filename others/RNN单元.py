import numpy as np


def tanh(x):
    return np.tanh(x)


def rnn_cell(prev_h, x, Wh, Wx, bh):
    """
    :param prev_h: 上一个时间步的隐藏状态，初始时为全零向量
    :param x: 当前时间步的输入向量，这里是一个随机生成的输入
    :param Wh: 隐藏状态的权重矩阵，用于将上一个时间步的隐藏状态与当前时间步的输入连接起来
    :param Wx:输入的权重矩阵，用于将当前时间步的输入与上一个时间步的隐藏状态连接起来
    :param bh:隐藏状态的偏置
    :return:
    """
    # Concatenate input x and previous hidden state prev_h
    concat_input = np.concatenate((prev_h, x), axis=1)

    # Calculate the next hidden state
    next_h = tanh(np.dot(concat_input, Wh) + np.dot(x, Wx) + bh)

    return next_h


# Define the input size, hidden size, and output size
input_size = 3
hidden_size = 4

# Initialize weights and biases
Wh = np.random.randn(hidden_size + input_size, hidden_size)
Wx = np.random.randn(input_size, hidden_size)
bh = np.zeros((1, hidden_size))

# Initialize previous hidden state
prev_h = np.zeros((1, hidden_size))

# Generate a random input vector
x = np.random.randn(1, input_size)

# Perform one step of the RNN
next_h = rnn_cell(prev_h, x, Wh, Wx, bh)

# Print the results
print("Input x:", x)
print("Previous Hidden State prev_h:", prev_h)
print("Next Hidden State next_h:", next_h)
