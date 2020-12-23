def fun_print(input_str, index, variable: dict):
    while input_str[index] != ';':
        if input_str[index] == '”':     # если это строка
            index += 1
            while input_str[index] != '”':
                print(input_str[index])
                index += 1
        else:   # если это переменная
            print(variable[input_str[index]])

        index += 1

    index += 1
    from interpreter import main_loop
    main_loop(input_str, index, variable)
