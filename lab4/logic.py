import re

from parse.parse_file import EMPTY_STR_SYMB


def find_set_first(rule, rules_dict) -> list:
    ans = []
    tokens = set()
    res = []

    for right in rule.right:
        first_char = right[0]
        if first_char == '<':   # nonterminal
            end = right.find(">")
            non = right[:end+1]

            rules_dict[non].need_to_check = False
            res += find_set_first(rules_dict[non], rules_dict)

        elif first_char == '‘':  # terminal
            end = right.find("’")
            s = {right[1:end]}
            tokens |= s
        elif first_char == EMPTY_STR_SYMB:  # Надо исправить
            s = {EMPTY_STR_SYMB}
            tokens |= s

    ans += res
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
    print()
    for key in rules_dict.keys():
        if rules_dict[key].need_to_check:
            ans = find_set_first(rules_dict[key], rules_dict)
            print('ANS: ', ans)
    # TODO: дождаться ответа от Кремера и в соответствии с ним
    #       пообъединять(нет) множества и составить словарь

    print('\nFIRST:', first_dict)
    return first_dict


# FOLLOW
def find_set_second(rule, rules_dict) -> list:
    ans = []
    tokens = set()

    for right in rule.right:
        last_char = right[-1]
        if last_char == '>':   # nonterminal
            begin = right.rfind("<")
            non = right[begin:]
            tokens |= {non}

            # rules_dict[non].need_to_check = False

    ans.append((rule.left, tokens))
    return ans


def get_follow(rules, rules_dict: dict):
    """
    FOLLOW(E) = set{} -
    возвращает словарь всех FOLLOW вида
        { E: set },
    где E - нетерминал,
    set - множество токенов, пораждаемых фукцией FOLLOW
        (множество терминалов, которые могут следовать после E)
    :return:
    """
    follow_dict = {}
    # for rule in rules:
    print()
    for key in rules_dict.keys():
        if rules_dict[key].need_to_check:
            ans = find_set_second(rules_dict[key], rules_dict)
            print('ANS: ', ans)
    # TODO: дождаться ответа от Кремера и в соответствии с ним
    #       пообъединять(нет) множества и составить словарь

    print('\nFOLLOW:', follow_dict)
    return follow_dict