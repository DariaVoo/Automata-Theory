import pandas as pd

from parse.parse_file import EMPTY_STR_SYMB


def predictive_analysis(table, input_str, terminals):
    stack = [EMPTY_STR_SYMB, '<program>']
    input_str = input_str.split()
    index = 0
    print('Start analysis!')
    while index < len(input_str):
        print()
        print(f'Stack: {stack}\ninput: {input_str[index:]}')
        if stack[-1] == input_str[index] == EMPTY_STR_SYMB:
            print('All is OK! Good job!')
        elif stack[-1] == input_str[index]:
            a = stack.pop()
            print(f'pop from stack {a}')
            index += 1
        elif stack[-1] in terminals:
            print(f'Error: Wrong terminal on stack {stack[-1]}')
            print(f'Remove terminal {stack[-1]} from stack!')
            stack.pop()
        else:
            production = table.loc[stack[-1], input_str[index]]
            if production is not None:
                a = stack.pop()
                stack += production
                print(f'Use production {a} -> {production}')
            else:
                print('Error, table is empty!')
                break
