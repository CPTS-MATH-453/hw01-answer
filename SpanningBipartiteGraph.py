from Graph import *

class SpanningBipartiteGraph:
    def __init__(self, set_X, G):
        self.num_nodes_X = len(set_X)
        self.num_nodes_Y = G.num_nodes - self.num_nodes_X
        self.set_X = set_X
        self.set_Y = set(range(G.num_nodes)) - self.set_X
        # Initialize a 2D matrix with zeros, with X as row, Y as column
        self.adj_matrix = [[0] * self.num_nodes_Y for _ in range(self.num_nodes_X)]
        xi = 0
        for x in self.set_X:
            yi = 0
            for y in self.set_Y:
                if G.is_adjacent(x, y):
                    self.add_edge(xi, yi)
                yi += 1
            xi += 1

    def add_edge(self, nodeX, nodeY):
        # Add an undirected edge between node1 and node2
        self.adj_matrix[nodeX][nodeY] = 1

    def remove_edge(self, nodeX, nodeY):
        # Remove the edge between node1 and node2
        self.adj_matrix[nodeX][nodeY] = 0

    def num_edges(self):
        num_edges = 0
        for row in self.adj_matrix:
            num_edges += sum(row)
        return num_edges

    def print_graph(self):
        # Print the Bipartite graph
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    test_graph = Graph(4)
    # test_graph.print_graph()
    test_graph.add_edge(1,2)
    test_graph.add_edge(3,0)
    test_graph.add_edge(3,2)
    test_graph.add_edge(3,2)
    sb_graph = SpanningBipartiteGraph({0, 2}, test_graph)
    sb_graph.print_graph()
    print("Number of edges is", sb_graph.num_edges())