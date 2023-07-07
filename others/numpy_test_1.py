import numpy as np

# 创建两个示例矩阵
matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix2 = np.array([[2, 4, 6], [8, 10, 12]])

# 对应元素相乘
result = np.multiply(matrix1, matrix2)

print(result)


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



