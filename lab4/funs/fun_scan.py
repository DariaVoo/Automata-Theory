def fun_scan(input_str, index, variable: dict):
    a = input("\nI want a scan!\t")
    variable[a] = a

    from interpreter import main_loop
    main_loop(input_str, index + 2, variable)

