import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from Graph import Graph

B = Graph('graph.txt')
print(B.array)
G = nx.from_numpy_array(B.array)
labels = {}
nodes = list(G.nodes())
for i in range(len(nodes)):
    labels[nodes[i]] = B.names[i]
nx.draw(G, labels=labels, with_labels=True)
plt.show()


