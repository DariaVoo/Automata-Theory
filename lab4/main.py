from first import get_first
from follow import get_follow
from logic import make_table
from parse.parse_file import parse_file, get_terminals_and_non, make_transitions

if __name__ == '__main__':

    rules, main_rules = parse_file('grammar')
    terminals, nonterminals = get_terminals_and_non(main_rules)
    dict_rule, dict_rule_full = make_transitions(main_rules)
    first = get_first(dict_rule)
    follow = get_follow(first, dict_rule_full)
    table = make_table(first, follow, main_rules, terminals)


