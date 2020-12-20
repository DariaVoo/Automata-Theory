from parse.parse_file import EMPTY_STR_SYMB


def analysis(table, input_str, terminals):
    stack = [EMPTY_STR_SYMB]
    index = 0
    while index < len(input_str):
        print(f'Stack: {stack} input: {input_str[index:]}')
        if stack[-1] == input_str[index] == EMPTY_STR_SYMB:
            print('All is OK! Good job!')
        elif stack[-1] == input_str[index]:
            a = stack.pop()
            print(f'pop from stack {a}')
            index += 1
        elif stack[-1] in terminals:
            print(f'Error: Terminal on stack {stack[-1]}')
            print(f'Remove terminal {stack[-1]} from stack!')
            stack.pop()
        else:
            if table.loc[stack[-1], input_str[index]] is not None:
                stack.pop()
                stack += table.loc[stack[-1], input_str[index]]
            else:
                print('Error, table is empty!')
