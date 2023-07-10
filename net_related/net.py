import copy
from typing import Dict, List

import networkx as nx
from matplotlib import pyplot as plt

from net_related.link import Link
from net_related.router import Router

_width = 3840 / 100
_height = 2160 / 100
# 创建一个 Figure 对象并设置图像大小（可选）
fig = plt.figure(figsize=(_width, _height))  # 设置图像宽度和高度（以英寸为单位）
# 设置图像的DPI值
_dpi_value = 100  # 或者根据需要设置其他DPI值
fig.dpi = _dpi_value


class Net:
    def __init__(self):
        self.G: nx.Graph = nx.read_graphml("../resource/graph.graphml")
        """读取出来的图的节点是字符串类型的，离谱！要更改节点的名字"""
        relabel_table: dict = {
            number: int(number) for number in self.G.nodes
        }
        self.G: nx.Graph = nx.relabel_nodes(self.G, relabel_table)
        self.router_storage = [2755, 3116, 3424, 2208, 3646, 3267, 3011, 3473, 4026, 3980, 3563, 3835, 2586, 2212,
                               3638, 4207]
        self.router_storage.sort()
        self.router_calculate = [143, 167, 115, 196, 168, 135, 186, 53, 151, 47, 116, 107, 83, 80, 135, 165]
        self.router_calculate.sort(reverse=True)
        self.router_bandwidth = [438, 520, 443, 458, 488, 525, 452, 483, 471, 496, 484, 488,
                                 532, 509, 550, 433]
        """路由器组 为字典，键为路由器的编号，值为所对应的路由器,设置路由器内部可存储的数据容量。"""
        self.routers: Dict[int, Router] = {
            number: Router(number, storage=self.router_storage[number], computing_power=self.router_calculate[number],
                           bandwidth=self.router_bandwidth[number]) for number in self.G.nodes
        }
        # """更新图的边权值， 为其两头路由器容量之和的一半"""
        # for u, v in self.G.edges:
        #     self.G[u][v]['weight']: int = (self.routers[u].storage + self.routers[v].storage) // 2
        """网络连接组 为字典，键为起始路由器和终止路由器的元组，值为相对应的网络链接。"""
        self.link_bandwidth = [761, 443, 656, 655, 302, 488, 542, 673, 674, 624, 639, 678, 463, 426, 334, 254,
                               659, 327, 703, 888, 392, 468, 504, 656, 453, 251, 669, 509, 603, 661, 469, 371]
        self.links: Dict[tuple, Link] = {
            (start, target): Link((start, target)) for start, target in self.G.edges
        }
        for number, link in zip(range(32), self.links.values()):
            link.sign = number
            link.bandwidth = self.link_bandwidth[number]

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def deal_data(self):
        for router in self.routers.values():
            router.deal_sensor_data()
            router.deal_calculate_task()
            dataset = router.pop_data_communication()
            if dataset:
                for data in dataset:
                    index = data.path.index(data.current_router) + 1
                    ports = (data.current_router, data.path[index])
                    if ports in self.links.keys():
                        data.delay = data.bandwidth_required / \
                                     (self.links[ports].bandwidth *
                                      self.links[ports].communication_distribution[data.slice_sign])
                    else:
                        data.delay = data.bandwidth_required / \
                                     (self.links[ports[::-1]].bandwidth *
                                      self.links[ports[::-1]].communication_distribution[data.slice_sign])
                    self.routers[data.path[index]].push_data_communication(data)

    def show_graph(self):
        # 使用spring布局绘制图形
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_size=6000, font_size=60, width=8.0)

        # 添加显示权重的边标签
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)

        # 显示绘图
        plt.show()

    def save_picture(self):
        # 保存图像为文件
        # 使用spring布局绘制图形
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True)

        # 添加显示权重的边标签
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)

        plt.savefig("../resource/graph.svg", dpi=_dpi_value, format='svg')

    def initialize(self):
        for router in self.routers.values():
            # 针对路由器带宽资源的初始化，切片一是主要处理通信业务的
            router.distribution[1][1] = 0.7
            router.distribution[1][2] = 0.15
            router.distribution[1][3] = 0.15
            # 针对路由器计算资源的初始化，切片二是主要处理计算业务的
            router.distribution[2][1] = 0.15
            router.distribution[2][2] = 0.7
            router.distribution[2][3] = 0.15
            # 针对路由器存储资源的初始化，切片三是主要处理存储业务的
            router.distribution[2][1] = 0.15
            router.distribution[2][2] = 0.15
            router.distribution[2][3] = 0.7
        for link in self.links.values():
            # 针对链路带宽资源的初始化，切片一是主要处理通信业务的
            link.communication_distribution[1] = 0.7
            link.communication_distribution[2] = 0.15
            link.communication_distribution[3] = 0.15

    def act_in_links(self):
        for link in self.links.values():
            link.communication_distribution[1] = (self.routers[link.ports[0]].distribution[1][1] +
                                                  self.routers[link.ports[1]].distribution[1][1]) / 2
            link.communication_distribution[2] = (self.routers[link.ports[0]].distribution[1][2] +
                                                  self.routers[link.ports[1]].distribution[1][2]) / 2
            link.communication_distribution[3] = (self.routers[link.ports[0]].distribution[1][3] +
                                                  self.routers[link.ports[1]].distribution[1][3]) / 2

    def chose_paths(self) -> Dict[int, List[List[int]]]:
        paths: Dict[int, List[List[int]]] = {
            1: [[]],
            2: [[]],
            3: [[]]
        }
        slice_1_start_node = [0, 1]
        slice_1_target_node = [6, 10]
        slice_2_start_node = [1, 2]
        slice_2_target_node = [10, 12]
        slice_3_start_node = [2, 3]
        slice_3_target_node = [6, 12]
        """为通信数据包临时选一些路"""
        """切片一的临时图"""
        tem_graph_slice_1 = copy.deepcopy(self.G)
        """切片二的临时图"""
        tem_graph_slice_2 = copy.deepcopy(self.G)
        """切片三的临时图"""
        tem_graph_slice_3 = copy.deepcopy(self.G)
        """以切片一在通信上的性能指标作为权值的基础，链路两端路由器的平均值作为该链路的权值"""
        for start, target, data in tem_graph_slice_1.edges(data=True):
            data['weight'] = (self.routers[start].state[0][0] + self.routers[target].state[0][0]) / 2
        paths[1] = [nx.shortest_path(tem_graph_slice_1, source=source, target=target)
                    for source in slice_1_start_node for target in slice_1_target_node]
        """以切片一在通信上的性能指标作为权值的基础，链路两端路由器的平均值作为该链路的权值"""
        for start, target, data in tem_graph_slice_2.edges(data=True):
            data['weight'] = (self.routers[start].state[0][1] + self.routers[target].state[0][1]) / 2
        paths[2] = [nx.shortest_path(tem_graph_slice_2, source=source, target=target)
                    for source in slice_2_start_node for target in slice_2_target_node]
        """以切片一在通信上的性能指标作为权值的基础，链路两端路由器的平均值作为该链路的权值"""
        for start, target, data in tem_graph_slice_3.edges(data=True):
            data['weight'] = (self.routers[start].state[0][2] + self.routers[target].state[0][2]) / 2
        paths[3] = [nx.shortest_path(tem_graph_slice_3, source=source, target=target)
                    for source in slice_3_start_node for target in slice_3_target_node]
        return paths
