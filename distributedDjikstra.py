# PSEUDOCODE:

# TODO: Consider dividing each edge into a bunch of sub graphs
# 	to accommodate for multiple people being on 1 road


from collections import defaultdict

def main():
	graph = Graph()

	people = 3

	start = 'A'
	end = 'F'

	people = [Person(start, end) for i in range(people)] #Change range value to change number of ppl

	while people:
		for person in people:
			if not person.reached():
				route = dijkstra(person.current_pos, end)
				next_pos = route[0]
				if not person.current_pos==start:
					graph.update_cost(prev_pos, person.current_pos, value=-1) # reduces cost of the edge the person is no longer on

				graph.update_cost(person.current_pos, next_pos, value=1) # increases cost of the edge on which person travels
				prev_pos = person.current_pos
				person.move(next_pos)

			else:
				people.remove(person)

class Person:
	
	def __init__(self, start=None, end=None):
		self.current_pos = None
		
		self.start = start
		self.end = end

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



class Graph:
	def __init__(self, filename):
		self.nodes = set()
		self.edges = defaultdict(dict)

		with open(filename) as f:
			for line in f:
				from_node, to_node, cost, *_ = line.strip().split(" ")
				cost = int(cost)
				self.edges[from_node][to_node] = cost
				self.edges[to_node][from_node] = cost
				self.nodes.add(from_node)
				self.nodes.add(to_node)

	def update_cost(self, initial, final, value=1):
		self.edges[initial][final] += value
		self.edges[final][initial] += value
		pass


def dijkstra(start, end):
	'''
	This function returns an array of the best 
	path to be taken from start to end

	TODO: figure out optimum way to recalculate
			dijkstra by only recalculating wrt
			the edge whose cost has changed
	'''

	pass