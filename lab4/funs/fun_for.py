from funs.fun_expr import fun_expr


def set_step(type_for):
    step = 0
    if type_for == 'to':
        step = 1
    elif type_for == 'downto':
        step = -1
    else:
        print('Uncorrect type of for! Avaliable: to, downto')
    return step


def fun_for(input_str, index, variable: dict):
    from interpreter import main_loop

    var_name = input_str[index]
    input_str, index, variable = fun_expr(input_str, index + 2, variable)
    var_value = int(input_str[index])  # expr

    index += 1
    for_type = input_str[index]

    input_str, index, variable = fun_expr(input_str, index + 1, variable)
    target = int(input_str[index])   # expr
    step = set_step(for_type)

    variable[var_name] = var_value
    while input_str[index] != '{':
        index += 1
    index += 1
    index_begin = index

    while variable[var_name] != target:
        index = index_begin
        input_str, index, variable = main_loop(input_str, index, variable)
        variable[var_name] += step

    del variable[var_name]

    if input_str[index] == '}':
        index += 1
    # проверяем на вложенность, если вложенный просто возвращаем
    if input_str[index] == '}':
        return input_str, index, variable

    return main_loop(input_str, index, variable)

