import numpy as np


# 定义sigmoid和tanh激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def tanh(x):
    return np.tanh(x)


# 定义LSTM单元
def lstm_cell(prev_c, prev_h, x, Wf, Wi, Wc, Wo, bf, bi, bc, bo, d_hidden_state):
    concat_input = np.concatenate((prev_h, x), axis=1)

    forget_gate = sigmoid(np.dot(concat_input, Wf) + bf)
    input_gate = sigmoid(np.dot(concat_input, Wi) + bi)
    cell_candidate = tanh(np.dot(concat_input, Wc) + bc)
    cell_state = forget_gate * prev_c + input_gate * cell_candidate
    output_gate = sigmoid(np.dot(concat_input, Wo) + bo)
    hidden_state = output_gate * tanh(cell_state)

    # 计算梯度
    d_output_gate = tanh(cell_state) * d_hidden_state
    d_tanh_cell_state = output_gate * d_hidden_state
    d_cell_state = (1 - np.tanh(cell_state) ** 2) * d_tanh_cell_state
    d_forget_gate = prev_c * d_cell_state
    d_input_gate = cell_candidate * d_cell_state
    d_cell_candidate = input_gate * d_cell_state

    # 传递梯度到前一个时间步
    d_prev_c = forget_gate * d_cell_state

    # 更新参数的梯度，这里省略了具体的更新步骤

    return cell_state, hidden_state, forget_gate, input_gate, cell_candidate, output_gate, d_forget_gate, d_input_gate, d_cell_candidate, d_output_gate, d_prev_c


# 定义LSTM模型
def lstm_model(inputs, initial_cell_state, initial_hidden_state, parameters):
    cell_state = initial_cell_state
    hidden_state = initial_hidden_state
    cell_states, hidden_states = [], []

    # 遍历序列中的每个时间步
    for t in range(len(inputs)):
        x = inputs[t]
        cell_state, hidden_state = lstm_cell(cell_state, hidden_state, x, *parameters)
        cell_states.append(cell_state)
        hidden_states.append(hidden_state)

    return cell_states, hidden_states


# 定义损失函数
def mean_squared_error(predictions, targets):
    return np.mean((predictions - targets) ** 2)


# 初始化参数
input_size = 3
hidden_size = 4

Wf = np.random.randn(hidden_size + input_size, hidden_size)
bf = np.zeros((1, hidden_size))

Wi = np.random.randn(hidden_size + input_size, hidden_size)
bi = np.zeros((1, hidden_size))

Wc = np.random.randn(hidden_size + input_size, hidden_size)
bc = np.zeros((1, hidden_size))

Wo = np.random.randn(hidden_size + input_size, hidden_size)
bo = np.zeros((1, hidden_size))

# 构建训练数据
num_steps = 10
input_element = np.random.randn(1, input_size) * 10
input_sequence = [input_element for _ in range(num_steps)]

initial_cell_state = np.zeros((1, hidden_size))
initial_hidden_state = np.zeros((1, hidden_size))

target = np.random.randn(1, hidden_size) * 10
targets = [target for _ in range(num_steps)]

# 超参数
learning_rate = 0.001
epochs = 100

# 训练过程
for epoch in range(epochs):
    total_loss = 0
    gradients = np.zeros_like(Wf)

    # 在每个epoch中遍历训练序列
    for step in range(num_steps):
        x = input_sequence[step]
        target = targets[step]

        # 执行LSTM模型前向传播
        predicted_cell_states, predicted_hidden_states = lstm_model([x], initial_cell_state, initial_hidden_state,
                                                                    [Wf, Wi, Wc, Wo, bf, bi, bc, bo])

        # 计算损失
        loss = mean_squared_error(predicted_hidden_states[-1], target)
        total_loss += loss

        # 反向传播计算梯度
        d_loss = 2 * (predicted_hidden_states[-1] - target)  # 损失对输出的梯度
        d_cell_state, d_hidden_state = np.zeros_like(initial_cell_state), np.zeros_like(initial_hidden_state)

        # 反向传播更新参数（梯度下降）
        for t in reversed(range(num_steps)):
            x = input_sequence[t]
            prev_cell_state = initial_cell_state if t == 0 else predicted_cell_states[t - 1]
            prev_hidden_state = initial_hidden_state if t == 0 else predicted_hidden_states[t - 1]

            concat_input = np.concatenate((prev_hidden_state, x), axis=1)
            d_output_gate = tanh(predicted_cell_states[t]) * d_hidden_state
            d_tanh_cell_state = predicted_hidden_states[t] * d_hidden_state
            d_cell_state += (1 - tanh(predicted_cell_states[t]) ** 2) * d_tanh_cell_state
            d_cell_candidate = sigmoid(np.dot(concat_input, Wi) + bi) * d_cell_state
            d_input_gate = tanh(np.dot(concat_input, Wc) + bc) * d_cell_state
            d_forget_gate = prev_cell_state * d_cell_state

            dWi = np.dot(np.concatenate((prev_hidden_state, x), axis=1).T, d_input_gate * sigmoid(
                np.dot(np.concatenate((prev_hidden_state, x), axis=1), Wi) + bi))
            dWc = np.dot(np.concatenate((prev_hidden_state, x), axis=1).T, d_cell_candidate * tanh(
                np.dot(np.concatenate((prev_hidden_state, x), axis=1), Wc) + bc))
            dWo = np.dot(np.concatenate((prev_hidden_state, x), axis=1).T, d_output_gate * sigmoid(
                np.dot(np.concatenate((prev_hidden_state, x), axis=1), Wo) + bo))

            d_cell_state = d_forget_gate * d_cell_state  # 传递到前一个时间步
            d_hidden_state = np.dot(d_input_gate * sigmoid(
                np.dot(np.concatenate((prev_hidden_state, x), axis=1), Wi) + bi).T, Wi[:-hidden_size, :]) + \
                             np.dot(d_cell_candidate * tanh(
                                 np.dot(np.concatenate((prev_hidden_state, x), axis=1), Wc) + bc).T,
                                    Wc[:-hidden_size, :]) + \
                             np.dot(d_output_gate * sigmoid(
                                 np.dot(np.concatenate((prev_hidden_state, x), axis=1), Wo) + bo).T,
                                    Wo[:-hidden_size, :])

            # 更新参数
            Wf -= learning_rate * np.dot(np.concatenate((prev_hidden_state, x), axis=1).T,
                                         d_forget_gate * sigmoid(
                                             np.dot(np.concatenate((prev_hidden_state, x), axis=1), Wf) + bf))
            Wi -= learning_rate * dWi
            Wc -= learning_rate * dWc
            Wo -= learning_rate * dWo

    average_loss = total_loss / num_steps
    print(f"Epoch {epoch + 1}/{epochs}, Loss: {average_loss}")
