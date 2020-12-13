from Transition import Rule, Transition
from parse.file_op import read_file

PARTS_RULE_SEPARATOR = '>'
RULE_SEPARATOR = '|'
NONTERMINAL = set('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(sep=' '))
MARKER_STACK = '#'  # h0


def make_transitions(rules, alphabet):
    transitions = []
    state_from = state_to = 's0'

    print('Commands:\nType1')
    #     Строим команды типа 1, '' - empty symb
    for rule in rules:
        stack_from = rule.left
        stack_to = rule.right
        inp = ''

        t = Transition(state_from, inp, stack_from, state_to, stack_to)
        print(t)
        transitions.append(t)

    print("Type2")
    # Строим команды типа 2 для всех терминальных символов
    for alpha in alphabet:
        stack_from = inp = alpha
        stack_to = ""

        t = Transition(state_from, inp, stack_from, state_to, stack_to)
        print(t)
        transitions.append(t)

    # Добавляем переход в конечное состояние
    print('Type3 - Final state')
    inp = stack_to = ''
    stack_from = MARKER_STACK
    t = Transition(state_from, inp, stack_from, state_to, stack_to)
    print(t)
    transitions.append(t)
    return transitions


def main_make_transitions(rules, alphabet, main_rules):
    dict_inp = {}
    states_dict = {}
    state_from = state_to = 's0'

    print('Commands:\nType1')
    #     Строим команды типа 1, '' - empty symb
    inp = ''
    for rule in main_rules:
        stack_from = rule.left
        stack_to = rule.right

        dict_inp[stack_from] = (state_to, tuple(stack_to))

    # Добавляем переход в конечное состояние
    print('Type3 - Final state')
    inp = stack_to = ''
    stack_from = MARKER_STACK
    dict_inp[stack_from] = (state_to, '')
    states_dict[inp] = dict_inp

    print("Type2")
    # Строим команды типа 2 для всех терминальных символов
    for alpha in alphabet:
        stack_from = inp = alpha
        stack_to = ""
        states_dict[inp] = {stack_from: (state_to, tuple(stack_to))}

    print(states_dict)
    return states_dict


def get_stack_symb_alphabet(rules):
    alphabet: set  # P
    stack_symbols: set = set(MARKER_STACK)  # Z

    for rule in rules:
        stack_symbols |= set(rule.left)
        stack_symbols |= set(rule.right)

    print("stack symbols: ", stack_symbols)
    alphabet = stack_symbols - NONTERMINAL
    print("alphabet: ", alphabet)
    stack_symbols |= set([MARKER_STACK, 'E'])

    return alphabet, stack_symbols


def parse_file(file_name):
    rules = []
    main_rules = []

    str_rules = read_file(file_name).split(sep='\n')
    # rules.remove("")

    # valid = [re.fullmatch(r'[A-Z]>*', s) for s in rules]
    # if None in valid:
    #     print("Invalid transitions:", rules[valid.index(None)])
    #     return None

    for rule in str_rules:
        rights = []
        sep_index = rule.find('>')
        left = rule[:sep_index]
        right = rule[sep_index + 1:]
        print(f'left: {left} right: {right}')

        end_index = right.find('|')
        r = rule[sep_index + 1:]
        while end_index != -1:
            right = r[:end_index]

            r = r[end_index + 1:]
            end_index = r.find('|')
            # print(f'left: {left} right: {right}')
            rules.append(Rule(left, right))
            rights.append(right)

        if end_index == -1:
            right = r
            # print(f'left: {left} right: {right}')
            rules.append(Rule(left, right))
            rights.append(right)

        main_rules.append(Rule(left, rights))

    print("Get Rules:")
    for r in rules:
        print(r)
    return rules, main_rules


