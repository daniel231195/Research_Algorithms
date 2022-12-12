import math
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def find_max_len_cliques(graph):
    """
    We take all cliques from graph with networkx algorithm
    :param graph:  random undirected graph -> G(n,p)
    :return: The max length of cliques
    """
    cliques = nx.find_cliques(graph)
    max_len = -math.inf
    arr = []
    for i in cliques:
        if max_len < len(i):
            arr = i
            max_len = len(i)
    return arr


def find_apx_theory(n):
    """
     Calculation of the theoretical approximation ratio : O(|V| / (log |V|)^2)
    :param n: |V|
    :return: |V| / (log |V|)^2
    """
    log = math.log(n, 2)
    log = math.pow(log, 2)
    return (n / log)


def apx_of_max_cliques(n, p):
    """
        We use in approximation algorithm for find the max length ,
        the algorithm take from networkx.
        We get number of vertex |V| and random probability , build random undirected graph and calculate
        the max length cliques
    :param n: |V|
    :param p: probability for edge
    :return: approximation of max length of clique
    """
    graph = nx.gnp_random_graph(n, 0.5)
    apx_max_cliques = list(nx.approximation.max_clique(graph))
    real_max_cliques = find_max_len_cliques(graph)
    apx_theory = find_apx_theory(n)
    return abs(len(apx_max_cliques) - len(real_max_cliques)), round(apx_theory, 3)


def draw_graph(res):
    """
    I take the code of plot form this web
    https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html
    :param res:
    :return: plot of apx graph
    """
    arr = []
    real_apx_ratio = []
    theoretical_apx_ratio = []
    for i in res:
        arr.append(i[0])
        real_apx_ratio.append(i[1][0])
        theoretical_apx_ratio.append(i[1][1])
    x = np.arange(len(arr))  # the label locations
    width = 0.15  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, real_apx_ratio, width, label='real apx ratio')
    rects2 = ax.bar(x + width / 2, theoretical_apx_ratio, width, label='theoretical apx ratio')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('apx ratio')
    ax.set_xlabel('G(n,p)')
    ax.set_title('Comparison of approximation ratio results')
    ax.set_xticks(x)
    ax.set_xticklabels(arr, rotation=270)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', rotation=270)

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.show()


def run_Q2():
    """
        We rand random probability and send apx_of_max_cliques func
        and get the ans from this func .
        We check 40 time this calculate with random probability and different number of node in range 1-50
    :return:
    """
    res = []
    print("Running....", end="")
    for n in range(1, 41):
        print(f"{n}...", end=""),
        random.seed(n)
        p = round(random.uniform(0, 1), 1)
        x = []
        x.append((n * 10, p))
        x.append(apx_of_max_cliques(n * 10, p))
        res.append(x)
    print()
    print("Finish Run")
    draw_graph(res)


if __name__ == '__main__':
    run_Q2()
