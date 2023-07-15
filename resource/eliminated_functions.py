import numpy as np
from scipy.stats import norm


def reword_for_delay(delay) -> float:
    """求正态分布函数与一条平行于x轴的直线所围成的面积，传入的参数为直线的y坐标值。作为求时延的奖励函数"""
    # 运行一次大概为1/5000秒
    # 正态分布的标准差
    std_dev: float = 1
    """如果当前时间片没有处理通信任务就返回一个比较小的奖励值"""
    if delay == -1:
        return 0.2
    elif delay >= norm.pdf(0, 0, std_dev):
        return 0
    elif delay <= 0:
        return 1
    else:
        _x: float = np.sqrt(-2 * np.square(std_dev) * np.log(np.sqrt(2 * np.pi) * std_dev * delay))
        return norm.cdf(_x, 0, std_dev) - \
            norm.cdf(-_x, 0, std_dev) - 2 * \
            _x * norm.pdf(_x, 0, std_dev)
