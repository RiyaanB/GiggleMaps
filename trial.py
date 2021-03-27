from distributedDjikstra import dijkstra
from Graph import Graph

graph = Graph('graph2.txt')

print(dijkstra(graph, '1', '3'))