from random import randint
from random import sample

VERTICES_MIN = 20
VERTICES_MAX = 60

EDGES_MIN = 1 #Per Vertex
EDGES_MAX = 4 #Per Vertex


# Creates a square matrix representing the graph
def createMatrix(width):
	return [([False] * width) for i in range(width)]

def buildGraph():
	vertices = randint(VERTICES_MIN, VERTICES_MAX)
	matrix = createMatrix(vertices)

	#Used to get random edges
	sampleVertices = range(0, vertices)

	for vertexI in range(vertices):
		edgesCount = randint(EDGES_MIN, EDGES_MAX)
		edges = sample(sampleVertices, edgesCount)

		for vertexJ in edges:
			matrix[vertexI][vertexJ] = True
			matrix[vertexJ][vertexI] = True

	matrixToText(matrix)

def matrixToText(matrix):
	text = ""

	for row in range(len(matrix)):
		text += str(row) + " "
		for col in range(len(matrix)):
			if matrix[row][col]:
				text += str(col) + ","
		text += "\n"
	
	return text
