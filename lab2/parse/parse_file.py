import re

from parse.file_op import read_file
import networkx as nx
import matplotlib.pyplot as plt

class State:
    """ Состояние автомата
        @n_state - номер состояния
        @type_state - тип состояния f - конечное q - обычное
        @condition - условие перехода в это состояние
    """
    def __init__(self, num_state: int, type_state: str, condition: str):
        self.n_state = num_state
        self.type_state = type_state
        self.condition = condition
        self.edges = []

def draw(graph: nx.DiGraph):
    nx.draw_circular(graph,  # pos=nodes,
                     with_labels=False,
                     # node_color=color_map,
                     node_size=20)
    plt.show()


def create_graph(transitions: str):
    graph = nx.DiGraph()

    for word in transitions:
        states = re.findall(r'[qf]\d+', word)
        condition = re.findall(r',.=', word)
        condition = condition[0][1:-1]
        graph.add_edge(states[0], states[-1], weight=condition)

    print(graph.nodes)
    print(graph.edges)
    return graph


def parse_file(file_name):
    transitions = set(read_file(file_name).split(sep='\n'))
    transitions.remove("")
    transitions = sorted(list(transitions))

    valid = [re.fullmatch(r'q\d+,.=[qf]\d+', s) for s in transitions]
    if None in valid:
        print("Invalid transitions:", transitions[valid.index(None)])
        return None

    create_graph(transitions)

