'''
Making random graphs into csv or json
'''
import networkx as nx
import random

DIRECTED = False #True
NODECOUNT = 240
EDGECOUNT = 576
COST_RANGE = (1,300)
FILENAME = "nt_hw4_graph3.json"

def draw_graph_with_edgecost(G):
    '''
    Draw networkx graph with edge cost attribute
    '''
    import matplotlib.pyplot as plt
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, "cost")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def export_json_graph(filename, nodecount, edgecount, direct_bool, cost_range):
    '''
    Makes file of json representing random graph
    '''
    rand_graph = nx.gnm_random_graph(nodecount,
                                     edgecount,
                                     directed=direct_bool)
    for edge in rand_graph.edges():
        print(edge[0], edge[1])
        rand_graph[edge[0]][edge[1]]["cost"] = random.randint(cost_range[0], cost_range[1])

    import json
    from networkx.readwrite import json_graph
    with open(filename, 'w') as outfile:
        json.dump(json_graph.node_link_data(rand_graph), outfile, indent=4)
    
    draw_graph_with_edgecost(rand_graph)

def main():
    export_json_graph(FILENAME, NODECOUNT, EDGECOUNT, DIRECTED, COST_RANGE)

if __name__ == '__main__':
    main()
