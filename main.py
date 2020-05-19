from graphs import *
from geneticAlgorithm import *

colorNum = 3
graph = Graph("graph1.gx", colorNum)
graph.setRandomColoring()

print(fitness(graph))
