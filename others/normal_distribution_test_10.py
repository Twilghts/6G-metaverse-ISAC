from scipy.stats import norm
import numpy as np


def reword_for_throughput(throughput: int):
    # 正态分布的均值和标准差
    mean = 0
    std_dev = 1
    norm.cdf(throughput, mean, std_dev)
