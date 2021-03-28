from distributedDjikstra import simulator, google_maps, giggle_maps
from Graph import Graph
from main import draw
import csv
from Person import Person
import matplotlib.pyplot as plt


graph = Graph('test_graphs/graph3.txt')
graph2 = Graph('test_graphs/graph3.txt')

people = []
people2 = []

with open('test_persons/people_start_end_same.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			people.append(Person(row[0], row[1]))
			people2.append(Person(row[0], row[1]))


print(simulator(graph, google_maps(graph, people)))
print(simulator(graph2, giggle_maps(graph2, people2)))
draw(graph2)

