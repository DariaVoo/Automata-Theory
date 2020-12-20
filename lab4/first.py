from parse.parse_file import EMPTY_STR_SYMB


def find_set_first(rule, rules_dict) -> list:
    ans = []
    res = []
    all_tokens = set()

    for right in rule.right:
        tokens = set()
        first_char = right[0]
        if first_char == '<':   # nonterminal
            end = right.find(">")
            non = right[:end+1]

            # rules_dict[non].need_to_check = False
            r1 = find_set_first(rules_dict[non], rules_dict)
            if r1:
                for n, terms in r1:
                    tokens |= terms
            res += r1

        elif first_char == '‘':  # terminal
            end = right.find("’")
            s = {right[1:end]}
            tokens |= s
        elif first_char == EMPTY_STR_SYMB:  # Надо исправить
            s = {EMPTY_STR_SYMB}
            tokens |= s

        all_tokens |= tokens
        # добавляем в правило множество first для конкретно этого правила
        rule.first_in_right.append(tokens)

    ans += res
    ans.append((rule.left, all_tokens))
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
