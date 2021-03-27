import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from Graph import Graph


def draw(filename):
    B = Graph(filename)

    G = nx.to_directed(nx.to_networkx_graph(B.edges, multigraph_input=True))

    for from_node, to_nodes in B.edges.items():
        for to_node, value in to_nodes.items():
            G.edges[(from_node, to_node)]['weight'] = value

    pos = nx.spring_layout(G)
    nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
    edge_labels = nx.get_edge_attributes(G,'weight') # key is edge, pls check for your case
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_color='red',label_pos=0.2)
    plt.show()


if __name__ == '__main__':
    draw('graph2.txt')