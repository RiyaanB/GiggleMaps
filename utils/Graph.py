from collections import defaultdict
import csv


class Graph:
    def __init__(self, filename):
        self.nodes = set()
        self.edges = defaultdict(dict)

        with open(filename) as f:
            data = csv.reader(f)
            for line in data:
                from_node = line[0]
                to_node = line[1]
                cost = int(line[2])

                self.edges[from_node][to_node] = cost
                self.edges[to_node][from_node] = cost

                self.nodes.add(from_node)
                self.nodes.add(to_node)

    def update_cost(self, initial, final, value=1):
        self.edges[initial][final] += value


if __name__ == "__main__":
    graph = Graph('test_graphs/graph.csv')
    print(graph.nodes)
