import scipy.stats as stats
import numpy as np

# 创建标准正态分布对象
norm_dist = stats.norm()

# 直线的 y 坐标
c = 0.3

# 求解与直线交点的 _t 坐标
x_intersections = norm_dist.ppf(c)

# 打印交点坐标
for i in range(len(x_intersections)):
    print(f"交点{i+1}：({x_intersections[i]}, {c})")
