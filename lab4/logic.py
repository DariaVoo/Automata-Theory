import re

from parse.parse_file import EMPTY_STR_SYMB


def find_set_first(rule, rules_dict) -> list:
    ans = []
    tokens = set()

    for right in rule.right:
        first_char = right[0]
        if first_char == '<':   # nonterminal
            end = right.find(">")
            non = right[:end+1]

            ans.append((rule.left, tokens))
            rules_dict[non].need_to_check = False
            return ans + find_set_first(rules_dict[non], rules_dict)
        elif first_char == '‘':  # terminal
            end = right.find("’")
            s = {right[1:end]}
            tokens |= s
        elif first_char == EMPTY_STR_SYMB:
            continue

    ans.append((rule.left, tokens))
    return ans


def get_first(rules, rules_dict: dict):
    """
    FIRST(E) = set{} -
    возвращает словарь всех FIRST вида
        { E: set },
    где E - нетерминал,
    set - множество токенов, пораждаемых фукцией FIRST
        (множество терминалов, с которых могут начинаться строки, выводимые из E)
    :return:
    """
    first_dict = {}
    # for rule in rules:
    for key in rules_dict.keys():
        if rules_dict[key].need_to_check:
            ans = find_set_first(rules_dict[key], rules_dict)
            print('ANS: ', ans)

    print('\nFIRST:', first_dict)
    return first_dict
