class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        # Initialize a 2D matrix with zeros
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def add_edge(self, node1, node2):
        # Add an undirected edge between node1 and node2
        self.adj_matrix[node1][node2] = 1
        self.adj_matrix[node2][node1] = 1

    def remove_edge(self, node1, node2):
        # Remove the edge between node1 and node2
        self.adj_matrix[node1][node2] = 0
        self.adj_matrix[node2][node1] = 0

    def num_edges(self):
        num_edges = 1
        for i in range(self.num_nodes):
            for j in range(i+1, self.num_nodes):
                if self.adj_matrix[i][j] == 1:
                    num_edges += 1
        return num_edges

    def num_edges_in_set(self, node, subset):
        # count the number of edges joining the given node and nodes in subset.
        # example input: 1, {0, 2}
        num_edges = 0
        for s in subset:
            if self.adj_matrix[node][s] == 1:
                num_edges += 1
        return num_edges

    def is_adjacent(self, node1, node2):
        if self.adj_matrix[node1][node2] == 1:
            return True
        else:
            return False

    def print_graph(self):
        # Print the adjacency matrix
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    # use case
    test_graph = Graph(3)
    # test_graph.print_graph()
    test_graph.add_edge(1,2)
    # test_graph.print_graph()