import pandas as pd

from parse.parse_file import EMPTY_STR_SYMB


def create_list_for_stack(right):
    # очищаем терминалы от кавычек и разделяем конкатенированные терминалы
    str_r = right.split()
    str_r = [word[1:-1] if word.startswith('‘') else word for word in str_r]
    # for word in str_r:
    #     if word.startswith('‘'):     # убираем кавычки
    #         word = word[1:-1]
    #     # elif word.startwith('')
    str_r.reverse()
    return str_r


def make_table(follow, rules, terminals):
    table = pd.DataFrame(columns=list(terminals))
    for rule in rules:
        for first, right in zip(rule.first_in_right, rule.right):
            for term in first:
                # a = right.split()
                # a.reverse()
                a = create_list_for_stack(right)
                table.loc[rule.left, term] = a

            if EMPTY_STR_SYMB in first:
                for ter in follow[rule.left]:
                    # a = right.split()
                    # a.reverse()
                    a = create_list_for_stack(right)
                    table.loc[rule.left, ter] = a

    # table.to_csv('table.csv')
    return table