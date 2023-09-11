import time

from DQN.train import choose_router_index_by_calculate_weight
from net_related.net import Net

if __name__ == '__main__':
    net = Net()
    start_time = time.perf_counter()
    for i in range(100000):
        # print(choose_router_index_by_calculate_weight(net))
        numbers = choose_router_index_by_calculate_weight(_net=net)
    print(f"消耗时间:{time.perf_counter() - start_time}")
    for i in range(100000):
        pass
