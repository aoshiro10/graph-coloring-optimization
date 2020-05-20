from graphs import *
from geneticAlgorithm import *
from visualizeGraph import *

colorNum = 3
graphPath = "graph1.gx"
population = createInitialPopulation(graphPath, colorNum)

# Careful! This might create infinite graphs
while True:
	fitnessScores, bestGraph = evaluateGeneration(population)
	plotGraph(bestGraph)
	if fitness(bestGraph) == 1:
		break
	# Temporary
	population = createInitialPopulation(graphPath, colorNum)
