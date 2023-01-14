import doctest

import networkx as nx
from typing import List

def build_graph(valuations: List[List[int]]):
    """
    This function implementation of Q5A :
    The preference-graph constructor for the indifference byte-swapping algorithm
    :param valuations:
    :return:
    >>> ex1 = [[10,15,20],[20,15,7],[5,3,80]]
    >>> ex2 = [[50,70,20,6],[90,43,7,44],[80,3,43,23],[12,24,44,71]]
    >>> ex3 = [[50,70,20,6,32],[90,43,7,44,22],[80,3,43,23,45],[12,24,44,71,123],[12,53,67,1,4]]
    >>> build_graph(ex1)
    True
    >>> build_graph(ex2)
    True
    >>> build_graph(ex3)
    False
    """
    g = nx.DiGraph()
    g.add_nodes_from(range(len(valuations)))
    edge_lst = [[(i, j) for j in range(len(valuations[i])) if valuations[i][j] == max(valuations[i])] for i in range(len(valuations))]
    # print(edge_lst)
    edge_lst = [val for sublist in edge_lst for val in sublist]
    # print(edge_lst)
    g.add_edges_from(edge_lst)
    return check_TSCC(g)

def check_TSCC(g: nx.DiGraph):
    """
    Checks if the graph has a finite strongly connected component
    :param g:
    :return:
    """
    sccs = nx.strongly_connected_components(g)
    for scc in sccs:
        if all(edge in g.edges() for edge in [(i, i) for i in scc]):
            for node in scc:
                out_edges = g.out_edges(node)
                if not any(edge[1] not in scc for edge in out_edges):
                    #print("The graph has a terminal strongly connected component.")
                    return True
    #print("The graph does not have a terminal strongly connected component.")
    return False

if __name__ == '__main__':
    doctest.testmod()
    # check_TSCC(build_graph([[10,15,20],[20,15,7],[5,3,80]]))