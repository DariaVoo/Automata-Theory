from parse.parse_file import EMPTY_STR_SYMB


def analysis(table, input_str):
    stack = [EMPTY_STR_SYMB]

    # if is None -> str is empty