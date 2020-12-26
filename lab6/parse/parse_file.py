import xml.etree.ElementTree as ET


def parse_file(file_name):
    mytree = ET.parse(file_name)
    root = mytree.getroot()

    print(root)
    return root

    # # all item attributes
    # print(f"\033[31m\033[4m {'Color'}  \033[0m")
    # print('\nAll attributes:')
    # for elem in root:
    #     print(elem.tag, elem.attrib)
    #
    #     for subelem in elem:
    #         print('\t', subelem.tag, subelem.attrib)


