from NPDA import NPDA
from magic_pushdown_automation import do_npda
from parse.parse_file import parse_file, get_stack_symb_alphabet, make_transitions, MARKER_STACK

if __name__ == '__main__':
    rules, main_rules = parse_file('test2.txt')
    alphabet, stack_symb = get_stack_symb_alphabet(rules)

    transitions = make_transitions(main_rules, alphabet)
    automate = NPDA(transitions, (MARKER_STACK, 'E'))
    automate.read_input('a+a*a')


    # states_dir = main_make_transitions(rules, alphabet, main_rules)
    #
    # automate = do_npda(alphabet, stack_symb, states_dir)
    #
    # # if automate.accepts_input('a+a*a'):
    # #     print('accepted')
    # # else:
    # #     print('rejected')
    #
    # ret = automate.read_input_stepwise('a+a*a')
    # for state in ret:
    #     print(state)


