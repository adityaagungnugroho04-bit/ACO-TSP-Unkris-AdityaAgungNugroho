import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [
    ("A","#",3),
    ("A","C",6),
    ("#","C",2),
    ("#","G",5),
    ("C","F",4),
    ("F","E",2),
    ("D","E",7),
    ("B","C",9),
    ("B","D",8),
    ("D","H",9),
    ("E","H",1),
    ("E","G",1),
    ("G","H",3)
]

for u,v,w in edges:
    G.add_edge(u,v,weight=w)

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2500
)

labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Traveling Salesman Graph")
plt.show()
