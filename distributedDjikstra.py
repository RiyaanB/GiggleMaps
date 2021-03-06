import csv
from utils.heap import Heap
import numpy as np
from utils.Graph import Graph
from utils.Person import Person
import time
from utils.draw import draw
from utils.google_graph_writer import write_google_graph


def simulator(graph: Graph, everyone: list):
	system_age = 0
	for i in everyone:
		i.reset()
	reached = []
	while len(reached) < len(everyone):
		system_age += 1
		for person in everyone:
			if not person.reached():
				person.age += 1
				if person.limbo == 0:
					graph.update_cost(person.path[person.current_pos], person.path[person.current_pos+1], 1)
					person.limbo = graph.edges[person.path[person.current_pos]][person.path[person.current_pos+1]]

				person.limbo -= 1
				if person.limbo == 0:
					graph.update_cost(person.path[person.current_pos], person.path[person.current_pos+1], -1)
					person.current_pos += 1
					if person.reached():
						reached.append(person)
						person.already_reached = True
						continue
			elif not person.already_reached:
				person.already_reached = True
				reached.append(person)
			else:
				pass

	user_sum_age = 0
	for person in reached:
		user_sum_age += person.age
		# print(person.path)
	return system_age, user_sum_age/len(reached)


def google_maps(graph: Graph, everyone: list):
	system_age = 0
	reached = []
	for person in everyone:
		person.path.extend(dijkstra(graph, person.start, person.end)[1])
		person.next_node = 1
	while len(reached) < len(everyone):
		system_age += 1
		for person in everyone:
			if not person.reached():
				person.age += 1
				if person.limbo == 0:
					person.next_node = person.current_pos + 1
					graph.update_cost(person.path[person.current_pos], person.path[person.next_node], 1)
					person.limbo = graph.edges[person.path[person.current_pos]][person.path[person.next_node]]

				person.limbo -= 1
				if person.limbo == 0:
					graph.update_cost(person.path[person.current_pos], person.path[person.current_pos+1], -1)
					person.nodes_visited.add(person.path[person.current_pos])
					person.current_pos += 1
					if person.reached():
						reached.append(person)
						person.already_reached = True
						continue
			elif not person.already_reached:
				person.already_reached = True
				reached.append(person)
			else:
				pass
	return reached


def giggle_maps(graph: Graph, everyone: list):
	system_age = 0
	reached = []
	while len(reached) < len(everyone):
		system_age += 1
		for person in everyone:
			if not person.reached():
				person.age += 1
				if person.limbo == 0:
					person.path = person.path[:person.current_pos+1]
					person.path.extend(dijkstra(graph, person.path[person.current_pos], person.end)[1])
					person.next_node = person.current_pos + 1
					graph.update_cost(person.path[person.current_pos], person.path[person.next_node], 1)
					person.limbo = graph.edges[person.path[person.current_pos]][person.path[person.next_node]]

				person.limbo -= 1
				if person.limbo == 0:
					graph.update_cost(person.path[person.current_pos], person.path[person.next_node], -1)
					person.current_pos += 1
					person.nodes_visited.add(person.path[person.current_pos])
					if person.reached():
						person.already_reached = True
						reached.append(person)
						continue
			elif not person.already_reached:
				reached.append(person)
				person.already_reached = True
			else:
				pass

	return reached


class SpecialMinHeap(Heap):
	def greater(self, a, b):
		return a if self.m_heap[a]['distance'] < self.m_heap[b]['distance'] else b


def dijkstra(graph, start, end):
	'''
	This function returns a tuple of least distance and the best path to be taken from start + 1 to end
	TODO: figure out optimum way to recalculate
			dijkstra by only recalculating wrt
			the edge whose cost has changed
	'''

	nodes = {node: {'distance': (0 if node == start else np.inf), 'path_via': None, 'done': False, 'name': node} for node in graph.nodes}

	pq = SpecialMinHeap()
	pq.push(nodes[start])

	while not pq.empty():
		current_master_node = pq.pop()

		if current_master_node['name'] == end:
			route = [end]
			path_via = end

			while path_via != start:
				route.append(nodes[path_via]['path_via'])
				path_via = route[-1]

			return nodes[end]['distance'], route[-2::-1]

		if current_master_node['done']:
			continue

		for adj_node, distance in graph.edges[current_master_node['name']].items():
			if not nodes[adj_node]['done']:
				distance += current_master_node['distance']

				if nodes[adj_node]['distance'] > distance:
					nodes[adj_node]['distance'] = distance
					nodes[adj_node]['path_via'] = current_master_node['name']
					pq.push(nodes[adj_node])

		current_master_node['done'] = True

	raise RuntimeError('End point not found')


if __name__ == '__main__':
	write_google_graph('Four Seasons Hotel, Mumbai', 'Dhirubhai Ambani International School, Mumbai')
	a = 'google_graph_detailed.txt'
	b = 'google_people.txt'
	#b = 'test_persons/people8.csv'

	graph = Graph(a)
	graph2 = Graph(a)
	draw(graph)
	people = []
	people2 = []
	with open(b, 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			people.append(Person(row[0], row[1]))
			people2.append(Person(row[0], row[1]))

	start = time.time()
	print(simulator(graph2, giggle_maps(graph2, people2)))
	end = time.time()
	print(end - start)

	start = time.time()
	print(simulator(graph, google_maps(graph, people)))
	end = time.time()
	print(end - start)

