import re

from funs.RULES import RULES
from parse.parse_file import EMPTY_STR_SYMB


def get_next_lexem(input_str, index):
    current = input_str[index]
    if current.find('‘') and current in RULES.keys():
        token = current
        # print(f'token = {token}')
    elif current == EMPTY_STR_SYMB:
        print("END OF PROGRAM!")
        return None, index
    elif re.search(r"[\+\-*\/]", current):
        token = 'expression'
        return token, index
    elif re.search(r"[><==!=]", current):
        token = 'bool_expression'
        return token, index
    else:
        print(f"Error in interpreter, found: {input_str[index]}")
        return None, index
    return token, index + 1


def main_loop(input_str, index, variable):
    token, index = get_next_lexem(input_str, index)

    if token:
        token = RULES[token]
        input_str, index, variable = token(input_str, index, variable)

    return input_str, index, variable
