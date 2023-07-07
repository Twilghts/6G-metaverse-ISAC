import random

import networkx as nx

G: nx.Graph = nx.read_graphml("../resource/graph.graphml")
"""读取出来的图的节点是字符串类型的，离谱！要更改节点的名字"""
relabel_table: dict = {
    number: int(number) for number in G.nodes
}
G: nx.Graph = nx.relabel_nodes(G, relabel_table)
for node in G.nodes:
    print(node)
for start, target, data in G.edges(data=True):
    data['weight'] = (start + target) / 2
for edge in G.edges(data=True):
    print(edge)
