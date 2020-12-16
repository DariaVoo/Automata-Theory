class To:
    def __init__(self, state_to, to_stack: list):
        self.state_to = state_to
        self.add_to_stack = list(to_stack)

        # if '(' not in self.add_to_stack:
        #     self.add_to_stack.reverse()

    def __str__(self):
        str_to = ''
        for t in self.add_to_stack:
            str_to += str(t)
        return f'{self.state_to}, {str_to}'


class Transition:
    def __init__(self, state: str, input: str, stack: str, state_to: str = '', to_stack: list = None):
        self.state = state
        self.input = input
        self.stack = stack

        self.to = []
        self.add_to(state_to, to_stack)

    def is_finish(self):
        return not self.stack and not self.input

    def get_state(self):
        return f'State: {self.state} Str: [{self.input}] Stack: {self.stack}'

    def add_to(self, state_to, to_stack):
        if to_stack is None:
            self.to.append(To(state_to, ''))
            return

        for l in to_stack:
            self.to.append(To(state_to, l))

    def get_count_to(self):
        return len(self.to)

    def get_transition(self):
        return self.to[0].state_to, self.to[0].add_to_stack

    def __eq__(self, other):
        return self.state == other.state and (self.input == other.input or self.input == '') and self.stack == other.stack[-1]

    def __str__(self):
        str_to = self.to[0].state_to + ', '
        for t in self.to:
            str_to += str(t.add_to_stack)
        return f'O({self.state}, {self.input}, {self.stack}) -> ({str_to})'


class Rule:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def add_right(self, right):
        buf = right
        self.right = [right]
        self.right.append(right)

    def __str__(self):
        return f"{self.left} -> {self.right}"
