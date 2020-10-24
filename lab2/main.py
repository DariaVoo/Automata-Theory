from check_deterministic import check_deterministic
from draw import draw
from parse.graph_to_file import graph_to_file
from parse.parse_file import parse_file
from to_deterministic import to_deterministic

if __name__ == "__main__":
    # file_name = str(input())
    file_name = "var2.txt"
    graph = parse_file(file_name)
    # draw(graph)
    # print(graph.adj)
    if not check_deterministic(graph):
        determ_graph = to_deterministic(graph)
        # draw(determ_graph)
        file_name = str(input("Enter a file name "))
        graph_to_file(determ_graph, file_name)
