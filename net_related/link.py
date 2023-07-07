from collections import deque
from typing import Union, List
from data import CommunicationData


class Link:
    def __init__(self, ports: tuple, bandwidth: int = 1000):
        self.sign = None
        self.ports: tuple = ports  # 链路两端连接的路由器序号
        self.bandwidth: int = bandwidth
        """与通信相关的参数"""
        self.cache_queue_communication = deque()
        self.communication_distribution = {
            1: -1,
            2: -1,
            3: -1
        }

    def __repr__(self):
        return f'Link({self.ports})。'

    def __str__(self):
        return f'Link({self.ports})。'

    def transmit_communication_data(self, dataset: Union[None, List[CommunicationData]]) \
            -> Union[None, List[CommunicationData]]:
        if dataset is None:
            return None
        else:
            tem_list: List[CommunicationData] = []
            for data in dataset:
                data.delay = data.bandwidth_required / \
                             (self.communication_distribution[data.slice_sign] * self.bandwidth)
                tem_list.append(data)
        return tem_list
