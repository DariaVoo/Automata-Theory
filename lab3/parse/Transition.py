class Transition:
    def __init__(self, state: str, input: str, stack: str, state_to: str, to_stack: str):
        self.state = state
        self.input = input
        self.stack = stack

        self.state_to = state_to
        self.add_to_stack = set(to_stack)

    def do_transition(self):
        pass

    def __str__(self):
        return f'O({self.state}, {self.input}, {self.stack}) -> ({self.state_to}, {self.add_to_stack})'


class Rule:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left} -> {self.right}"
