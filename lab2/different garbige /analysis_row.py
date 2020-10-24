from FSM import FSM


def analysis_str(str: str):
    state_machine = FSM()
    for ch in str:
        state_machine.send(ch)
    return state_machine.does_match()
