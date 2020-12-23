class Command:
    """ Вспомогательный класс ключевыъ слов анализатора """
    def __init__(self, str_command, fun):
        self.command: str = str_command
        self.fun = fun


class For:
    def __init__(self, counter_name, counter, target, index_begin, type_for):
        self.counter_name
        self.counter: int
        self.target: int
        self.index_begin: int
        self.step = 0
        self.set_step(type_for)

    def set_step(self, type_for):
        if type_for == 'to':
            self.step = 1
        elif type_for == 'downto':
            self.step = -1
        else:
            print('Uncorrect type of for! Avaliable: to, downto')