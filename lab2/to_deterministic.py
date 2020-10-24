import networkx as nx


def to_deterministic(graph: nx.DiGraph):
    """ Перевод из недетерминированного автомата в детерминированный

        @:return nx.DiGraph - недетерминированный автомат
    """
    new_graph = nx.DiGraph()
    join_vertex = []

    print("Joint vertexes: ", end='')
    for key_begin in graph.adj.keys():
        begin = key_begin

        for v in join_vertex:
            if v.find(key_begin) != -1:
                begin = v

        weigths = {}
        for key_end in graph.adj[key_begin].keys():
            w = graph.adj[key_begin][key_end]['weigth']
            # is_not_loop = begin.find(key_end) == -1
            # is_not_loop = True

            if w not in weigths.keys():
                weigths[w] = []
            # if is_not_loop:  # не петля
            weigths[w].append(key_end)

        # print(weigths)
        for key_w in weigths:
            if len(weigths[key_w]) > 1:
                # end = ''
                # for w in weigths[key_w]:
                #     for v in join_vertex:   # Проверяем, что вершина ещё не объединена
                #         if v.find(w) == -1:
                #             end += w
                #     if len(join_vertex) == 0:
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

    return new_graph
