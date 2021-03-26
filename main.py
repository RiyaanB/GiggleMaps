import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


A = np.matrix([[0, 1, 1],
               [1, 0, 1],
               [1, 1, 100]])


G = nx.from_numpy_matrix(A)
nx.draw(G)
plt.show()
