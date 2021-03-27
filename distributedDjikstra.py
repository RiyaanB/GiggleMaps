# PSEUDOCODE:

# TODO: Consider dividing each edge into a bunch of sub graphs
# 	to accommodate for multiple people being on 1 road


from collections import defaultdict
import csv
from heap import Heap
import numpy as np
from Graph import Graph


def main():
	graph = Graph('graph.txt')

	people = 3

	with open('start_end.txt') as f:
		people = [Person(row[0], row[1]) for row in csv.reader(f)]

	while people:
		for person in people:
			if not person.reached():
				route = dijkstra(person.current_pos, person.end)
				next_pos = route[0]
				if not person.current_pos == person.start:
					graph.update_cost(person.prev_pos, person.current_pos, value=-1) # reduces cost of the edge the person is no longer on

				graph.update_cost(person.current_pos, next_pos, value=1) # increases cost of the edge on which person travels
				person.prev_pos = person.current_pos
				person.move(next_pos)

			else:
				people.remove(person)

class Person:
	
	def __init__(self, start=None, end=None):
		self.current_pos = None
		
		self.start = start
		self.end = end
		self.prev_pos = None

		self.route_taken = [self.start]

	def reached(self):
		return self.current_pos==self.end

	def move(self, pos):
		'''
		This method will change current position
		of the person and will also append this 
		new position to self.route_taken
		'''

		self.current_pos = pos
		self.route_taken.append(self.current_pos)




class SpecialMinHeap(Heap):
	def greater(self, a, b):
		return a if self.m_heap[a]['distance'] < self.m_heap[b]['distance'] else b
	
	
def dijkstra(graph, start, end):
	'''
	This function returns a tuple of least distance and the best path to be taken from start to end

	TODO: figure out optimum way to recalculate
			dijkstra by only recalculating wrt
			the edge whose cost has changed
	'''
	
	# TODO: write this damn function
	nodes = {node: {'distance': (0 if node == start else np.inf), 'path_via': None, 'done': False} for node in graph.nodes}
	
	pq = SpecialMinHeap()
	pq.push(nodes[start])
	
	while True:
		current_master_node = pq.pop()

		if current_master_node == end:
			break
		if nodes[current_master_node]['done']:
			continue

		for adj_node, distance in graph.edges[start].items():
			if not nodes[adj_node]['done']:
				distance += current_master_node['distance']

				if nodes[adj_node]['distance'] > distance: # What about ==
					nodes[adj_node]['distance'] = distance
					nodes[adj_node]['path_via'] = current_master_node
					pq.push(nodes[adj_node]) #pass by reference, pass by value

		nodes[current_master_node]['done'] = True

	route = [end]
	path_via = nodes[end]['path_via']

	while path_via != start:
		route.append(nodes[path_via]['path_via'])
		path_via = route[-1]

	return (nodes[end]['distance'], route[-1::])



if __name__ == '__main__':
	main()
