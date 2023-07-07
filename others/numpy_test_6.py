import numpy as np
import time
from DQN.methods import reword

state = ((0.1, 0.15, 0.16),
         (0.19, 0.18, 0.17),
         (0.20, 0.21, 0.22))

start_time = time.perf_counter()
for i in range(10000):
    _reword = reword(state)
print(time.perf_counter() - start_time)
