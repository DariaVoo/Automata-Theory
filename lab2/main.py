from check_deterministic import check_deterministic
from draw import draw
from parse.parse_file import parse_file

if __name__ == "__main__":
    # file_name = str(input())
    file_name = "var2.txt"
    graph = parse_file(file_name)
    # draw(graph)
    check_deterministic(graph)
