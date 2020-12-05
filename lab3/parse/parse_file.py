import re

from parse.State import Rule
from parse.file_op import read_file

PARTS_RULE_SEPARATOR = '>'
RULE_SEPARATOR = '|'
NONTERMINAL = 'A-Z'


def parse_file(file_name):
    alphabet: set = set()  # P
    stack_symbols: set = set()  # Z
    rules_res: dict = {}
    rules = []

    str_rules = read_file(file_name).split(sep='\n')
    # rules.remove("")

    # valid = [re.fullmatch(r'[A-Z]>*', s) for s in rules]
    # if None in valid:
    #     print("Invalid transitions:", rules[valid.index(None)])
    #     return None

    for rule in str_rules:
        sep_index = rule.find('>')
        left = rule[:sep_index]
        right = rule[sep_index + 1:]
        print(f'left: {left} right: {right}')

        end_index = right.find('|')
        r = rule[sep_index + 1:]
        while end_index != -1:
            right = r[:end_index]
            r = r[end_index + 1:]
            end_index = r.find('|')
            print(f'left: {left} right: {right}')
            rules.append(Rule(left, right))

        if end_index == -1:
            right = r
            print(f'left: {left} right: {right}')
            rules.append(Rule(left, right))

    print(rules)
    return alphabet, stack_symbols, rules_res

