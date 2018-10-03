'''
Sample for 2018 Network Theory HW#2
Created in Oct. 4th(Thu) by JuneTech
'''
import networkx as nx

def read_json_return_graph(filename):
    '''
    Reads JSON file of graph information, returns nx.Graph instance
    '''
    import json
    with open(filename) as f:
        js_graph = json.load(f)
    return nx.readwrite.json_graph.node_link_graph(js_graph, multigraph=False)

def return_cycle(G):
    return [1, 2, 4, 1]