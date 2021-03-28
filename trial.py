from distributedDjikstra import dijkstra
from Graph import Graph

graph = Graph('test_graphs/graph2.csv')

print(dijkstra(graph, '1', '3'))