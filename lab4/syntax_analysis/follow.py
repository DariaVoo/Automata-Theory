def find_set_second_nonterm(rule) -> list:
    ans = {rule.left}

    for right in rule.right:
        last_char = right[-1]
        if last_char == '>':   # nonterminal
            begin = right.rfind("<")
            non = right[begin:]
            ans |= {non}

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
                        # print(f'Add from FIRST: {firsts[nonterm]}')
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
    # print()
    for key in rules_dict.keys():
        nonterms = find_set_second_nonterm(rules_dict[key])
        # print(f'ANS{key}: ', nonterms)

        terms = find_set_second_terms(rules_dict[key], nonterms, firsts)

        follow_dict[key] = terms

    print('\nFOLLOW:', follow_dict)

    return follow_dict
