from Graph import Graph
from SpanningBipartiteGraph import *

def sbg(g):
    # TODO: Find a spanning bipartite graph such that |E(F)| ≥ 1/2 |E(G)|.
    # Input: Graph g.
    # Output: BipartiteGraph bg.
    set_X = set()
    set_Y = set()
    for i in range(g.num_nodes):
        num_edges_X = g.num_edges_in_set(i, set_X)
        num_edges_Y = g.num_edges_in_set(i, set_Y)
        if num_edges_X > num_edges_Y:
            set_Y.add(i)
        else:
            set_X.add(i)

    print(set_X)

    return set_X

if __name__ == "__main__":
    test_graph = Graph(4)
    # test_graph.print_graph()
    test_graph.add_edge(1,2)
    test_graph.add_edge(3,0)
    test_graph.add_edge(1,0)
    test_graph.add_edge(3,2)
    test_graph.add_edge(3,2)
    sb_graph = SpanningBipartiteGraph(sbg(test_graph), test_graph)
    sb_graph.print_graph()
    print("Number of edges is", sb_graph.num_edges())
