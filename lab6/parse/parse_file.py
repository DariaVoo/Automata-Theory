import xml.etree.ElementTree as ET

from logic.COLORS import COLORS
from parse.print_color_line import print_color_line
from parse.syntax_analyzer import syntax_analyzer


def parse_file(file_name):
    mytree = ET.parse(file_name)
    root = mytree.getroot()

    print(root)
    s = syntax_analyzer(root, None)
    if s:
        print_color_line('2', 'All syntax is OK!')
        return root
    else:
        print_color_line('1', 'Fix this, please!')
        return None
