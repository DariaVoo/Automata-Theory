from logic.logic import find
from parse.parse_file import parse_file


def main(name):
    xml = parse_file('test.xml')
    if xml is None:
        return None
    find(xml, None, None)


if __name__ == '__main__':
    main('PyCharm')

