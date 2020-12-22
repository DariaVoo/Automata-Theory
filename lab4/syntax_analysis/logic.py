import pandas as pd

from parse.parse_file import EMPTY_STR_SYMB


def error_handler(error_msg, count_mistakes, index, f, stack, input_str):
    # восстановление после ошибки
    print(f'Stack: {stack}\ninput: {input_str[index:]}')
    print(error_msg)
    print(f'Skip {input_str[index]} from input str!\n')
    count_mistakes += 1

    f.write(error_msg)
    f.write(f'\nSkip {input_str[index]} from input str!\n')
    index += 1
    return count_mistakes, index


def predictive_analysis(table: pd.DataFrame, input_str, terminals, file_name_log):
    stack = [EMPTY_STR_SYMB, '<program>']
    index = 0
    as_flag = False
    count_mistakes = 0

    f = open(file_name_log, 'w')
    print('Start analysis!')
    while index < len(input_str):
        # print(f'Stack: {stack}\ninput: {input_str[index:]}')
        f.write(f'\nStack: {stack}\ninput: {input_str[index:]}\n')
        if stack[-1] == input_str[index] == EMPTY_STR_SYMB:
            stack.pop()
            while index < len(input_str) and input_str[index] == EMPTY_STR_SYMB:
                index += 1
            f.write(f'I found empty symbol {EMPTY_STR_SYMB}')
        elif stack[-1] == input_str[index]:
            a = stack.pop()
            f.write(f'pop from stack {a}\n')
            index += 1
        elif stack[-1].find('><') != -1:
            f.write(f'get concat production {stack[-1]}\n')
            # закидываем на стек левое значение конкатенации
            end = stack[-1].find(">")
            a = stack[-1][:end+1]
            b = stack[-1][end+1:]
            stack.pop()
            stack.append(b)
            stack.append(a)
            as_flag = False

            # рассматриваем это слово из строки посимвольно
            li = list(input_str[index])
            input_str = input_str[:index] + li + list(EMPTY_STR_SYMB) + input_str[index + 1:]
        elif stack[-1] in terminals:
            # восстановление после ошибки
            count_mistakes, index = error_handler(f'Error: Wrong terminal on input str {input_str[index]}',
                                                  count_mistakes, index, f, stack, input_str)
            # stack.pop()
        elif stack[-1] != EMPTY_STR_SYMB:
            col = input_str[index]
            if col not in table.columns:
                col = EMPTY_STR_SYMB
            if as_flag:
                col = input_str[index][0]

            production = table.loc[stack[-1], col]
            if type(production) != float:
                a = stack.pop()
                stack += production
                f.write(f'Use production {a} -> {production}\n')

            else:
                if stack[-1] == '<assign_end>' or stack[-1] == '<identifier>' or stack[-1] == '<bool_expression>':
                    as_flag = True
                else:
                    count_mistakes, index = error_handler('Error, table is empty!',
                                                          count_mistakes, index, f, stack, input_str)
                    return
        else:
            # восстановление после ошибки
            count_mistakes, index = error_handler('Error, empty symbol in str!',
                                                  count_mistakes, index, f, stack, input_str)

    print("----------------------------\nDone!")
    print(f'Count mistakes: {count_mistakes}')


