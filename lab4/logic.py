import pandas as pd

from parse.parse_file import EMPTY_STR_SYMB


def predictive_analysis(table: pd.DataFrame, input_str, terminals):
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
        elif stack[-1].find('><') != -1:
            print(f'get concat production {stack[-1]}')
            # закидываем на стек левое значение конкатенации
            end = stack[-1].find(">")
            a = stack[-1][:end+1]
            stack.pop()
            stack.append(a)

            # рассматриваем это слово из строки посимвольно
            li = list(input_str[index])
            input_str = input_str[:index] + li + input_str[index + 1:]
        elif stack[-1] in terminals:
            print(f'Error: Wrong terminal on stack {stack[-1]}')
            print(f'Remove terminal {stack[-1]} from stack!')
            stack.pop()
        else:
            col = input_str[index]
            if col not in table.columns:
                col = EMPTY_STR_SYMB
            production = table.loc[stack[-1], col]
            if type(production) != float:
                a = stack.pop()
                stack += production
                print(f'Use production {a} -> {production}')

            else:
                if stack[-1] == '<assign_end>':
                    # рассматриваем это слово из строки посимвольно
                    li = list(input_str[index])
                    input_str = input_str[:index] + li + input_str[index + 1:]
                else:
                    print('Error, table is empty!')
                    break
