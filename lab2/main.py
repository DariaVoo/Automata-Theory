from check_deterministic import check_deterministic
from draw import draw
from parse.parse_file import parse_file
from to_deterministic import to_deterministic

if __name__ == "__main__":
    # file_name = str(input())
    file_name = "var2.txt"
    graph = parse_file(file_name)
    # draw(graph)
    # print(graph.adj)
    check_deterministic(graph)
    to_deterministic(graph)
