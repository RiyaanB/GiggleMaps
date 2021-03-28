import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from Graph import Graph




def draw(graph: Graph):
    G = nx.DiGraph(incoming_graph_data=graph.edges)

    for from_node, to_nodes in graph.edges.items():
        for to_node, value in to_nodes.items():
            G.edges[(from_node, to_node)]['weight'] = value

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)

    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_color='red',label_pos=0.2)
    plt.show()


if __name__ == '__main__':
    B = Graph("graph5.csv")
    draw(B)