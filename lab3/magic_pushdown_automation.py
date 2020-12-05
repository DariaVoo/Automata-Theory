from automata.pda.npda import NPDA
# NPDA which matches palindromes consisting of 'a's and 'b's
# (accepting by final state)
# q0 reads the first half of the word, q1 the other half, q2 accepts.
# But we have to guess when to switch.
npda = NPDA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    stack_symbols={'A', 'B', '#'},
    transitions={
        'q0': {
            '': {
                '#': {('q2', '#')},
            },
            'a': {
                '#': {('q0', ('A', '#'))},
                'A': {
                    ('q0', ('A', 'A')),
                    ('q1', ''),
                },
                'B': {('q0', ('A', 'B'))},
            },
            'b': {
                '#': {('q0', ('B', '#'))},
                'A': {('q0', ('B', 'A'))},
                'B': {
                    ('q0', ('B', 'B')),
                    ('q1', ''),
                },
            },
        },
        'q1': {
            '': {'#': {('q2', '#')}},
            'a': {'A': {('q1', '')}},
            'b': {'B': {('q1', '')}},
        },
    },
    initial_state='q0',
    initial_stack_symbol='#',
    final_states={'q2'},
    acceptance_mode='final_state'
)