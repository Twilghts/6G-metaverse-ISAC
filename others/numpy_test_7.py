import time

import numpy as np


def matrix_multiplication(matrix1, matrix2):
    """
    计算两个矩阵的乘法
    :param matrix1: 第一个矩阵，二维列表
    :param matrix2: 第二个矩阵，二维列表
    :return: 乘法结果矩阵，二维列表
    """
    # 检查矩阵的尺寸是否满足乘法条件
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("矩阵的尺寸不满足乘法条件！")

    # 初始化结果矩阵
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]

    # 进行矩阵乘法计算
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


if __name__ == '__main__':
    matrix_1 = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]

    matrix_2 = [[10, 11, 12],
                [13, 14, 15],
                [16, 17, 18]]

    ndarray_1 = np.array(matrix_1)
    ndarray_2 = np.array(matrix_2)
    ndarray_3 = ndarray_1 @ ndarray_2
    start_time = time.perf_counter()
    for i in range(10000):
        ndarray_3 = ndarray_1 @ ndarray_2
    print(time.perf_counter() - start_time)
    print(ndarray_3)
    matrix_3 = matrix_multiplication(matrix_1, matrix_2)
    start_time = time.perf_counter()
    for i in range(10000):
        matrix_3 = matrix_multiplication(matrix_1, matrix_2)
    print(time.perf_counter() - start_time)
    print(matrix_3)