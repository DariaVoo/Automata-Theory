from check_deterministic import check_deterministic
from draw import draw
from logic_check_str.check_str import analysis_str
from parse.graph_to_file import graph_to_file
from parse.parse_file import parse_file
from to_deterministic import to_deterministic
from to_deterministic_it import to_deterministic_it

if __name__ == "__main__":
    # file_name = str(input())
    file_name = "test.txt"
    graph = parse_file(file_name)
    if graph is not None:
        # draw(graph)
        if not check_deterministic(graph):
            determ_graph = to_deterministic_it(graph)
            # draw(determ_graph)
            if str(input("Do you want to write determined automate to file? (yes/no)")) == "yes":
                file_name = str(input("Enter a file name "))
                graph_to_file(determ_graph, file_name)
            graph = determ_graph

        if str(input("Do you want to analyze any str? (yes/no)")) == "yes":
            in_str = str(input("Enter a string:\t"))
            analysis_str(in_str, graph)
