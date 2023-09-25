from scipy.stats import norm
import numpy as np


def reword_for_throughput(throughput: int):
    # 正态分布的均值和标准差
    mean = 0
    std_dev = 0.7
    norm.cdf(throughput, mean, std_dev)


print(norm.pdf(0, 0, 0.9))
print(norm.pdf(0.01, 0, 1.0 / np.sqrt(2 * np.pi)))
print(norm.pdf(2, 0, 1.0 / np.sqrt(2 * np.pi)))
