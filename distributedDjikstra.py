# PSEUDOCODE:

class Person:
	def __init__(self):
		self.current_pos = None
		self.route_taken = []
		first_move = True

	def reached(self, end):
		return self.current_pos==end

	def move(self, pos):
		'''
		This method will change current position
		of the person and will also append this 
		new position to self.route_taken
		'''
		if first_move:
			self.route_taken.append(self.current_pos)
			first_move = False

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

person1 = Person()
person2 = Person()
person3 = Person()

graph = Graph()

people = [person1, person2, person3]  # list of person objects

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






