import numpy as np

mean = 2500 # 正态分布的均值
stddev = 700  # 正态分布的标准差
size = 16  # 生成的整数数量

random_floats = np.random.normal(mean, stddev, size)
random_ints = np.round(random_floats).astype(int)

print(random_ints)

lam = 1600  # 泊松分布的参数 lambda
size = 16  # 生成的整数数量

random_poisson = np.random.poisson(lam, size)
random_ints = random_poisson.astype(int)

print(random_ints)
