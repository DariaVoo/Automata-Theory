import copy
import xml.etree.ElementTree as ET

from logic.COLORS import COLORS
from parse.Block import Block


def syntax_analyzer(root: ET.Element, block: Block):
    ans_ = True
    if block is not None:
        if root.tag == 'column':
            block = copy.deepcopy(block)
            block.current_rows = 0
        elif root.tag == 'row':
            block = copy.deepcopy(block)
            block.current_cols = 0

    if root.tag == 'block':
        block = Block(int(root.attrib['columns']), int(root.attrib['rows']))

    for elem in root:
        print(elem.tag, elem.attrib)
        if block is not None:
            ans = block.add_rows_cols(elem.tag)
            if ans:
                print(f'{COLORS["3"]} Wrong count of {ans}')
                return False

        ans_ = ans_ and syntax_analyzer(elem, block)
    return ans_
