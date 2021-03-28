import numpy as np
from collections import defaultdict
from Person import Person
import csv


class Graph:
    def __init__(self, filename):
        self.nodes = set()
        self.edges = defaultdict(dict)
        self.people_positions = {}
        self.people = []
        self.names = []
        self.time_taken = defaultdict(lambda: 0)


        with open(filename) as f:
            data = csv.reader(f)
            for line in data:
                from_node = line[0]
                to_node = line[1]
                cost = int(line[2])

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
        self.edges[initial][final] += value
        pass

    def update_positions(self, initial, final, remove=False):
        if not remove:
            self.people_positions[(initial,final)] += 1
        else:
            self.people_positions[(initial,final)] -= 1

    def add_people(self, people_filename):
        with open(people_filename) as f:
            for line in f:
                from_node, to_node, name, *_ = line.strip().split(" ")
                self.people.append(Person(from_node, to_node, name))

    def add_node(self, initial, final, cost=1):
        self.nodes.add(initial)
        self.nodes.add(final)

        self.edges[from_node][to_node] = cost
        self.edges[to_node][from_node] = cost

        pass


if __name__ == "__main__":
    graph = Graph('graph.csv')
    print(graph.nodes)
    print(graph.array)
