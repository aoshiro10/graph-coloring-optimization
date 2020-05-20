from graphs import *

NUM_INDIVIDUALS = int(1e3)

# Calculates the fitness of the graph between 0 and 1 (inclusive)
# Fitness is calculate based on the number of vertices with no neighboring vertex with the same color
def fitness(graph):
	correctVertices = 0
	for vertex in graph.getVertices():
		if vertex.differentColorNeighbor():
			correctVertices+=1
	return correctVertices/len(graph.getVertices())

# Creates a list of length NUM_INDIVIDUALS with randomly colored graphs
def createInitialPopulation(graph_path, colorNum):
	population = []
	for _ in range(NUM_INDIVIDUALS):
		graph = Graph("graph1.gx", colorNum)
		graph.setRandomColoring()
		population.append(graph)
	return population

# Evaluates the entire generation and outputs a tuple with three elements
# First element is a list with all the fitness scores
# Second element is the best graph
def evaluateGeneration(population):
	argMax = None
	maxFitness = 0
	fitnessScores = []
	for instance in population:
		fitnessScore = fitness(instance)
		fitnessScores.append(fitnessScore)
		if maxFitness <= fitnessScore:
			argMax = instance
			maxFitness = fitnessScore

	return (fitnessScores, argMax)
