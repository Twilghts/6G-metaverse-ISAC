import numpy as np

"""针对每个切片的每类资源的重要性所设置的权重参数"""
weights_for_points = np.array([[8, 1, 1],
                               [1, 1, 8],
                               [1, 8, 1]], dtype=int)
"""针对每类切片在总网络上的重要性所设置的参数,分别代表切片一，切片二，切片三"""
weights_for_slice = np.array([[2, 0, 0],
                              [0, 9, 0],
                              [0, 0, 3]], dtype=int)

# 创建一个3x3的全1的矩阵
ones_matrix = np.ones((3, 3))
ones_matrix = np.multiply(ones_matrix, weights_for_points)
ones_matrix = ones_matrix @ weights_for_slice
print(np.sum(ones_matrix) / (np.sum(weights_for_points @ weights_for_slice)))