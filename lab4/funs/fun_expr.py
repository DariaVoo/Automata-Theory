import re

from funs.get_var import get_var


def do_exp(a, b, op: str):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif b == 0:    # Check for divide by zero/modulo by zero
        print('Divide by zero!')
        return None
    elif op == '/':
        return a / b
    elif op == '%':
        return a % b

    print('No such op!')
    return None


factors = ['+', '-', '*', '/']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def get_term(expr, variable):
    symbs = re.findall(r"[\+\-*\/()]", expr)

    if len(symbs) == 0:
        return int(expr)
    elif len(symbs) == 1:
        expr_ = expr.split(sep=symbs[0])
        if expr_[0][0] not in nums:
            a = int(get_var([expr_[0]], variable))
        else:
            a = int(expr_[0])
        if expr_[1][0] not in nums:
            b = (get_var([expr_[1]], variable))
        else:
            b = int(expr_[1])

        ans = do_exp(a, b, symbs[0])
        return ans
    else:
        if '(' in symbs:
            sep_index = expr.find('(') - 1
            sep_index_end = expr.find(')')
            op = expr[sep_index]
            a_str = expr[:sep_index]
            b_str = expr[sep_index + 2:sep_index_end]
            a, b = get_term(a_str, variable), get_term(b_str, variable)
            ans = do_exp(a, b, op)
            return ans
        else:
            for f in factors:
                if f in symbs:
                    sep_index = expr.find(f)
                    op = expr[sep_index]
                    a_str = expr[:sep_index]
                    b_str = expr[sep_index + 1:]
                    a, b = get_term(a_str, variable), get_term(b_str, variable)
                    ans = do_exp(a, b, op)
                    return ans
    return None


def fun_expr(input_str, index, variable: dict):
    expr: str = input_str[index]
    ans = get_term(expr, variable)
    print(f'Ans: {input_str[index]} = {ans}')
    input_str[index] = ans
    return input_str, index, variable