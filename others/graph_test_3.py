import networkx as nx
from matplotlib import pyplot as plt

G: nx.Graph = nx.read_graphml("../resource/graph.graphml")
"""读取出来的图的节点是字符串类型的，离谱！要更改节点的名字"""
relabel_table: dict = {
    number: int(number) for number in G.nodes
}
G: nx.Graph = nx.relabel_nodes(G, relabel_table)
for num_node in range(16, 34):
    G.add_node(num_node)

for num_edge in range(16, 32):
    if num_edge < 24:
        G.add_edge(num_edge, 32)
    else:
        G.add_edge(num_edge, 33)

G.add_edge(32, 0)
G.add_edge(33, 1)

# 使用spring布局绘制图形
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=60, font_size=6, width=1)

# 添加显示权重的边标签
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# 显示绘图
plt.show()

# Save the graph to a GraphML file
nx.write_graphml(G, "../resource/graph_2.graphml")