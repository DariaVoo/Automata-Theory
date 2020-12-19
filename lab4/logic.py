import pandas as pd


def make_table(first, follow, rules, terminals):
    table = pd.DataFrame(columns=list(terminals))
    for nonterm in first.key():
        for term in first[nonterm]:
            table.loc[nonterm, term] = 