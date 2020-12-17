import re

from Transition import Rule, Transition
from parse.file_op import read_file

PARTS_RULE_SEPARATOR = '>'
RULE_SEPARATOR = '|'
NONTERMINAL = set('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(sep=' '))
MARKER_STACK = '#'  # h0
EMPTY_STR_SYMB = '~'


def make_transitions(rules, alphabet):
    transitions = []
    state_from = state_to = 's0'

    print("Type2")
    # Строим команды типа 2 для всех терминальных символов
    for alpha in alphabet:
        stack_from = inp = alpha
        stack_to = ""

        t = Transition(state_from, inp, stack_from, state_to, [stack_to])
        print(t)
        transitions.append(t)

    # Добавляем переход в конечное состояние
    print('Type3 - Final state')
    inp = stack_to = ''
    stack_from = MARKER_STACK
    t = Transition(state_from, inp, stack_from, state_to, [stack_to])
    print(t)
    transitions.append(t)

    print('Commands:\nType1')
    #     Строим команды типа 1, '' - empty symb
    state_from = state_to = 's0'
    for rule in rules:
        stack_from = rule.left
        stack_to = rule.right
        inp = ''

        t = Transition(state_from, inp, stack_from, state_to, stack_to)
        print(t)
        transitions.append(t)
    print()
    return transitions


def get_terminals_and_non(rules):
    nonterminals: set = set()
    terminals: set = set()

    print()
    for rule in rules:
        nonrerms = re.findall(r'<[^‘’]+?>', str(rule))
        terms = []
        for r in rule.right:
            ful = re.findall(r'‘.*?’', str(r))
            fi = [s[1:-1] for s in ful]
            terms += fi

        nonterminals |= set(nonrerms)
        terminals |= set(terms)

        rule.terminals = terms
        rule.nonterminals = nonrerms

        # print('Rule:', rule)
        # print('Terminals:', ter)
        # print('Nonterminals:', nonter)
        # print()

    print('Nonterminals:', len(nonterminals), nonterminals)
    print('Terminals:', len(terminals), terminals)
    return terminals, nonterminals


def parse_file(file_name):
    rules = []
    main_rules: list[Rule] = []

    str_rules = read_file(file_name).split(sep='\n')
    # rules.remove("")

    # valid = [re.fullmatch(r'[A-Z]>*', s) for s in rules]
    # if None in valid:
    #     print("Invalid transitions:", rules[valid.index(None)])
    #     return None

    # Разбираем каждое правило на левую и правую часть
    # и составляем лист из правил Rule
    for rule in str_rules:
        rights = []
        sep_index = rule.find(': ')
        left = rule[:sep_index]
        right = rule[sep_index + 2:]

        end_index = right.find(' | ')
        r = rule[sep_index + 2:]
        while end_index != -1:
            right = r[:end_index]

            r = r[end_index + 3:]
            end_index = r.find(' | ')

            rules.append(Rule(left, right))
            rights.append(right)

        if end_index == -1:
            right = r
            rules.append(Rule(left, right))
            rights.append(right)

        main_rules.append(Rule(left, rights))

    print("Get Rules:")
    for r in main_rules:
        print(r)
    return rules, main_rules


