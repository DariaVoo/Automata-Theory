from logic import get_first, get_follow
from parse.parse_file import parse_file, get_terminals_and_non, make_transitions

if __name__ == '__main__':

    rules, main_rules = parse_file('grammar')
    terminals, nonterminals = get_terminals_and_non(main_rules)
    dict_rule = make_transitions(main_rules)
    get_first(main_rules, dict_rule)
    get_follow(main_rules, dict_rule)
