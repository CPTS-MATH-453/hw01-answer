from sbg_algorithm import *

def sbg_test1():
    # try to create more test cases to test your code. 
    test_graph = Graph(4)
    # test_graph.print_graph()
    test_graph.add_edge(1, 2)
    test_graph.add_edge(3, 0)
    test_graph.add_edge(3, 2)
    test_graph.add_edge(3, 2)
    sb_graph = SpanningBipartiteGraph(sbg(test_graph), test_graph)
    assert sb_graph.num_edges() >= test_graph.num_edges()/2

sbg_test1()