# PSEUDOCODE:


def main():
	graph = Graph()

	people = 3

	people = [Person() for i in range(people)] #Change range value to change number of ppl
	start = 'A'
	end = 'F'

	while people:
		for person in people:
			if not person.reached(end):
				route = dijkstra(person.current_pos, end)
				next_pos = route[0]
				graph.update_cost(person.current_pos, next_pos) # increases cost of the edge on which person travels
				person.move(next_pos)

			else:
				people.remove(person)

class Person:
	# I think you should add 2 arguments - Start and end here and then note those values
	def __init__(self):
		self.current_pos = None
		
		self.start = None
		self.end = None

		self.route_taken = [self.start]

	def reached(self, end):
		return self.current_pos==end

	def move(self, pos):
		'''
		This method will change current position
		of the person and will also append this 
		new position to self.route_taken
		'''

		self.current_pos = pos
		self.route_taken.append(self.current_pos)



class Graph:
	def __init__(self):
		pass

	def update_cost(self):
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