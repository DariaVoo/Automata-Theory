import xml.etree.ElementTree as ET

from logic.COLORS import COLORS
from parse.Block import Block


def syntax_analyzer(root: ET.Element, block: Block):
    if root.tag == 'block':
        block = Block(int(root.attrib['rows']), int(root.attrib['columns']))

    ans = True
    for elem in root:
        print(elem.tag, elem.attrib)
        if block is not None:
            ans = block.add_rows_cols(elem.tag)
            if ans:
                print(f'{COLORS["1"]} Wrong count of {ans}')
                return False

        ans = ans and syntax_analyzer(elem, block)
    return ans
