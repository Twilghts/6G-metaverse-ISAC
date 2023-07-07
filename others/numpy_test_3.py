import numpy as np
from numpy import float16


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


arguments = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]], dtype=float16)

functions = np.array([[func1, func2, func3],
                      [func4, func5, func6],
                      [func7, func8, func9]])

result = np.vectorize(lambda f, x: f(x))(functions, arguments)

print(result)
