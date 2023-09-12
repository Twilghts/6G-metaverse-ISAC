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
        self.core_graph: nx.Graph = nx.read_graphml("../resource/graph.graphml")
        """读取出来的图的节点是字符串类型的，离谱！要更改节点的名字"""
        relabel_table: dict = {
            number: int(number) for number in self.core_graph.nodes
        }
        self.core_graph: nx.Graph = nx.relabel_nodes(self.core_graph, relabel_table)
        self.router_storage = [2222, 1386, 1602, 2235, 1961, 2263, 3089, 852, 1746, 2525, 3170, 472, 1884, 2520,
                               2816, 2362]
        self.router_storage.sort(reverse=True)
        self.router_calculate = [226, 383, 225, 165, 210, 247, 334, 156, 210, 241, 320, 264, 233, 129, 281, 132]
        """用作为计算类任务根据路由器计算资源随机选择路由器"""
        self.total_calculate_weight = sum(self.router_calculate)
        self.router_calculate.sort()
        self.router_bandwidth = [438, 520, 443, 458, 488, 525, 452, 483, 471, 496, 484, 488,
                                 532, 509, 550, 433]
        """路由器组 为字典，键为路由器的编号，值为所对应的路由器,设置路由器内部可存储的数据容量。"""
        self.core_routers: Dict[int, Router] = {
            number: Router(number, storage=self.router_storage[number], computing_power=self.router_calculate[number],
                           bandwidth=self.router_bandwidth[number]) for number in range(0, 16)
        }
        self.edge_routers_first: Dict[int, Router] = {
            number: Router(number) for number in range(16, 24)
        }
        self.edge_routers_second: Dict[int, Router] = {
            number: Router(number) for number in range(24, 32)
        }
        self.base_station: Dict[int, Router] = {
            number: Router(number) for number in [32, 33]
        }
        # """更新图的边权值， 为其两头路由器容量之和的一半"""
        # for u, v in self.core_graph.edges:
        #     self.core_graph[u][v]['weight']: int = (self.core_routers[u].storage + self.core_routers[v].storage) // 2
        """网络连接组 为字典，键为起始路由器和终止路由器的元组，值为相对应的网络链接。"""
        self.link_bandwidth = [761, 443, 656, 655, 302, 488, 542, 673, 674, 624, 639, 678, 463, 426, 334, 254,
                               659, 327, 703, 888, 392, 468, 504, 656, 453, 251, 669, 509, 603, 661, 469, 371]
        self.links: Dict[tuple, Link] = {
            (start, target): Link((start, target)) for start, target in self.core_graph.edges
        }
        for number, link in zip(range(32), self.links.values()):
            link.sign = number
            link.bandwidth = self.link_bandwidth[number]

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def deal_data(self):
        for router in self.core_routers.values():
            passing_dataset = router.deal_sensor_data()
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
                    self.core_routers[data.path[index]].push_data_communication(data)
            if passing_dataset:
                for data in passing_dataset:
                    index = data.path.index(data.current_router) + 1
                    ports = (data.current_router, data.path[index])
                    if ports in self.links.keys():
                        data.delay = data.storage_required / \
                                     (self.links[ports].bandwidth *
                                      self.links[ports].communication_distribution[data.slice_sign])
                    else:
                        data.delay = data.storage_required / \
                                     (self.links[ports[::-1]].bandwidth *
                                      self.links[ports[::-1]].communication_distribution[data.slice_sign])
                    self.core_routers[data.path[index]].push_sensor_data(data)

        for router in self.edge_routers_first.values():
            while router.sensor_queue:
                if len(self.base_station[32].sensor_queue) <= 300:
                    """存取数据要记得增减负载值"""
                    data = router.sensor_queue.pop()
                    data.delay += 0.001
                    router.sensor_load_slice[data.slice_sign] -= data.storage_required
                    self.base_station[32].sensor_queue.append(data)
                    data.current_router = 32
                else:
                    break

        for router in self.edge_routers_second.values():
            while router.sensor_queue:
                if len(self.base_station[33].sensor_queue) <= 150:
                    data = router.sensor_queue.pop()
                    data.delay += 0.001
                    router.sensor_load_slice[data.slice_sign] -= data.storage_required
                    self.base_station[33].sensor_queue.append(data)
                    data.current_router = 33
                else:
                    break

        self.core_routers[0].push_sensor_data(self.base_station[32].sensor_queue)
        self.base_station[32].sensor_queue.clear()

        self.core_routers[1].push_sensor_data(self.base_station[33].sensor_queue)
        self.base_station[33].sensor_queue.clear()

    def show_graph(self):
        # 使用spring布局绘制图形
        pos = nx.spring_layout(self.core_graph)
        nx.draw(self.core_graph, pos, with_labels=True, node_size=6000, font_size=60, width=8.0)

        # 添加显示权重的边标签
        labels = nx.get_edge_attributes(self.core_graph, 'weight')
        nx.draw_networkx_edge_labels(self.core_graph, pos, edge_labels=labels)

        # 显示绘图
        plt.show()

    def save_picture(self):
        # 保存图像为文件
        # 使用spring布局绘制图形
        pos = nx.spring_layout(self.core_graph)
        nx.draw(self.core_graph, pos, with_labels=True)

        # 添加显示权重的边标签
        labels = nx.get_edge_attributes(self.core_graph, 'weight')
        nx.draw_networkx_edge_labels(self.core_graph, pos, edge_labels=labels)

        plt.savefig("../resource/graph.svg", dpi=_dpi_value, format='svg')

    def initialize(self):
        for router in self.core_routers.values():
            # 针对路由器带宽资源的初始化，切片一是主要处理通信业务的
            router.distribution[1][1] = 0.625
            router.distribution[1][2] = 0.1475
            router.distribution[1][3] = 0.1475
            # 针对路由器计算资源的初始化，切片二是主要处理计算业务的
            router.distribution[2][1] = 0.2
            router.distribution[2][2] = 0.6
            router.distribution[2][3] = 0.2
            # 针对路由器存储资源的初始化，切片三是主要处理存储业务的
            router.distribution[3][1] = 0.15
            router.distribution[3][2] = 0.15
            router.distribution[3][3] = 0.7
        for link in self.links.values():
            # 针对链路带宽资源的初始化，切片一是主要处理通信业务的
            link.communication_distribution[1] = 0.625
            link.communication_distribution[2] = 0.1475
            link.communication_distribution[3] = 0.1475

        for router in self.edge_routers_first.values():
            # 针对路由器带宽资源的初始化，切片一是主要处理通信业务的
            router.distribution[1][1] = 0.625
            router.distribution[1][2] = 0.1475
            router.distribution[1][3] = 0.1475
            # 针对路由器计算资源的初始化，切片二是主要处理计算业务的
            router.distribution[2][1] = 0.2
            router.distribution[2][2] = 0.6
            router.distribution[2][3] = 0.2
            # 针对路由器存储资源的初始化，切片三是主要处理存储业务的
            router.distribution[3][1] = 0.15
            router.distribution[3][2] = 0.15
            router.distribution[3][3] = 0.7

        for router in self.edge_routers_second.values():
            # 针对路由器带宽资源的初始化，切片一是主要处理通信业务的
            router.distribution[1][1] = 0.625
            router.distribution[1][2] = 0.1475
            router.distribution[1][3] = 0.1475
            # 针对路由器计算资源的初始化，切片二是主要处理计算业务的
            router.distribution[2][1] = 0.2
            router.distribution[2][2] = 0.6
            router.distribution[2][3] = 0.2
            # 针对路由器存储资源的初始化，切片三是主要处理存储业务的
            router.distribution[3][1] = 0.15
            router.distribution[3][2] = 0.15
            router.distribution[3][3] = 0.7

    def act_in_links(self):
        for link in self.links.values():
            link.communication_distribution[1] = (self.core_routers[link.ports[0]].distribution[1][1] +
                                                  self.core_routers[link.ports[1]].distribution[1][1]) / 2
            link.communication_distribution[2] = (self.core_routers[link.ports[0]].distribution[1][2] +
                                                  self.core_routers[link.ports[1]].distribution[1][2]) / 2
            link.communication_distribution[3] = (self.core_routers[link.ports[0]].distribution[1][3] +
                                                  self.core_routers[link.ports[1]].distribution[1][3]) / 2

    def chose_paths(self) -> Dict[int, List[List[int]]]:
        paths: Dict[int, List[List[int]]] = {
            1: [[]],
            2: [[]],
            3: [[]],
            4: [[]],
            5: [[]],
            6: [[]]  # 为感知类任务设置的路径
        }
        slice_1_start_node = [4, 5]
        slice_1_target_node = [6, 10]
        slice_2_start_node = [1, 2]
        slice_2_target_node = [10, 12]
        slice_3_start_node = [2, 3]
        slice_3_target_node = [6, 12]
        """为传感类任务选择路径"""
        sensor_start_node = [0, 1]
        sensor_target_node = [n for n in range(2, 15, 3)]
        """为通信数据包临时选一些路"""
        """切片一的临时图"""
        tem_graph_slice_1 = copy.deepcopy(self.core_graph)
        """切片二的临时图"""
        tem_graph_slice_2 = copy.deepcopy(self.core_graph)
        """切片三的临时图"""
        tem_graph_slice_3 = copy.deepcopy(self.core_graph)
        """以切片一在通信上的性能指标作为权值的基础，链路两端路由器的平均值作为该链路的权值"""
        for start, target, data in tem_graph_slice_1.edges(data=True):
            data['weight'] = (self.core_routers[start].state[0][0] + self.core_routers[target].state[0][0]) / 2
        paths[1] = [nx.shortest_path(tem_graph_slice_1, source=source, target=target)
                    for source in slice_1_start_node for target in slice_1_target_node]
        paths[4] = [nx.shortest_path(tem_graph_slice_1, source=source, target=target)
                    for source in sensor_start_node for target in sensor_target_node]
        """以切片一在通信上的性能指标作为权值的基础，链路两端路由器的平均值作为该链路的权值"""
        for start, target, data in tem_graph_slice_2.edges(data=True):
            data['weight'] = (self.core_routers[start].state[0][1] + self.core_routers[target].state[0][1]) / 2
        paths[2] = [nx.shortest_path(tem_graph_slice_2, source=source, target=target)
                    for source in slice_2_start_node for target in slice_2_target_node]
        paths[5] = [nx.shortest_path(tem_graph_slice_2, source=source, target=target)
                    for source in sensor_start_node for target in sensor_target_node]
        """以切片一在通信上的性能指标作为权值的基础，链路两端路由器的平均值作为该链路的权值"""
        for start, target, data in tem_graph_slice_3.edges(data=True):
            data['weight'] = (self.core_routers[start].state[0][2] + self.core_routers[target].state[0][2]) / 2
        paths[3] = [nx.shortest_path(tem_graph_slice_3, source=source, target=target)
                    for source in slice_3_start_node for target in slice_3_target_node]
        paths[6] = [nx.shortest_path(tem_graph_slice_3, source=source, target=target)
                    for source in sensor_start_node for target in sensor_target_node]
        return paths
