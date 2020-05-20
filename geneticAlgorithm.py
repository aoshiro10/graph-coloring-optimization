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
