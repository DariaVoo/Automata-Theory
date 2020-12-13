class Transition:
    def __init__(self, state: str, input: str, stack: str, state_to: str='', to_stack: str=''):
        self.state = state
        self.input = input
        self.stack = stack

        self.state_to = state_to
        self.add_to_stack = list(to_stack)
        self.add_to_stack.reverse()

        self.magazine = []

    def get_transition(self,):
        print(f"Do transition: {str(self)}\n")
        return self.state_to, self.add_to_stack
        #
        # self.state = state_to
        #
        # if not add_to_stack:
        #     self.magazine.pop()
        # else:
        #     self.magazine += list(add_to_stack)

    def __eq__(self, other):
        return self.state == other.state and self.input == other.input and self.stack == other.stack

    def __str__(self):
        return f'O({self.state}, {self.input}, {self.stack}) -> ({self.state_to}, {self.add_to_stack})'


class Rule:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left} -> {self.right}"
