from funs.fun_bool_expr import fun_bool_expr


def skip_braket(br, input_str, index):
    while input_str[index:] and input_str[index] != br:
        index += 1
    if input_str[index:]:
        index += 1
    return index


def fun_if(input_str, index, variable: dict):
    from interpreter import main_loop
    input_str, index, variable = fun_bool_expr(input_str, index, variable)
    condition = bool(input_str[index])

    index = skip_braket('{', input_str, index)
    if condition:   # если всё ок выполняем ветку if
        input_str, index, variable = main_loop(input_str, index, variable)
        index = skip_braket('}', input_str, index)
        if input_str[index] == 'else':
            index = skip_braket('}', input_str, index)

    else:   # если нет - ветку else, если она есть
        index = skip_braket('}', input_str, index)
        if input_str[index] == 'else':
            index = skip_braket('{', input_str, index)
            input_str, index, variable = main_loop(input_str, index, variable)

    return main_loop(input_str, index, variable)
