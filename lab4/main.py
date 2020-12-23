from interpreter import main_loop
from syntax_analysis.first import get_first
from syntax_analysis.follow import get_follow
from syntax_analysis.logic import predictive_analysis
from syntax_analysis.make_table import make_table
from parse.parse_file import parse_file, get_terminals_and_non, make_transitions, get_input



def syntax_analysis(grammar_file='grammar', program_file='test.txt', log_file='log.txt'):
    rules, main_rules = parse_file(grammar_file)
    terminals, nonterminals = get_terminals_and_non(main_rules)
    dict_rule, dict_rule_full = make_transitions(main_rules)
    first = get_first(dict_rule)
    follow = get_follow(first, dict_rule_full)
    table = make_table(follow, main_rules, terminals)
    print()
    input_str = get_input(program_file)
    return predictive_analysis(table, input_str, terminals, log_file)


def main():
    sa = True
    sa = syntax_analysis('grammar2', 'test2.txt', 'log2.txt')
    if not sa:
        print('please, FIX THE ERRORS! NOW!')
        return None

    input_str = get_input('test2.txt')
    varaibles = {}
    main_loop(input_str, 0, varaibles)
    print()


if __name__ == '__main__':
    main()

