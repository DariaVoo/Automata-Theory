import re

from funs.get_var import get_value


def do_bool_exp(a, b, op: str):
    a = str(a)
    b = str(b)
    if op == '<':
        return a < b
    elif op == '>':
        return a > b
    elif op == '==':
        return a == b
    elif op == '!=':
        return a != b

    print('No such bool op!')
    return None


factors_bool = ['<', '>', '!', '=']


def get_bool_term(expr, variable):
    symbs = re.findall(r"[=<>!]", expr)

    if len(symbs) == 0:
        if expr in variable.keys():
            expr = get_value(expr, variable)
        return expr
    elif len(symbs) == 1:
        expr_ = expr.split(sep=symbs[0])
        if expr_[0][0] in variable.keys():
            a = get_value(expr_[0], variable)
        else:
            a = expr_[0]
        if expr_[1][0] in variable.keys():
            b = get_value(expr_[1], variable)
        else:
            b = expr_[1]

        ans = do_bool_exp(a, b, symbs[0])
        return ans
    else:
        if '(' in symbs:
            sep_index = expr.find('(') - 1
            sep_index_end = expr.find(')')
            op = expr[sep_index]
            a_str = expr[:sep_index]
            b_str = expr[sep_index + 2:sep_index_end]
            a, b = get_bool_term(a_str, variable), get_bool_term(b_str, variable)
            ans = do_bool_exp(a, b, op)
            return ans
        else:
            for f in factors_bool:
                if f in symbs:
                    sep_index = expr.find(f)
                    len_sep = 1
                    if f == '=':
                        if expr[sep_index + 1] == '=':
                            op = '=='
                            len_sep = 2
                    elif f == '!':
                        if expr[sep_index + 1] == '=':
                            op = '!='
                            len_sep = 2
                    else:
                        op = expr[sep_index]
                    a_str = expr[:sep_index]
                    b_str = expr[sep_index + len_sep:]
                    a, b = get_bool_term(a_str, variable), get_bool_term(b_str, variable)
                    ans = do_bool_exp(a, b, op)
                    return ans
    return None


def fun_bool_expr(input_str, index, variable: dict):
    expr: str = input_str[index]
    ans = get_bool_term(expr, variable)
    print(f'Ans: {input_str[index]} = {ans}')
    input_str[index] = ans
    return input_str, index, variable