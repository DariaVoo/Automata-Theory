import networkx as nx
import matplotlib.pyplot as plt


def draw(graph: nx.DiGraph):
    plt.rcParams.update({'font.size': 25, 'font.weight': 'bold'})
    nx.draw_circular(graph,
                     with_labels=True,
                     # node_color=color_map,
                     node_size=110)
    plt.show()
