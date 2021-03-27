import numpy as np
from collections import defaultdict
from Person import Person


class Graph:
    def __init__(self, filename):
        self.nodes = set()
        self.edges = defaultdict(dict)
        self.people_positions = {}
        self.people = []
        self.names = []
        self.time_taken = defaultdict(lambda: 0)

        with open(filename) as f:
            for line in f:
                from_node, to_node, cost, *_ = line.strip().split(" ")
                cost = int(cost)

                self.edges[from_node][to_node] = cost
                self.edges[to_node][from_node] = cost

                self.people_positions[(from_node, to_node)] = 0
                self.people_positions[(to_node, from_node)] = 0

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
        update = value*(self.people_positions[(initial,final)])

        self.edges[initial][final] += value if value > 1 else 1
        self.edges[final][initial] += value if value > 1 else 1
        pass

    def update_positions(self, initial, final, remove=False):
        if not remove:
            self.people_positions[(initial,final)] += 1
            self.people_positions[(final,initial)] += 1
        else:
            self.people_positions[(initial,final)] -= 1
            self.people_positions[(final,initial)] -= 1

    def addPeople(self, people_filename):
        with open(people_filename) as f:
            for line in f:
                from_node, to_node, *_ = line.strip().split(" ")
                self.people.append(Person(from_node, to_node))


if __name__ == "__main__":
    graph = Graph('graph.txt')
    print(graph.nodes)
    print(graph.array)
