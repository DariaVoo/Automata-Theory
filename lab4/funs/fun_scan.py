from interpreter import main_loop


def scan_(input_str, index, variable: dict):
    a = input()
    variable[a] = a
    main_loop(input_str, index)

