class To:
    def __init__(self, state_to, to_stack: list):
        """
        Информация о состоянии, в которое мы переходим и что мы кладём на стек.
        :param state_to: состояние, в которое мы переходим
        :param to_stack: символы, которые мы закидываем на стек
        """
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
        """
        Правило перехода
        :param state: текущее состояние (из которого переходим)
        :param input: текущее состояние входной ленты (текущий символ считывается из ленты в алгоритме, по дефолту это конец ленты)
        :param stack: текущее состояние стека
        :param state_to: куда переходим
        :param to_stack: что добавляем в магазин, при переходе
        """
        self.state = state
        self.input = input
        self.stack = stack

        self.to = []
        self.add_to(state_to, to_stack)

    def is_finish(self):
        return not self.stack and not self.input

    def get_state(self):
        """ Получение текущего состояния в строковом представлении """
        return f'State: {self.state} Str: [{self.input}] Stack: {self.stack}'

    def add_to(self, state_to, to_stack):
        """
        Добавляем переходы
        (в случае неоднозначного перехода, есть несколько состояний в которые мы преходим)
        :param state_to:
        :param to_stack:
        :return: None
        """
        if to_stack is None:
            self.to.append(To(state_to, ''))
            return

        for l in to_stack:
            self.to.append(To(state_to, l))

    def get_count_to(self):
        return len(self.to)

    def get_transition(self):
        """ Получение параметров в случае однозначного перехода """
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
        """
        Правило в строковом представлении
        :param left: левая часть правила - откуда переходим
        :param right: правая часть правила(куда переходим) - лист, поскольку автомат недетерменированнный
        """
        self.left = left
        self.right = right
        self.terminals = None
        self.nonterminals = None

    def add_right(self, right):
        self.right = [right]
        self.right.append(right)

    def __str__(self):
        return f"{self.left} -> {self.right}"
