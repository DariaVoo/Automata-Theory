import re

from parse.parse_file import EMPTY_STR_SYMB


def get_first(rules):
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
    for rule in rules:
        tokens = set()
        for right in rule.right:
            first_char = right[0]
            if first_char == '<':
                #   recursion
                continue
            elif first_char == '‘':
                tokens |= re.find(r'<[^‘’]+?>', str(right))
            elif first_char == EMPTY_STR_SYMB:
                continue

        first_dict[rule.left] = tokens