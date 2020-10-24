import networkx as nx


def analysis_str(instr: str, graph: nx.DiGraph):
    """ Анализ строки akmc
    """
    print(graph.adj)
    current_state = prev_state = 'q0'
    for char in instr:
        print(current_state, f'-{char}->', end=' ')
        for key in graph.adj[current_state].keys():
            prev_state = current_state
            if char == graph.adj[current_state][key]['weigth']:
                current_state = key
                break
        if current_state == prev_state:
            print(f"Invalid str: you can't go anythere from state {current_state} by send {char}")
            return
        if current_state.startswith('f'):
            print("You have arrived at the final state ", current_state)
            return

    print("You have arrived at the state ", current_state)
