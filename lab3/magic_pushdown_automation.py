from automata.pda.npda import NPDA

from parse.parse_file import MARKER_STACK


def do_npda(alphabet, stack_symb, states_dict):
    npda = NPDA(
        states={'s0'},
        input_symbols=alphabet,
        stack_symbols=stack_symb,
        transitions={
            's0': states_dict,
        },
        initial_state='s0',
        initial_stack_symbol=(MARKER_STACK, 'E'),
        final_states={'s0'},
        acceptance_mode='both'
    )
    return npda
