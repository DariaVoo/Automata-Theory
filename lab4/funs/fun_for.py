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
    var_value = int(input_str[index + 2])  # expr
    for_type = input_str[index + 3]
    target = int(input_str[index + 4])   # expr
    step = set_step(for_type)

    variable[var_name] = var_value
    index += 5
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

    return main_loop(input_str, index, variable)

