import xml.etree.ElementTree as ET

from parse.syntax_analyzer import syntax_analyzer


def parse_file(file_name):
    mytree = ET.parse(file_name)
    root = mytree.getroot()

    print(root)
    if syntax_analyzer(root, None):
        print('All is OK!')
        return root
    else:
        print('Fix this, please!')
        return None
