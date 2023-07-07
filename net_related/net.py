from typing import Dict

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
        self.router_storage = [19060, 8763, 16297, 22901, 13735, 13530, 21507, 19683, 3692, 22855, 28427, 12424,
                               13628, 12968, 22011, 10952]
        self.router_calculate = [143, 167, 115, 196, 168, 135, 186, 53, 151, 47, 116, 107, 83, 80, 135, 165]
        self.router_bandwidth = [438, 520, 443, 458, 488, 525, 452, 483, 471, 496, 484, 488, 532, 509, 550, 433]
        """路由器组 为字典，键为路由器的编号，值为所对应的路由器,设置路由器内部可存储的数据容量。"""
        self.routers: Dict[int: Router] = {
            number: Router(number, storage=self.router_storage[number], computing_power=self.router_calculate[number],
                           bandwidth=self.router_bandwidth[number]) for number in self.G.nodes
        }
        # """更新图的边权值， 为其两头路由器容量之和的一半"""
        # for u, v in self.G.edges:
        #     self.G[u][v]['weight']: int = (self.routers[u].storage + self.routers[v].storage) // 2
        """网络连接组 为字典，键为起始路由器和终止路由器的元组，值为相对应的网络链接。"""
        self.links: Dict[tuple: Link] = {
            (start, target): Link((start, target)) for start, target in self.G.edges
        }

    def __repr__(self):
        pass

    def __str__(self):
        pass

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
