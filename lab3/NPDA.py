import copy
import sys

from Transition import Transition


class NPDA:
    def __init__(self, transitions, init_stack, init_state='s0', input_str="", verbose=False):
        self.transitions: list[Transition] = transitions
        self.stack = list(init_stack)
        self.input_str = input_str
        self.state = init_state
        self.current_states: list[Transition] = [Transition(init_state, '', self.stack[-1])]
        self.verbose = verbose

    def do_transitions(self):
        find_state = True
        # self.current_states = [Transition('s0', self.input_str[0], self.stack[-1])]

        while find_state:
            find_state = False

            for tr in self.transitions:
                for state in self.current_states:
                    empty = Transition(state.state, '', self.stack[-1])
                    if tr == state:
                        find_state = True

                        if tr.get_count_to() > 1:
                            for right in tr.to:
                                if tr.input:
                                    self.input_str = self.input_str[1:]

                                state_to, add_to_stack = right.state_to, right.add_to_stack
                                state.state = state_to
                                state.stack = self.stack.pop()
                                self.stack += add_to_stack

                                print("to recursive")
                                ndpa = copy.deepcopy(self)
                                return ndpa.do_transitions()

                        else:
                            if tr.input:
                                self.input_str = self.input_str[1:]

                            state_to, add_to_stack = tr.get_transition()
                            state.state = state_to
                            state.stack = self.stack.pop()
                            self.stack += add_to_stack
                        # del from stack and str

                        state.input = self.input_str[0]
                        print(self)
                    elif empty == tr:
                        find_state = True
                        state_to, add_to_stack = tr.get_transition()
                        state.state = state_to
                        state.stack = self.stack.pop()
                        self.stack += add_to_stack
                        print(self)
            # self.do_transitions()

            if not find_state:
                print(self)
                print('такого состояния не существует')
                return False
                # sys.exit()
        return True

    def read_input(self, input):
        self.input_str = input
        print(self)
        if self.do_transitions():
            print("Dcё ок!!!")

    def __str__(self):
        st = ''
        for state in self.current_states:
            st += str(state)
        return f'Str: {self.input_str} Stack: {self.stack} Current transitions: {st}'
