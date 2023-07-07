import random
import time

import numpy as np

from DQN.agent import DQN

if __name__ == '__main__':
    action_size = 10
    agent = DQN((3, 3), action_size)
    x_test = np.random.rand(3, 3).reshape(1, 9)
    value = agent.policy_model.predict(x_test)
    print(value)
    for i in range(10001):
        agent.remember(_state=np.random.rand(3, 3).reshape(1, 9),
                       _action=random.randint(0, action_size - 1),
                       reward=random.random(),
                       _next_state=np.random.rand(3, 3).reshape(1, 9))
    start_time = time.perf_counter()
    for i in range(200):
        agent.replay()
        print(f"第{i}轮训练。消耗时间:{time.perf_counter() - start_time}")
    print(f"总消耗时间:{time.perf_counter() - start_time}")
    for i in range(1000):
        act = agent.act(np.random.random((1, 9)), True)
