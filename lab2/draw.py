import networkx as nx
import matplotlib.pyplot as plt


def draw(graph: nx.DiGraph):
    nx.draw_circular(graph,  # pos=nodes,
                     with_labels=False,
                     # node_color=color_map,
                     node_size=20)
    plt.show()
