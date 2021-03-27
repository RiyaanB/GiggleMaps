from collections import defaultdict
import csv
from heap import Heap
import numpy as np
from Graph import Graph
from Person import Person
import time
from plot_graph import plot_graph
from main import draw

def simulator(graph: Graph, everyone: list):
	system_age = 0
	for i in everyone:
		i.age = 0
		i.limbo = 0
		i.current_pos = 0
		i.next_node = 0
		i.already_reached = False
	reached = []
	while len(everyone) != 0:
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
						everyone.remove(person)
						continue
			elif person.already_reached:
				pass
			else:
				person.already_reached = True
				reached.append(person)
				everyone.remove(person)

	user_sum_age = 0
	for person in reached:
		user_sum_age += person.age
		print(person.path)
	return (system_age, user_sum_age)


def google_maps(graph: Graph, everyone: list):
	system_age = 0
	reached = []
	for person in everyone:
		person.path.extend(dijkstra(graph, person.start, person.end)[1])
		person.next_node = 1
	while len(everyone) != 0:
		system_age += 1

		for person in everyone:
			if not person.reached():
				person.age += 1
				if person.limbo == 0:
					graph.update_cost(person.path[person.current_pos], person.path[person.next_node], 1)
					person.limbo = graph.edges[person.path[person.current_pos]][person.path[person.next_node]]
					person.current_pos = person.next_node

				person.limbo -= 1
				if person.limbo == 0:
					graph.update_cost(person.path[person.current_pos-1], person.path[person.current_pos], -1)
					person.nodes_visited.add(person.path[person.current_pos])
					if person.reached():
						person.already_reached = True
						continue
					person.next_node += 1
			elif person.already_reached:
				pass
			else:
				person.already_reached = True
				person.age += 1
				reached.append(person)
				everyone.remove(person)

	return reached


def giggle_maps(graph: Graph, everyone: list):

	system_age = 0
	reached = []
	while len(everyone) != 0:
		system_age += 1
		for person in everyone:
			if not person.reached():
				person.age += 1
				if person.limbo == 0:
					person.path = person.path[:person.current_pos+1]
					person.path.extend(dijkstra(graph, person.path[person.current_pos], person.end)[1])
					graph.update_cost(person.path[person.current_pos], person.path[person.next_node], 1)
					person.limbo = graph.edges[person.path[person.current_pos]][person.path[person.next_node]]
					person.current_pos += 1

				person.limbo -= 1
				if person.limbo == 0:
					graph.update_cost(person.path[person.current_pos-1], person.path[person.current_pos], -1)
					person.nodes_visited.add(person.current_pos)
					if person.reached():
						person.already_reached = True
						continue
					person.next_node += 1
			elif person.already_reached:
				pass
			else:
				person.already_reached = True
				person.age += 1
				reached.append(person)
				everyone.remove(person)

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

			return (nodes[end]['distance'], route[-2::-1])

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
	graph = Graph('graph3.txt')
	graph2 = Graph('graph3.txt')
	with open('test_people.txt') as f:
		people = [Person(row[0], row[1], row[2]) for row in csv.reader(f)]

	with open('test_people.txt') as g:
		people2 = [Person(row[0], row[1], row[2]) for row in csv.reader(g)]

	start = time.time()
	print(simulator(graph, giggle_maps(graph2, people2)))
	end = time.time()
	print(end - start)

	start = time.time()
	print(simulator(graph, google_maps(graph, people)))
	end = time.time()
	print(end - start)


'''
{
'1': {'2': 1, '5': 1, '6': 1}, 
'2': {'1': 1, '3': 1, '4': 1, '7': 1}, 
'3': {'2': 1, '4': 1, '6': 1}, 
'4': {'3': 1, '5': 1, '2': 1, '7': 1}, 
'5': {'4': 1, '1': 1, '6': 1}, 
'6': {'1': 1, '3': 1, '5': 1}, 
'7': {'2': 1, '4': 1}
}
'''

'''
{'1': {'2': 3, '5': 1, '6': 3},
'2': {'1': 3, '3': 1, '4': 1, '7': 1}, 
'3': {'2': 1, '4': 1, '6': 1}, 
'4': {'3': 1, '5': 1, '2': 1, '7': 1}, 
'5': {'4': 1, '1': 1, '6': 1}, 
'6': {'1': 3, '3': 1, '5': 1}, 
'7': {'2': 1, '4': 1}}
'''


