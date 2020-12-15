import copy
import sys

from Transition import Transition


class NPDA:
    def __init__(self, transitions, init_stack, init_state='s0', input_str="", verbose=False):
        self.transitions: list[Transition] = transitions
        # self.stack = list(init_stack)
        # self.input_str = input_str
        # self.state = init_state
        self.state = Transition(init_state, input_str, list(init_stack))
        # self.current_states: list[Transition] = [Transition(init_state, '', self.stack[-1])]
        self.verbose = verbose


    def do_transitions(self):
        find_state = True
        # self.current_states = [Transition('s0', self.input_str[0], self.stack[-1])]

        # print("in transition")
        # print(self)
        while not self.state.is_finish() and find_state:
            find_state = False
            # empty = Transition(self.state.state, '', self.state.stack[-1])

            # print(self)
            # for state in self.current_states:
            for tr in self.transitions:
                if self.state.is_finish():
                    return True

                if tr == self.state:
                    find_state = True

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
                            ndpa = copy.deepcopy(self)
                            return ndpa.do_transitions()

                    else:
                        if tr.input:
                            self.state.input = self.state.input[1:]

                        state_to, add_to_stack = tr.get_transition()
                        self.state.state = state_to
                        self.state.stack.pop() #= self.state.stack.pop()
                        self.state.stack += add_to_stack
                    # del from stack and str

                    # self.state.input = self.state.input[0]
                    print(self)

            # if empty == self.state:
            #     find_state = True
            #     state_to, add_to_stack = tr.get_transition()
            #     self.state.state = state_to
            #     self.state.stack = self.state.stack.pop()
            #     self.stack += add_to_stack
            #     print(self)
            # self.do_transitions()

            if not find_state:
                print(self)
                print('такого состояния не существует')
                return False
                # sys.exit()

        if not self.input_str:
            return True
        else:
            return False

    def read_input(self, input):
        self.state.input = input
        print(self)
        if self.do_transitions():
            print("Dcё ок!!!")

    def __str__(self):
        # st = ''
        # for state in self.current_states:
        #     st += str(state)
        return f'Str: [{self.state.input}] Stack: {self.state.stack} Current transitions:'
