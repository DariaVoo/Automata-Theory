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

            # rules_dict[non].need_to_check = False
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


def get_first(rules_dict):
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
        ans = find_set_first(rules_dict[key], rules_dict)
        print(f'ANS{key}: ', ans)

        first = set()
        for nonterm, terms in ans:
            first |= terms
            if nonterm in first_dict.keys():
                first_dict[nonterm] |= terms
            else:
                first_dict[nonterm] = terms

        first_dict[key] |= first

    print('\nFIRST:', first_dict)
    return first_dict


# FOLLOW
def find_set_second_nonterm(rule) -> list:
    ans = {rule.left}
    tokens = set()

    for right in rule.right:
        last_char = right[-1]
        if last_char == '>':   # nonterminal
            begin = right.rfind("<")
            non = right[begin:]
            ans |= {non}

        # elif last_char == '’':   # terminal
        #     begin = right.rfind("‘")
        #     non = right[begin + 1:-1]

    # ans.append((rule.left, tokens))
    return ans


def find_set_second_terms(rule, nonterms, firsts):
    terms = set()

    for right in rule.right:
        last_char = right[-1]
        if last_char == '’':   # terminals
            begin = right.rfind("‘")
            t = right[begin + 1:-1]
            terms |= {t}

        else:
            for nonterm in nonterms:    # Смотрим, содержит ли наша строка нетерминал
                begin = right.rfind(nonterm)
                if begin != -1:
                    if begin + len(nonterm) >= len(right):
                        terms |= firsts[nonterm]
                        print(f'Add feom FIRST: {firsts[nonterm]}')
                    elif right[begin + len(nonterm)] == '‘':
                        end = right.rfind('’')
                        t = right[begin + len(nonterm):end + 1]
                        terms |= {t}

    return terms


def get_follow(firsts, rules_dict: dict):
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
        nonterms = find_set_second_nonterm(rules_dict[key])
        print(f'ANS{key}: ', nonterms)

        terms = find_set_second_terms(rules_dict[key], nonterms, firsts)

        follow_dict[key] = terms

    print('\nFOLLOW:', follow_dict)

    return follow_dict