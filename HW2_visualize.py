'''
Visualize tool for 2018 Network Theory HW#2
Created in Oct. 4th(Thu) by JuneTech
'''
import networkx as nx
import matplotlib.pyplot as plt

def show_path_among_graph(G, path):
    path_edges = list(zip(path[:-1], path[1:]))
    pos = nx.get_node_attributes(G, "pos")
    nx.draw_networkx(G, pos)
    nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
    nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=3)
    labels = nx.get_edge_attributes(G, "distance")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.axis('equal')
    plt.show()

import nt_hw2_20162338
G = nt_hw2_20162338.read_json_return_graph("example_graph.json")
path = nt_hw2_20162338.return_cycle(G)

show_path_among_graph(G, path)
