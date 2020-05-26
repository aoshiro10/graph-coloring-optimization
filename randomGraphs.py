from random import randint

VERTICES_MIN = 20
VERTICES_MAX = 60

EDGES_MIN = 1 #Per Vertex
EDGES_MAX = 6 #Per Vertex


# Creates a square matrix representing the graph
def createMatrix(width):
	return [([0] * width) for i in range(width)]


def buildGraph(file_name):
	vertices = randint(VERTICES_MIN, VERTICES_MAX)
	# Matrix representation of the graph.
	# Since there are no self-loop the top left to bottom right diagonal
	# would be completely empty. For space efficiency, that diagonal will be used
	# to store the number of edges connecting a single vertex.
	matrix = createMatrix(vertices)

	#Used to get random edges
	sampleVertices = range(0, vertices)

	for vertexI in range(vertices):
		edgesCount = randint(EDGES_MIN, EDGES_MAX)

		# Get number of edges already connecting the vertex
		edgeI = matrix[vertexI][vertexI]

		iteration = 0
		# break while loop if there is no more vertex to connect.
		while edgeI < edgesCount and iteration < vertices:
			vertexJ = randint(0, vertices-1)

			# No self-loop  
			# No duplicate edge 
			# No vertices w/ more than EDGES_MAX edges.
			if (vertexI != vertexJ and 
				matrix[vertexI][vertexJ] == 0 and 
				matrix[vertexJ][vertexJ] < EDGES_MAX):

				matrix[vertexI][vertexJ] = 1
				matrix[vertexJ][vertexI] = 1

				matrix[vertexI][vertexI] += 1
				matrix[vertexJ][vertexJ] += 1

				edgeI += 1

			iteration += 1

	matrixToFile(matrix, file_name)

def matrixToFile(matrix, file_name):
	text = ""

	for row in range(len(matrix)):
		text += str(row) + " "
		for col in range(len(matrix)):
			if row != col and matrix[row][col]:
				text += str(col) + ","
		text += "\n"

	f = open(file_name, "w")
	f.write(text)
	f.close()
