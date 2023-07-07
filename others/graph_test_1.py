import random

import networkx as nx

G: nx.Graph = nx.read_graphml("../resource/graph.graphml")
"""读取出来的图的节点是字符串类型的，离谱！要更改节点的名字"""
relabel_table: dict = {
    number: int(number) for number in G.nodes
}
G: nx.Graph = nx.relabel_nodes(G, relabel_table)
start_node = 3
target_node = 11
num_paths = 1  # 需要选取的路径数量

all_paths = list(nx.all_simple_paths(G, start_node, target_node))
random_paths = random.sample(all_paths, num_paths)
print(random_paths)
