import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


A = np.matrix([[1, 1, 1],
               [1, 2, 1],
               [1, 2, 3]])
G = nx.from_numpy_matrix(A)
nx.draw(G)
plt.show()
