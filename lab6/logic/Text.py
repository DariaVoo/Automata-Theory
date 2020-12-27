from logic.COLORS import COLORS, BGCOLORS

HALIGN = {
    'left': '<',
    'center': '^',
    'right ': '>',
}


class Text:
    """ Класс для текста
        valign:param - вертикальное_выравнивание – одно из значений top, center, bottom
                        (выравнивание по верхнему краю, по центру и по нижнему краю соответственно)
        halign:param - горизонтальное_выравнивание – одно из значений left, center, right
                        (выравнивание по левому краю, по центру и по правому краю соответственно)
        textcolor - цифра, цвет текста
        bgcolor - цвет фона
        width - ширина - смещение по х
        height - высота - смещение по y
    """
    def __init__(self):
        self.valign = 'top'
        self.halign = 'left'
        self.textcolor = 7
        self.bgcolor = 0
        self.width = 1
        self.height = 1

    def set_param(self, valign, halign, textcolor, bgcolor, width):
        self.valign = valign
        self.halign = halign
        self.textcolor = textcolor
        self.bgcolor = bgcolor
        self.width = width
        self.height = 1

    def set_attr(self, attrib: dict):
        if 'valign' in attrib.keys():
            self.valign = attrib['valign']
        if 'halign' in attrib.keys():
            self.halign = attrib['halign']
        if 'textcolor' in attrib.keys():
            self.textcolor = attrib['textcolor']
        if 'bgcolor' in attrib.keys():
            self.bgcolor = attrib['bgcolor']
        if 'width' in attrib.keys():
            self.width = attrib['width']
        if 'height' in attrib.keys():
            self.height = attrib['height']

    def get_text(self, text: str):
        begin = 0
        while text[begin] == ' ' or text[begin] == '\n':
            begin += 1

        end = len(text) - 1
        while text[end] == ' ' or text[end] == '\n':
            end -= 1
        text = text[begin:end]

        templ = f':*{HALIGN[self.halign]}{self.width}'
        template = COLORS[str(self.textcolor)] + BGCOLORS[str(self.bgcolor)] + '{' + templ + '}' + COLORS['00']
        print(template.format(text))
