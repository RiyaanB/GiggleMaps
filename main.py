import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from dijkstra import Graph


A = np.matrix([[1, 1, 1, 0],
               [1, 2, 1, 0],
               [1, 2, 3, 0],
               [1, 0, 0, 4],
               ])
B = Graph('graph.txt')
print(B.array)
G = nx.from_numpy_array(B.array)
nx.draw(G)
plt.show()

