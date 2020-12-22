from interpreter import main_loop


def fun_print(input_str, index, variable: dict):
    to_print = ''
    while input_str[index] != ";":
        to_print += input_str[index]
        index += 1
    print(to_print)
    main_loop(input_str, index)
