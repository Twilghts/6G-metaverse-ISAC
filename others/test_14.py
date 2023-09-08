import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def reword_for_hash_rate(delay) -> float:
    std_dev: float = 0.5
    if delay == -1:
        return 0.07
    elif delay >= norm.pdf(0, 0, std_dev):
        return 0
    elif delay <= 0:
        return 1
    else:
        _x: float = np.sqrt(-2 * np.square(std_dev) * np.log(np.sqrt(2 * np.pi) * std_dev * delay))
        return norm.cdf(_x, 0, std_dev) - \
            norm.cdf(-_x, 0, std_dev) - 2 * \
            _x * norm.pdf(_x, 0, std_dev)


# 创建一个范围内的延迟值
delay_values = np.linspace(0, norm.pdf(0, 0, 0.5), 100)
rewards = [reword_for_hash_rate(delay) for delay in delay_values]

# 绘制函数图形
plt.figure(figsize=(8, 6))
plt.plot(delay_values, rewards, label='Reward Function')
plt.xlabel('Delay')
plt.ylabel('Reward')
plt.title('Reward Function for Hash Rate')
plt.legend()
plt.grid(True)
plt.show()
