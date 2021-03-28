import networkx as nx
import matplotlib.pyplot as plt
from utils.Graph import Graph

B = Graph('test_graphs/graph.csv')

def plot_graph(B, show=True, save=False):

    G = nx.to_directed(nx.to_networkx_graph(B.edges, multigraph_input=True))

    for from_node, to_nodes in B.edges.items():
        for to_node, value in to_nodes.items():
            G.edges[(from_node, to_node)]['weight'] = value

    pos = nx.spring_layout(G)
    nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
    edge_labels = nx.get_edge_attributes(G,'weight') # key is edge, pls check for your case
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_color='red',label_pos=0.2)

    if show:
        plt.show()

    if save:
        plt.savefig("graph_img_outputs/Weighted Graph.png")



