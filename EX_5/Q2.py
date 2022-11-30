import doctest
import heapq
import math
import queue


class Graph:
    """
        The class of graph with strategy pattern
        >>> Graph([[0, 2, math.inf, math.inf],[math.inf, math.inf, 1, math.inf],[math.inf, math.inf, 0, 4],[1, math.inf, math.inf, 0]],dijkstra)
        Dijkstra Algo The Short Dist: 7 , And Path: [0, 1, 2, 3]
        >>> Graph([[0, 2, math.inf, 1],[math.inf, math.inf, 1, math.inf],[math.inf, math.inf, 0, 4],[1, math.inf, math.inf, 0]],dijkstra)
        Dijkstra Algo The Short Dist: 1 , And Path: [0, 3]
        >>> Graph([[0, 2, math.inf, 1],[math.inf, math.inf, 1, math.inf],[math.inf, math.inf, 0, 4],[1, math.inf, math.inf, 0]],floyd_warshall)
        Floyd Warshall Algo All Short Dist: [[0, 2, 3, 1], [6, 8, 1, 5], [5, 7, 0, 4], [1, 3, 4, 0]]
        >>> Graph([[0, 9, 5, math.inf],[9, 0, 2, 3],[5, 2, 0, math.inf],[math.inf, 3, math.inf, 0]],floyd_warshall)
        Floyd Warshall Algo All Short Dist: [[0, 7, 5, 10], [7, 0, 2, 3], [5, 2, 0, 5], [10, 3, 5, 0]]
    """

    def __init__(self, graph, algo=None):
        self.graph = graph
        self.algo = algo

    def algorithm(self, src=None, dest=None):
        if self.algo == dijkstra:
            return self.algo(self, src=0, dest=3)
        else:
            return self.algo(self)

    def __repr__(self):
        if self.algo == dijkstra:
            dist, path = self.algorithm()
            statment = "Dijkstra Algo The Short Dist: {} , And Path: {}"
            return statment.format(dist, path)
        else:
            arr = self.algorithm()
            return "Floyd Warshall Algo All Short Dist: "+str(arr)



def dijkstra(g, src, dest):
    """
    :param g: get Graph
    :param src: start vertex
    :param dest: end vertex
    :return: shortest path between src and dest with dijkstra algo , and the path
    >>> dijkstra(Graph([[0, 2, math.inf, math.inf],[math.inf, math.inf, 1, math.inf],[math.inf, math.inf, 0, 4],[1, math.inf, math.inf, 0]]),0,3)
    (7, [0, 1, 2, 3])
    >>> dijkstra(Graph([[0, 2, math.inf, 1],[math.inf, math.inf, 1, math.inf],[math.inf, math.inf, 0, 4],[1, math.inf, math.inf, 0]]),0,3)
    (1, [0, 3])
    """
    path = {src: -1}
    g.graph[src][src] = 0
    unvisited = []
    dist = [math.inf] * len(g.graph)
    dist[src] = 0
    for i in range(0, len(g.graph)):
        unvisited.append(i)
    heapq.heapify(unvisited)
    while len(unvisited) > 0:
        v = heapq.heappop(unvisited)
        for neighbour in range(0, len(g.graph[v])):
            w = dist[v] + g.graph[v][neighbour]
            if w < dist[neighbour]:
                dist[neighbour] = w
                heapq.heapify(unvisited)
                path[neighbour] = v
    temp = []
    i = dest
    while i != src:
        temp.append(i)
        i = path[i]
    temp.append(src)
    temp.reverse()
    return dist[dest], temp


def floyd_warshall(g):
    """
    :param g: graph
    :return: all dist in the graph
    >>> floyd_warshall(Graph([[0, 9, 5, math.inf],[9, 0, 2, 3],[5, 2, 0, math.inf],[math.inf, 3, math.inf, 0]]))
    [[0, 7, 5, 10], [7, 0, 2, 3], [5, 2, 0, 5], [10, 3, 5, 0]]
    >>> floyd_warshall(Graph([[0, 2, math.inf, 1], [math.inf, math.inf, 1, math.inf], [math.inf, math.inf, 0, 4],[1, math.inf, math.inf, 0]]))
    [[0, 2, 3, 1], [6, 8, 1, 5], [5, 7, 0, 4], [1, 3, 4, 0]]
    """
    n = len(g.graph)
    arr = g.graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (arr[i][j] > arr[k][j] + arr[i][k]):
                    arr[i][j] = arr[k][j] + arr[i][k]
    return arr


if __name__ == '__main__':
    graph1 = [[0, 2, math.inf, math.inf], [math.inf, math.inf, 1, math.inf], [math.inf, math.inf, 0, 4],
              [1, math.inf, math.inf, 0]]
    graph2 = [[0, 2, math.inf, 1], [math.inf, math.inf, 1, math.inf], [math.inf, math.inf, 0, 4],
              [1, math.inf, math.inf, 0]]
    graph3 = [[0, 9, 5, math.inf], [9, 0, 2, 3], [5, 2, 0, math.inf], [math.inf, 3, math.inf, 0]]
    doctest.testmod()
    print("Graph 1 : ", Graph(graph1, algo=dijkstra))
    print("Graph 2 : ", Graph(graph2, algo=dijkstra))
    print("Graph 1 : ", Graph(graph1, algo=floyd_warshall))
    print("Graph 2 : ", Graph(graph2, algo=floyd_warshall))
    print("Graph 3 : ", Graph(graph3, algo=floyd_warshall))
