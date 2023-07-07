import numpy as np

# 定义九个参数
params = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# 定义九个函数
def func1(x):
    return x + 1


def func2(x):
    return x * 2


def func3(x):
    return x ** 2


def func4(x):
    return np.sin(x)


def func5(x):
    return np.cos(x)


def func6(x):
    return np.exp(x)


def func7(x):
    return np.log(x)


def func8(x):
    return np.sqrt(x)


def func9(x):
    return x / 2


# 将函数放入列表中
functions = [func1, func2, func3, func4, func5, func6, func7, func8, func9]

# 将函数列表转换为NumPy数组
func_array = np.array(functions)

# 对参数矩阵和函数数组进行广播运算
result_matrix = func_array[:, np.newaxis, np.newaxis](params)

# 打印结果矩阵
print(result_matrix)
