import networkx as nx


def to_deterministic(graph: nx.DiGraph):
    """ TODO: ПЕРЕДЕЛАТЬ
    Перевод из недетерминированного автомата в детерминированный

        @:return nx.DiGraph - недетерминированный автомат
    """
    new_graph = nx.DiGraph()
    join_vertex = []
    print(graph.adj)

    print("Joint vertexes: ", end='')
    for key_begin in graph.adj.keys():
        begin = key_begin

        if begin in new_graph.nodes:
            print(new_graph.adj.keys())
            for v in join_vertex:
                if v.find(key_begin) != -1:
                    begin = v

        weigths = {}
        for key_end in graph.adj[key_begin].keys():
            w = graph.adj[key_begin][key_end]['weight']
            # is_not_loop = begin.find(key_end) == -1
            # is_not_loop = True

            if w not in weigths.keys():
                weigths[w] = []
            # if is_not_loop:  # не петля
            weigths[w].append(key_end)

        # print(weigths)
        for key_w in weigths:
            if len(weigths[key_w]) > 1:
                # # Проверяем, что вершина ещё не объединена
                # end = ''
                # for w in weigths[key_w]:
                #     for v in join_vertex:
                #         if v.find(w) == -1:
                #             end += w
                #         else:
                #             end += w[-1]    # добавляем только цифру состояния
                #     if len(join_vertex) == 0:
                end = ''.join(map(str, weigths[key_w]))
                join_vertex.append(end)
                print(end, end=' ')
                new_graph.add_edge(begin, end, weight=key_w)
            else:
                end = weigths[key_w][0]
                # for v in join_vertex:
                #     if v.find(end) != -1:
                #         end = v
                new_graph.add_edge(begin, end, weight=key_w)
    print()
    return new_graph
