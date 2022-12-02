import doctest
import networkx as nx
from typing import List
import matplotlib.pyplot as plt

counter = 0


def find_cycle_in_consumption_graph(allocation: List[List[float]]):
    """
            >>> find_cycle_in_consumption_graph([[1, 1, 0.07, 0],[0, 0, 0.93, 1]])
            'no cycle'
            >>> find_cycle_in_consumption_graph([[1, 1, 0.25, 0],[0, 0, 0.75, 0.5],[0, 0, 0.25, 0.5]])
            [1, 6, 2, 5, 1]
            >>> find_cycle_in_consumption_graph([[1, 0.5, 0.25, 0],[0, 0, 0.75, 0.5],[0, 0, 0.25, 0.5],[0, 0.5, 0, 0]])
            [1, 7, 2, 6, 1]
            >>> find_cycle_in_consumption_graph([[0.5, 1, 0, 0],[0, 0, 1, 0.4],[0.5, 0, 0, 0.6]])
            'no cycle'
            >>> find_cycle_in_consumption_graph([[1, 0, 0, 0.25, 0.25, 0.5],[0, 1, 0, 0.5, 0.25, 0.25],[0, 0, 1, 0.25, 0.5, 0.25],])
            [6, 2, 8, 0, 6]
            """
    global counter
    counter += 1
    g = nx.Graph()
    g.add_nodes_from(range(0, len(allocation)), bipartite=0)
    g.add_nodes_from(range(len(allocation), len(allocation[0]) + len(allocation)), bipartite=1)
    for i in range(0, len(allocation)):
        for k in range(0, len(allocation[i])):
            if allocation[i][k] > 0:
                g.add_edge(i, len(allocation) + k)
    X, Y = nx.bipartite.sets(g)
    pos = dict()
    pos.update((n, (1, i)) for i, n in enumerate(X))  # put nodes from X at x=1
    pos.update((n, (2, i)) for i, n in enumerate(Y))  # put nodes from Y at x=2
    plt.title(label=f"Drawing {counter}", color="green")
    nx.draw(g, pos=pos, with_labels=True)
    plt.show()
    for i in range(0, len(allocation)):
        temp = nx.cycle_basis(g, i)
        if temp:
            temp[0].append(temp[0][0])
            return temp[0]
    return "no cycle"


if __name__ == '__main__':
    graph1 = [[1, 1, 0.07, 0],
              [0, 0, 0.93, 1]]
    graph2 = [[1, 1, 0.25, 0],
              [0, 0, 0.75, 0.5],
              [0, 0, 0.25, 0.5]]
    graph3 = [[1, 0.5, 0.25, 0],
              [0, 0, 0.75, 0.5],
              [0, 0, 0.25, 0.5],
              [0, 0.5, 0, 0]]
    graph4 = [[0.5, 1, 0, 0],
              [0, 0, 1, 0.4],
              [0.5, 0, 0, 0.6]]
    graph5 = [[1, 0, 0, 0.25, 0.25, 0.5],
              [0, 1, 0, 0.5, 0.25, 0.25],
              [0, 0, 1, 0.25, 0.5, 0.25],
              ]
    doctest.testmod()

    print("Drawing 1 graph 1 ----> ", find_cycle_in_consumption_graph(graph1))
    print("Drawing 2 graph 2 ----> ", find_cycle_in_consumption_graph(graph2))
    print("Drawing 3 graph 4 ----> ", find_cycle_in_consumption_graph(graph4))
