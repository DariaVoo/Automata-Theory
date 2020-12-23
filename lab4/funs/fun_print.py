from funs.get_var import get_value


def fun_print(input_str, index, variable: dict):
    while input_str[index] != ';':
        if input_str[index] == '”':     # если это строка
            index += 1
            while input_str[index] != '”':
                print(input_str[index], end=' ')
                index += 1
            print()
        else:   # если это переменная
            print(get_value(input_str[index], variable))

        index += 1

    index += 1
    if input_str[index] == '}':
        return input_str, index, variable

    from interpreter import main_loop
    return main_loop(input_str, index, variable)

