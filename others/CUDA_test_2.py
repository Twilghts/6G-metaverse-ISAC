import random
import time

import networkx as nx

from DQN.agent import DQN

# 创建一个具有20个节点的全连接图
G = nx.complete_graph(20)
agent = DQN(1, 20)
for _ in range(10000):
    state = random.randint(0, 19)
    action = random.randint(0, 19)
    next_state = random.randint(0, 19)
    reward = random.uniform(-1, 1)
    agent.remember(state, action, reward, next_state)
for i in range(1000):
    print(time.perf_counter())
    # 生成一个二维数组
    array = [[random.randint(0, 19) for _ in range(6)] for _ in range(3)]
    agent.act(array, True)
    agent.replay()
    print(f"第{i}次训练")
print(time.perf_counter())
