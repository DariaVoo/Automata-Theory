class Command:
    """ Вспомогательный класс ключевыъ слов анализатора """
    def __init__(self, str_command, fun):
        self.command: str = str_command
        self.fun = fun


class For:
    def __init__(self):
        self.counter: int
        self.target: int
        self.index_begin: int