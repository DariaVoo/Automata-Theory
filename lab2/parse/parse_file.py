import re

from parse.file_op import read_file


def parse_file(file_name):
    transitions = set(read_file(file_name).split(sep='\n'))
    transitions.remove("")
    transitions = sorted(list(transitions))

    valid = [re.fullmatch(r'q\d,.=[qf]\d', s) for s in transitions]
    if None in valid:
        print("Invalid transitions:", transitions[valid.index(None)])
        return None
