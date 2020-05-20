from graphs import *
from geneticAlgorithm import *
from visualizeGraph import *

colorNum = 3
graph = Graph("graph1.gx", colorNum)
graph.setRandomColoring()

print(fitness(graph))

plotGraph(graph)
