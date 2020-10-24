import re

from parse.file_op import read_file
import networkx as nx


def create_graph(transitions: str):
    graph = nx.DiGraph()

    for word in transitions:
        states = re.findall(r'[qf]\d+', word)
        condition = re.findall(r',.=', word)
        condition = condition[0][1:-1]
        graph.add_edge(states[0], states[-1], weight=condition)

    # print(graph.nodes)
    # print(graph.edges)
    return graph


def parse_file(file_name):
    transitions = set(read_file(file_name).split(sep='\n'))
    transitions.remove("")
    transitions = sorted(list(transitions))

    valid = [re.fullmatch(r'q\d+,.=[qf]\d+', s) for s in transitions]
    if None in valid:
        print("Invalid transitions:", transitions[valid.index(None)])
        return None

    return create_graph(transitions)

