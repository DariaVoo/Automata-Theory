def get_var(key, vars:dict):
    if key not in vars.keys():
        vars[key] = 0
    return vars[key]