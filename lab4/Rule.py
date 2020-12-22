import copy


class Rule:
    def __init__(self, left, right):
        """
        Правило в строковом представлении
        :param left: левая часть правила - откуда переходим
        :param right: правая часть правила(куда переходим) - лист, поскольку автомат недетерменированнный
        :param terminals: множество терминалов правила
        :param nonterminals: множество нетерминалов
        """
        self.left: str = left
        self.right: list = right
        self.terminals: list = []
        self.nonterminals: list = []
        self.first_in_right: list = []

    def add_right(self, right):
        self.right = [right]
        self.right.append(right)

    def create_new_gen_rule(self, template, nonterm, nonterms):
        new_right = []

        for r in self.right:
            new_r = template.replace(nonterm, r)
            new_right.append(new_r)

        new_nonterms = copy.deepcopy(nonterms)
        new_nonterms.remove(nonterm)
        return new_right, new_nonterms

    def __str__(self):
        return f"{self.left} -> {self.right}"
