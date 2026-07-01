import matplotlib.pyplot as plt
import networkx as nx

coordinates = {
    'A': (0, 6), 'B': (2, 8), 'C': (1, 3), 'D': (3, 4),
    'E': (2, 1), 'F': (4, 7), 'G': (6, 2), 'H': (7, 1), 'I': (8, 2)
}

edges = [
    ('A', 'B', 2.82),
    ('A', 'C', 3.16),
    ('C', 'D', 2.23),
    ('C', 'F', 5.0),
    ('D', 'E', 2.24),
    ('D', 'G', 3.6),
    ('D', 'H', 4.47),
    ('G', 'H', 1.0),
    ('G', 'I', 2.0),
    ('H', 'I', 1.0),
]

G = nx.Graph()
for node, pos in coordinates.items():
    G.add_node(node, pos=pos)
for n1, n2, w in edges:
    G.add_edge(n1, n2, weight=w)

pos = nx.get_node_attributes(G, 'pos')

plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        node_size=800, font_size=12, font_weight='bold')

edge_labels = {(n1, n2): w for n1, n2, w in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels)

plt.title("A* Graph")
plt.show()