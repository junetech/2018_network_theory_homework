'''
Reading file of graph & displaying by networkx
Created in 1. Oct. 2018 by JuneTech
'''
import json
import networkx as nx

def read_json_file(filename):
    '''
    Reads json file & returns networkx graph instance
    '''
    with open(filename) as f:
        js_graph = json.load(f)
    return nx.readwrite.json_graph.node_link_graph(js_graph)

def draw_graph_with_edgecost(G):
    '''
    You may be happy by using this...
    Draw networkx graph with edge cost attribute
    '''
    import matplotlib.pyplot as plt
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, "cost")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def solve(filename):

    # TA comment: start by reading json file into networkx graph
    nx_graph = read_json_file(filename)
    '''
    for the reference of accessing edge weights!
    you had better delete those two lines before submission
    '''
    for edge in nx_graph.edges():
        print("edge", edge, "have cost of", nx_graph[edge[0]][edge[1]]["cost"])

    '''just use it when you are interested
    import matplotlib.pyplot as plt
    draw_graph_with_edgecost(nx_graph)
    '''


def main():
    solve("nt_hw4_graph1.json")

if __name__ == '__main__':
    main()
