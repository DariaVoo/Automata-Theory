import re

from Transition import Rule, Transition
from parse.file_op import read_file

PARTS_RULE_SEPARATOR = '>'
RULE_SEPARATOR = '|'
EMPTY_STR_SYMB = '~'


def find_all_subrules(right, nonterms, left, rules_dict):
    new_right = []
    # new_rules = []
    for non in nonterms:
        bu, new_nons = rules_dict[non].create_new_gen_rule(right, non, nonterms)

        new_right += bu
        n = Rule(left, bu)
        # print(f'Nonterm {non}: ', n)
        # new_rules.append(n)
        for ri in bu:
            new_right += find_all_subrules(ri, new_nons, left, rules_dict)
    return new_right


def make_transitions(rules):
    rules_dict = {r.left: r for r in rules}
    # TODO: Дописать полную генерацию правил
    # new_rules = []
    # print()
    # for rule in rules:
    #     print('Rule:', rule)
    #     new_right = []
    #     for r, nonterms in zip(rule.right, rule.nonterminals):
    #         new_right += find_all_subrules(r, nonterms, rule.left, rules_dict)
    #         # for non in nonterms:
    #         #     bu, new_nons = rules_dict[non].create_new_gen_rule(r, non, nonterms)
    #         #
    #         #     new_right += bu
    #         #
    #         #     n = Rule(rule.left, bu)
    #         #     print(f'Nonterm {non}: ', n)
    #         #     new_rules.append(n)
    #         # # print()
    #     rule.right += new_right
    #     print(new_right)
    #     print('!!!!!')

    # print(rules_dict)
    return rules_dict


def get_terminals_and_non(rules):
    nonterminals: set = set()
    terminals: set = set()

    print()
    for rule in rules:
        nonterms = re.findall(r'<[^‘’]+?>', str(rule))
        terms = []
        for r in rule.right:
            ful = re.findall(r'‘.*?’', str(r))
            fi = [s[1:-1] for s in ful]
            terms += fi

            rule.terminals.append(fi)

            nonterm = re.findall(r'<[^‘’]+?>', str(r))
            rule.nonterminals.append(nonterm)

        nonterminals |= set(nonterms)
        terminals |= set(terms)

        # rule.terminals = terms
        # rule.nonterminals = nonterms

        # print('Rule:', rule)
        # print('Terminals:', terms)
        # print('Nonterminals:', nonterms)
        # print()

    print('Nonterminals:', len(nonterminals), nonterminals)
    print('Terminals:', len(terminals), terminals)
    return terminals, nonterminals


def parse_file(file_name):
    rules = []
    main_rules: list[Rule] = []

    str_rules = read_file(file_name).split(sep='\n')
    # rules.remove("")

    # valid = [re.fullmatch(r'[A-Z]>*', s) for s in rules]
    # if None in valid:
    #     print("Invalid transitions:", rules[valid.index(None)])
    #     return None

    # Разбираем каждое правило на левую и правую часть
    # и составляем лист из правил Rule
    for rule in str_rules:
        rights = []
        sep_index = rule.find(': ')
        left = rule[:sep_index]
        right = rule[sep_index + 2:]

        end_index = right.find(' | ')
        r = rule[sep_index + 2:]
        while end_index != -1:
            right = r[:end_index]

            r = r[end_index + 3:]
            end_index = r.find(' | ')

            rules.append(Rule(left, right))
            rights.append(right)

        if end_index == -1:
            right = r
            rules.append(Rule(left, right))
            rights.append(right)

        main_rules.append(Rule(left, rights))

    print("Get Rules:")
    for r in main_rules:
        print(r)
    return rules, main_rules


