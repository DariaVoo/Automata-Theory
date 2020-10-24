from FSM import FSM


def analysis_str(str: str):
    state_machine = FSM()
    for ch in str:
        state_machine.send(ch)
    return state_machine.does_match()



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

