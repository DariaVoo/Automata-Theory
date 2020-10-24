import networkx as nx


def check_deterministic(graph: nx.DiGraph):
    """ Проверяет какой это автомат
        @:returns
            @rvalue = True  Детерменированный автомат
            @rvalue = False Недетерменированный автомат

        Я определяю это посредством просмотра условий перехода.
        Если из одной вершины с одинаковым условием выходит несколько рёбер
        - это недетерменированный автомат.
    """
    for key_begin in graph.adj.keys():
        weigths = []
        for key_end in graph.adj[key_begin].keys():
            weigths.append(graph.adj[key_begin][key_end]['weigth'])
        if len(weigths) != len(set(weigths)):
            print("This is an Undetermined automaton!")
            return False

    print("This is an Determined automaton)")
    return True

