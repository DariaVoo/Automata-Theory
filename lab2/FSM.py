class FSM:
    def __init__(self):
        self.current_state = None
        self.stopped = False
        self.stop_state = None

    def setstate(self, state):
        self.current_state = state

    def send(self, char: str):
        """ Отправляет текущий ввод в current_state.
            Захватывает исключение ставит флаг stopped - неверный ввод
        """
        try:
            self.current_state.send(char)
        except StopIteration:
            self.stopped = True

    def does_match(self):
        """ Вовращает True, если текущее состояние можно разобрать этим автоматом.
            Если нет или получили неверный ввод возвращаем False
        """
        if self.stopped:
            return False
        return self.current_state == self.stop_state

    def _create_state(self):
        while True:
            # После получения ввода, сохраняем его в переменну char
            char = yield

            if char == 'b':
                self.current_state = self.q2
            else:
                # При получении невалидного ввода останавливаем цикл,
                # чтобы в следующий раз вызвать StopIteration
                break
