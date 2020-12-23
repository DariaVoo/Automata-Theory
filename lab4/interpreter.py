from funs.RULES import RULES
from parse.parse_file import EMPTY_STR_SYMB


def get_nex_lexem(input_str, index):
    current = input_str[index]
    if current.find('‘') and current in RULES.keys():
        token = current
        # print(f'token = {token}')
    elif current == EMPTY_STR_SYMB:
        token = None
        print("END OF PROGRAM!")
    else:
        token = None
        print("Error in interpreter")
    return token, index + 1


def main_loop(input_str, index, variable):
    token, index = get_nex_lexem(input_str, index)

    if token:
        token = RULES[token]
        input_str, index, variable = token(input_str, index, variable)

    return input_str, index, variable
