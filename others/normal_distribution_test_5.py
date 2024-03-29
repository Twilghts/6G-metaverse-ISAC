from scipy.stats import norm

# 正态分布的均值和标准差
mean = 0
std_dev = 1

# 给定的 y 值
y = 0.25

# 使用 ppf 函数计算对应的 _t 值
x = norm.ppf(y, loc=mean, scale=std_dev)

print("_t =", x)
pdf_value = norm.pdf(x, loc=mean, scale=std_dev)

print("PDF delay at _t =", pdf_value)
