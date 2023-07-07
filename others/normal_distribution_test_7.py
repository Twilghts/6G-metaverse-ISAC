from scipy.stats import norm

# 正态分布的均值和标准差
mean = 0
std_dev = 1

# 给定的概率密度函数值
pdf_value = 0.9

# 使用 ppf 函数计算对应的 x 值
x = norm.ppf(pdf_value, loc=mean, scale=std_dev)

# 使用 cdf 函数计算对应的 y 值
y = norm.cdf(x, loc=mean, scale=std_dev)

print("x =", x)
print("y =", y)
