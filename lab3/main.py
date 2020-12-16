from NPDA import NPDA
from magic_pushdown_automation import do_npda
from parse.parse_file import parse_file, get_stack_symb_alphabet, make_transitions, MARKER_STACK

if __name__ == '__main__':
    rules, main_rules = parse_file('test2.txt')
    alphabet, stack_symb = get_stack_symb_alphabet(rules)

    transitions = make_transitions(main_rules, alphabet)
    automate = NPDA(transitions, (MARKER_STACK, 'E'), verbose=True)
    automate.read_input('a')



