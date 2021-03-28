from distributedDjikstra import simulator, google_maps, giggle_maps
from Graph import Graph
from main import draw
import csv
from Person import Person
import matplotlib.pyplot as plt


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


graph = Graph('test_graphs/graph7.csv')
graph2 = Graph('test_graphs/graph7.csv')

people = []
people2 = []


with open('test_persons/people7.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			people.append(Person(row[0], row[1]))
			people2.append(Person(row[0], row[1]))

print("GOOGLE PATHS:")
google = simulator(graph, google_maps(graph, people))
# print(f"System Age for Google Maps:", google[0])
print(f"Avg Time Taken/Person for Google Maps:", google[1])
print("")
print("GIGGLE PATHS:")
giggle = simulator(graph2, giggle_maps(graph2, people2))
# print(f"System Age for Giggle Maps:", giggle[0])
print(f"Avg Time Taken/Person for Giggle Maps:", giggle[1])

print('\n\n\n')