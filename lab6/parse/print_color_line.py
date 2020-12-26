from logic.COLORS import COLORS


def print_color_line(num_color, text):
    print(f'{COLORS[num_color]} {text} {COLORS["00"]}')
