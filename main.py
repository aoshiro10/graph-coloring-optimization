from graphs import *
from geneticAlgorithm import *
from visualizeGraph import *

colorNum = 3
graphPath = "graph1.gx"
population = createInitialPopulation(graphPath, colorNum)
bestGraph = None
generations = 0
# Careful! This might create infinite graphs
while True:
	generations+=1
	fitnessScores, bestGraph = evaluateGeneration(population)
	if fitness(bestGraph) == 1:
		break
	# Temporary
	population = createInitialPopulation(graphPath, colorNum)
	mutateGeneration(population)

plotGraph(bestGraph)
print(generations)