import numpy as np


def sigmoid(_x):
    return 1 / (1 + np.exp(-_x))


def tanh(_x):
    return np.tanh(_x)


def lstm_cell(_prev_c, _prev_h, _x, _Wf, _Wi, _Wc, _Wo, _bf, _bi, _bc, _bo):
    """
    :param _prev_c:前一个单元的细胞状态
    :param _prev_h:前一个单元的输出
    :param _x:这个单元的输入
    :param _Wf:忘记门（Forget Gate）的参数值
    :param _Wi:输入门（Input Gate）的参数值之一
    :param _Wc:输入门（Input Gate）的参数值之一
    :param _Wo:输出门（Output gate）的参数值
    :param _bf:忘记门（Forget Gate）的偏移(bias)
    :param _bi:输入门（Input Gate）的偏移(bias)
    :param _bc:输入门（Input Gate）的偏移(bias)值之一
    :param _bo:输出门（Output gate）的偏移(bias)
    :return:当前的单元生成的细胞状态(Cell state)和输出值
    """
    # Concatenate input _x and previous hidden state _prev_h
    # 连接输入值和前一个单元的输出值
    concat_input = np.concatenate((_prev_h, _x), axis=1)
    # Forget gate（忘记门）
    forget_gate = sigmoid(np.dot(concat_input, _Wf) + _bf)
    # Input gate（输入门）
    input_gate = sigmoid(np.dot(concat_input, _Wi) + _bi)
    # Cell state update（更新细胞状态）
    cell_candidate = tanh(np.dot(concat_input, _Wc) + _bc)
    cell_state = forget_gate * _prev_c + input_gate * cell_candidate
    # Output gate（输出门）
    output_gate = sigmoid(np.dot(concat_input, _Wo) + _bo)
    # Hidden state update（隐藏状态更新）
    hidden_state = output_gate * tanh(cell_state)
    return cell_state, hidden_state

# Define the input size, hidden size, and output size
# 定义输入层尺寸、隐藏层尺寸和输出层尺寸
input_size = 3
hidden_size = 4
# Initialize weights and biases for the forget gate
# 为遗忘门初始化权重和偏差
Wf = np.random.randn(hidden_size + input_size, hidden_size)
bf = np.zeros((1, hidden_size))
# Initialize weights and biases for the input gate
# 初始化输入门的权重和偏差
Wi = np.random.randn(hidden_size + input_size, hidden_size)
bi = np.zeros((1, hidden_size))
# Initialize weights and biases for the cell state
# 初始化单元状态的权重和偏差
Wc = np.random.randn(hidden_size + input_size, hidden_size)
bc = np.zeros((1, hidden_size))
# Initialize weights and biases for the output gate
# 初始化输出门的权重和偏差
Wo = np.random.randn(hidden_size + input_size, hidden_size)
bo = np.zeros((1, hidden_size))
# Initialize cell state and hidden state
# 初始化细胞单元和隐藏状态
prev_c = np.zeros((1, hidden_size))
prev_h = np.zeros((1, hidden_size))
# Generate a random input vector
# 生成一个随机输入向量
x = np.random.randn(1, input_size)

# Perform one step of the LSTM(执行LSTM的一个步骤)
next_c, next_h = lstm_cell(prev_c, prev_h, x, Wf, Wi, Wc, Wo, bf, bi, bc, bo)

# Print the results
print("Input _x:", x)
print("Previous Cell State _prev_c:", prev_c)
print("Previous Hidden State _prev_h:", prev_h)
print("Next Cell State next_c:", next_c)
print("Next Hidden State next_h:", next_h)
