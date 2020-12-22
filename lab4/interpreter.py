from Command import Command
from funs import fun_print

RULES = {'print': Command('print', fun_print)}


def get_nex_lexem(st):
    n = 0
    return n


def main_loop(input_str, index):
    token = get_nex_lexem(input_str)

    token = RULES[token]
    token.fun(input_str, index)
