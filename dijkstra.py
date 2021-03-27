"""
from collections import defaultdict
import numpy as np
import heapq


class Person:
    def __init__(self, start_node, end_node):
        self.nodes_visited = set()
        self.nodes_visited.add(start_node)
        self.prev_node = start_node
        self.path = []
        self.next_node = ""

    def set_path(self, ls):
        self.path = ls
        self.next_node = self.path[0]

    def get_next_node(self):
        return self.path.pop(0) if self.path else ""



class Graph:
    def __init__(self, filename, people_filename):
        self.nodes = set()
        self.edges = defaultdict(dict)

        with open(filename) as f:
            for line in f:
                from_node, to_node, cost, *_ = line.strip().split(" ")
                self.edges[from_node][to_node] = int(cost)
                self.nodes.add(from_node)
                self.nodes.add(to_node)




def dijkstras_algo(graph, start):
    dists = {node: (0 if node==start else np.inf) for node in graph.nodes}
    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        if current_dist > dists[current_node]:
            continue

        for adj_node, cost in graph.edges[current_node].items():
            dist = current_dist + cost

            if dist < dists[adj_node]:
                dists[adj_node] = dist
                heapq.heappush(priority_queue, (dist, adj_node))

    return dists

def main(graph: Graph, people: list):

	time_taken = 0
	tot=0

	while tot<len(people):

		graph.time_taken = defaultdict(lambda: 0)

		for idx in range(len(people)):
			person = people[idx]
			if not person.reached():

				route = dijkstra(graph, person.current_pos, person.end)
				next_pos = route[1][0]

				graph.update_positions(person.current_pos, next_pos, remove=True)
				person.path.append(next_pos)

				if not person.current_pos == person.start:
					graph.update_cost(person.prev_pos, person.current_pos, value=-1) # reduces cost of the edge the person is no longer on

				graph.update_cost(person.current_pos, next_pos, value=1) # increases cost of the edge on which person travels
				person.prev_pos = person.current_pos

				person.move(next_pos)

				graph.time_taken[(person.prev_pos, person.current_pos)] += 1

				# print(person.path[-2:])

			elif person.already_reached:
				pass

			else:
				# print(f"PERSON {person.name} REACHED, PATH:", person.path)
				person.already_reached = True
				tot+=1

		try:
			time = max(graph.time_taken.values())
			time_taken += time
		except ValueError:
			pass

	return time_taken, [person.path for person in people]



if __name__ == '__main__':
    graph = Graph('graph.txt')
    print(dijkstras_algo(graph, 'A'))

# {
# 'A': {'B': 1, 'C': 2, 'D': 6}, 
# 'B': {'A': 1, 'C': 2, 'E': 4, 'F': 6, 'D': 1}, 
# 'C': {'A': 2, 'B': 2, 'E': 1, 'G': 5, 'F': 3}, 
# 'D': {'A': 6, 'E': 2, 'B': 1, 'G': 5, 'F': 2}, 
# 'E': {'B': 4, 'C': 1, 'D': 2, 'F': 1, 'G': 1}, 
# 'F': {'B': 6, 'C': 3, 'D': 2, 'E': 1}, 
# 'G': {'C': 5, 'D': 5, 'E': 1}
# }

"""
