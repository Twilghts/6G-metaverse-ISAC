from typing import Union

import numpy as np
from numpy import float32
from scipy.stats import norm

'''
def reword_for_delay(delay) -> float:
    if delay == -1:
        return 0.05
    mean = 0
    std_dev = 0.35 / np.sqrt(2 * np.pi)
    return 0.35 * norm.pdf(delay, mean, std_dev)
'''


def reword_for_delay(delay) -> float:
    """求正态分布函数与一条平行于x轴的直线所围成的面积，传入的参数为直线的y坐标值。作为求时延的奖励函数"""
    # 运行一次大概为1/5000秒
    # 正态分布的标准差
    std_dev: float = 1
    """如果当前时间片没有处理通信任务就返回一个比较小的奖励值"""
    if delay == -1:
        return 0.15
    elif delay >= norm.pdf(0, 0, std_dev):
        return 0
    elif delay <= 0:
        return 1
    else:
        _x: float = np.sqrt(-2 * np.square(std_dev) * np.log(np.sqrt(2 * np.pi) * std_dev * delay))
        return norm.cdf(_x, 0, std_dev) - \
            norm.cdf(-_x, 0, std_dev) - 2 * \
            _x * norm.pdf(_x, 0, std_dev)


def reword_for_hash_rate(delay) -> float:
    """求正态分布函数与一条平行于x轴的直线所围成的面积，传入的参数为直线的y坐标值。作为求时延的奖励函数"""
    # 运行一次大概为1/5000秒
    # 正态分布的标准差
    std_dev: float = 1
    """如果当前时间片没有处理通信任务就返回一个比较小的奖励值"""
    if delay == -1:
        return 0.15
    elif delay >= norm.pdf(0, 0, std_dev):
        return 0
    elif delay <= 0:
        return 1
    else:
        _x: float = np.sqrt(-2 * np.square(std_dev) * np.log(np.sqrt(2 * np.pi) * std_dev * delay))
        return norm.cdf(_x, 0, std_dev) - \
            norm.cdf(-_x, 0, std_dev) - 2 * \
            _x * norm.pdf(_x, 0, std_dev)


'''
def reword_for_hash_rate(delay: float) -> float:
    """求算力时延的奖励函数"""
    # 正态分布的均值和标准差
    """如果当前时间片没有处理计算任务就返回一个比较小的奖励值"""
    if delay == -1:
        return 0.05
    mean = 0
    std_dev = 0.35 / np.sqrt(2 * np.pi)
    return 0.35 * norm.pdf(delay, mean, std_dev)
'''


def reword_for_package_loss_sensitive(loss: Union[None, bool]) -> float:
    """丢包率敏感的切片的丢包率奖励函数"""
    """如果当前时间片没有处理存储任务就返回一个折中的奖励值"""
    if loss is None:
        return 0.03
    elif loss:
        return 0
    else:
        return 1


def reword_for_package_loss_insensitive(loss: Union[None, bool]) -> float:
    """丢包率不敏感的切片的丢包率奖励函数"""
    """如果当前时间片没有处理存储任务就返回一个折中的奖励值"""
    if loss is None:
        return 0.03
    elif loss != 0:
        return 0
    else:
        return 0.1


def reword(state: tuple):
    """
    Usage: 计算奖励值的函数,传入的3*3的元组应该满足如下现实联系：
            切片一对时延敏感，要求的带宽资源多。
            切片二对计算速度敏感，要求的计算资源多。
            切片三对丢包率敏感，要求的存储资源多。
            (   (切片一的带宽资源占比)    ,   (切片二的带宽资源占比)    ,   (切片三的带宽资源占比),
            (切片一的算力资源占比)    ,   (切片二的算力资源占比)    ,   (切片三的算力资源占比),
            (切片一的存储资源占比)    ,   (切片二的存储资源占比)    ,   (切片三的存储资源占比))
            正常情况下运行时间为1/1000秒
    """
    """将原始状态转换成float32参数的矩阵"""
    arguments = np.array(state, dtype=float32)
    """设定针对不同参数的奖励函数"""
    functions = np.array([[reword_for_delay, reword_for_delay, reword_for_delay],
                          [reword_for_hash_rate, reword_for_hash_rate, reword_for_hash_rate],
                          [reword_for_package_loss_insensitive, reword_for_package_loss_insensitive,
                           reword_for_package_loss_sensitive]])
    """将每个函数的元素应用到相应的参数上，求出原始奖励值"""
    result = np.vectorize(lambda f, x: f(x))(functions, arguments)
    """针对每个切片的每类资源的重要性所设置的权重参数"""
    weights_for_points = np.array([[7, 1.5, 1.5],
                                   [1.5, 7, 1.5],
                                   [1.5, 1.5, 7]], dtype=int)
    """针对每类切片在总网络上的重要性所设置的参数,分别代表切片一，切片二，切片三"""
    weights_for_slice = np.array([[1, 0, 0],
                                  [0, 1, 0],
                                  [0, 0, 1]], dtype=int)
    """将原始奖励值和每个切片的每类资源的重要性所设置的权重参数相乘"""
    # 对应元素相乘
    result = np.multiply(result, weights_for_points)
    """将第一次加权奖励值和每类切片在总网络上的重要性所设置的参数相乘"""
    result = result @ weights_for_slice
    """为所有的加权求平均值,即最后的奖励值矩阵求和后除以第一个权重矩阵和第二个权重矩阵相乘后并求和"""
    return np.sum(result) / (np.sum(weights_for_points @ weights_for_slice))
