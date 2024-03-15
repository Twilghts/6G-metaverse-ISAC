import numpy as np
from DQN.agent import DQN

x = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# print(sum(_t))
y = np.array(x, dtype=int)
z = np.sum(y)
agent = DQN((3, 3), 20)

list_1 = [3, 45, 34, 76, 7, 8, 9, 8, 9, 90, 12, 0, 123]

for item in list_1:
    print(item)
