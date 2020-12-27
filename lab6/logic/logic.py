from logic.Text import Text
from parse.Block import Block
from parse.print_color_line import print_color_line
from parse.syntax_analyzer import check_block

draft = {'\n', ' '}


def find(root, text: Text, block: Block):
    # print(f"\033[31m\033[4m {'Logic'}  \033[0m")

    if text is not None:
        if root.tag == 'column':
            text = Text()
            text.set_attr(root.attrib)

    block = check_block(block, root.tag)
    if root.tag == 'block':
        col = int(root.attrib['columns'])
        row = int(root.attrib['rows'])
        if block is not None:
            err = block.check_new_rows_cols(row, col)
        block = Block(col, row)
        text = Text()

    for elem in root:
        if block is not None:
            ans = block.add_rows_cols(elem.tag)

        if elem.tag == 'column' or elem.tag == 'row':
            text = Text()
            text.set_attr(root.attrib)

            if set(elem.text) != draft:
                text.get_text(elem.text)

            a = find(elem, text, block)

        # ans_ = ans_ and syntax_analyzer(elem, block)
    return None

