# PSEUDOCODE:

# TODO: Consider dividing each edge into a bunch of sub graphs
# 	to accommodate for multiple people being on 1 road


from collections import defaultdict
import csv
from heap import Heap
import numpy as np
from Graph import Graph
from Person import Person

def main():
	graph = Graph('graph.txt')

	print(dijkstra(graph, '1', '7'))
	exit()
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

	nodes = {node: {'distance': (0 if node == start else np.inf), 'path_via': None, 'done': False, 'name': node} for node in graph.nodes}
	
	pq = SpecialMinHeap()
	pq.push(nodes[start])
	
	while True:
		current_master_node = pq.pop()

		if current_master_node['name'] == end:
			break

		if current_master_node['done']:
			continue

		for adj_node, distance in graph.edges[current_master_node['name']].items():
			if not nodes[adj_node]['done']:
				distance += current_master_node['distance']

				if nodes[adj_node]['distance'] > distance: # What about ==
					nodes[adj_node]['distance'] = distance
					nodes[adj_node]['path_via'] = current_master_node['name'] 
					pq.push(nodes[adj_node]) 

		current_master_node['done'] = True

	route = [end]
	path_via = end

	while path_via != start:
		route.append(nodes[path_via]['path_via'])
		path_via = route[-1]

	return (nodes[end]['distance'], route[1::-1])



if __name__ == '__main__':
	main()

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