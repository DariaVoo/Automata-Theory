from first import get_first
from follow import get_follow
from logic import predictive_analysis
from make_table import make_table
from parse.parse_file import parse_file, get_terminals_and_non, make_transitions, get_input

if __name__ == '__main__':

    rules, main_rules = parse_file('grammar')
    terminals, nonterminals = get_terminals_and_non(main_rules)
    dict_rule, dict_rule_full = make_transitions(main_rules)
    first = get_first(dict_rule)
    follow = get_follow(first, dict_rule_full)
    table = make_table(follow, main_rules, terminals)
    # print()
    input_str = get_input('test.txt')
    predictive_analysis(table, input_str, terminals)


