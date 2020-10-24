from check_deterministic import check_deterministic
from draw import draw
from logic_check_str.check_str import analysis_str
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
        graph = determ_graph

    if str(input("Do you want to analyze any str? (yes/no)")) == "yes":
        in_str = str(input("Enter a string:\t"))
        analysis_str(in_str, graph)
