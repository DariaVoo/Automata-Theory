import networkx as nx


def to_deterministic_it(graph: nx.DiGraph):
    """ Перевод из недетерминированного автомата в детерминированный

        @:return nx.DiGraph - недетерминированный автомат
    """
    new_graph = nx.DiGraph()
    join_vertex = []

    print("Joint vertexes: ", end='')
    for key_begin in graph.adj.keys():  # идём по всем вершинам
        begin = key_begin
        weigths = {}
        for key_end in graph.adj[key_begin].keys():
            w = graph.adj[key_begin][key_end]['weight']
            if w not in weigths.keys():
                weigths[w] = []
            weigths[w].append(key_end)

        for key_w in weigths:
            if len(weigths[key_w]) > 1:
                end = ''.join(map(str, weigths[key_w]))
                print(end, end=' ')
                # check внутренние вершины
                for v in weigths[key_w]:
                    for k in join_vertex:   # Проверяем входит ли этот переход в граф
                        if k.find(v) != -1 and new_graph.adj[k][v]['weight'] == key_w:
                            new_graph.remove_edge(k, v)
                            new_graph.remove_node(v)

                    for u in weigths[key_w]:
                        if v != u and (v, u) in graph.edges:
                            new_graph.add_edge(end, u, weight=graph.adj[v][u]['weight'])

                join_vertex.append(end)
            else:
                end = weigths[key_w][0]

            # Проверяем входит ли эта вершина в объединённые
            begin_j = begin
            if begin not in new_graph.nodes:
                for v in join_vertex:
                    if v.find(key_begin) != -1:
                        begin_j = v
                        break
            end_j = end
            if end not in new_graph.nodes:
                for v in join_vertex:
                    if v.find(end) != -1:
                        end_j = v
                        break

            # # Если это не петля
            # if begin != end and begin_j == end_j:
            #     new_graph.add_edge(begin_j, end, weight=key_w)
            # else:
            new_graph.add_edge(begin_j, end_j, weight=key_w)

    print()
    return new_graph
