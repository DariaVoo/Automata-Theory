import networkx as nx


def to_deterministic(graph: nx.DiGraph):
    """ Перевод из недетерминированного автомата в детерминированный

        @:return nx.DiGraph - недетерминированный автомат
    """
    new_graph = nx.DiGraph()
    join_vertex = []

    for key_begin in graph.adj.keys():
        begin = key_begin

        for v in join_vertex:
            if v.find(key_begin) != -1:
                begin = v

        weigths = {}
        for key_end in graph.adj[key_begin].keys():
            w = graph.adj[key_begin][key_end]['weigth']
            is_not_loop = begin.find(key_end) == -1

            if w not in weigths.keys() and is_not_loop:
                weigths[w] = []
            if is_not_loop:  # не петля
                weigths[w].append(key_end)

        # print(weigths)
        for key_w in weigths:
            if len(weigths[key_w]) > 1:
                end = ''.join(map(str, weigths[key_w]))
                join_vertex.append(end)
                print(end)
                new_graph.add_edge(begin, end, weigth=key_w)
            else:
                end = weigths[key_w][0]
                for v in join_vertex:
                    if v.find(end) != -1:
                        end = v
                new_graph.add_edge(begin, end, weigth=key_w)

    # print(new_graph.adj)
    return new_graph