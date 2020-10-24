import networkx as nx

from parse.file_op import write_file


def graph_to_file(graph: nx.DiGraph, file_name: str):
    data: str = ''
    for begin, end, w in graph.edges.data('weigth'):
        data += f'{begin},{w}={end}\n'
    write_file(file_name, data)
    print("The new determined automaton is written to a file:", file_name)
    # print(data)
