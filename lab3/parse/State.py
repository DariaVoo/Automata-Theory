class State():
    state: str
    stack: list


class Rule:
    def __init__(self, left, right):
        self.left = left
        self.right = right
