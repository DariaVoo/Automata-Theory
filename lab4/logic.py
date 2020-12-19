import pandas as pd

from parse.parse_file import EMPTY_STR_SYMB


def make_table(first, follow, rules, terminals):
    table = pd.DataFrame(columns=list(terminals))
    for rule in rules:
        for first, right in zip(rule.first_in_right, rule.right):
            for term in first:
                a = list(right)
                a.reverse()
                table.loc[rule.left, term] = a

            if EMPTY_STR_SYMB in first:
                for ter in follow[rule.left]:
                    a = list(right)
                    a.reverse()
                    table.loc[rule.left, ter] = a

    # table.to_csv('table.csv')
    return table