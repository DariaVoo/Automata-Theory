import copy
import sys

from Transition import Transition


class NPDA:
    def __init__(self, transitions, init_stack, init_state='s0', input_str="", verbose=False):
        self.transitions: list[Transition] = transitions

        self.state = Transition(init_state, input_str, list(init_stack))

        self.configurations: list[(str, str)] = []
        self.verbose = verbose

    def do_transitions(self):
        find_state = True

        while not self.state.is_finish() and find_state:
            find_state = False
            for tr in self.transitions:
                if self.state.is_finish():
                    return self

                if tr == self.state:
                    find_state = True

                    #   Если переход не однозначный, то запускаем рекурсивынй вызов в каждое состояние
                    if tr.get_count_to() > 1:
                        for right in tr.to:
                            if tr.input:
                                self.state.input = self.state.input[1:]

                            print(tr)

                            state_to, add_to_stack = right.state_to, right.add_to_stack
                            self.state.state = state_to
                            self.state.stack.pop()
                            self.state.stack += add_to_stack

                            print("to recursive")

                            # TODO: Сохранять состояния куда-то (возможно в лист состояний класса - kostil)
                            #  мб лучше возвращать его
                            self.configurations.append((self.state.get_state(), str(tr)))

                            ndpa = copy.deepcopy(self)
                            return ndpa.do_transitions()

                    else:
                        if tr.input:
                            self.state.input = self.state.input[1:]

                        state_to, add_to_stack = tr.get_transition()
                        self.state.state = state_to
                        self.state.stack.pop()
                        self.state.stack += add_to_stack

                        self.configurations.append((self.state.get_state(), str(tr)))

                    print(self)

            if not find_state:
                print(self)
                print('такого состояния не существует')
                # TODO: можно поменять его на None
                return None
                # sys.exit()

        if not self.input_str:
            return self
        else:
            return None

    

    def read_input(self, input):
        self.state.input = input
        print(self)
        ans = self.do_transitions()
        if ans is not None:
            print(ans.configurations)
            print("Вcё ок!!!")

    def __str__(self):
        # st = ''
        # for state in self.current_states:
        #     st += str(state)
        return f'State: {self.state.state} Str: [{self.state.input}] Stack: {self.state.stack}'
