def fun_scan(input_str, index, variable: dict):
    a = input("\nI want a scan!\t")
    var_name = input_str[index]
    variable[var_name] = a

    index += 2
    if input_str[index] == '}':
        return input_str, index, variable

    from interpreter import main_loop
    return main_loop(input_str, index, variable)

