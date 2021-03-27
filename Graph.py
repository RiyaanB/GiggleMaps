import numpy as np
from collections import defaultdict
from Person import Person


class Graph:
    def __init__(self, filename):
        self.nodes = set()
        self.edges = defaultdict(dict)
        self.people = []
        self.names = []

        with open(filename) as f:
            for line in f:
                from_node, to_node, cost, *_ = line.strip().split(" ")
                from_node = int(from_node)
                to_node = int(to_node)
                cost = int(cost)
                self.edges[from_node][to_node] = cost
                self.edges[to_node][from_node] = cost
                self.nodes.add(from_node)
                self.nodes.add(to_node)

        self.names = [i for i in sorted(self.nodes)]
        array = []

        for name in self.names:
            row = []
            for name2 in self.names:
                try:
                    row.append(self.edges[name][name2])
                except KeyError:
                    row.append(0)
            array.append(row)
        self.array = np.array(array)


    def update_cost(self, initial, final, value=1):
        self.edges[initial][final] += value
        self.edges[final][initial] += value
        pass

    def addPeople(self, people_filename):
        with open(people_filename) as f:
            for line in f:
                from_node, to_node, *_ = line.strip().split(" ")
                self.people.append(Person(from_node, to_node))


if __name__ == "__main__":
    graph = Graph('graph.txt')
    print(graph.nodes)
    print(graph.array)
