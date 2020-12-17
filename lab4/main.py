from parse.parse_file import parse_file, get_terminals_and_non

if __name__ == '__main__':

    rules, main_rules = parse_file('grammar')
    terminals, nonterminals = get_terminals_and_non(main_rules)
