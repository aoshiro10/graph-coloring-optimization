class Vertex:
	def __init__(self, name):
		self.name = name
		self.color = None
		self.neighbors = []

	def setColor(self, color):
		self.color = color

	def __repr__(self):
		neighborNames = ""
		for neighbor in self.neighbors:
			neighborNames += (neighbor.name + " ")
		return "Vertex: " + self.name + "\n" + "Neighbors: " + neighborNames

class Graph:

	def __init__(self, filename):
		self.vertices = Graph.getVertices(filename)
		for vertex in self.vertices:
			print(vertex)

	@staticmethod
	def getVertices(filename):
		graphText = open(filename, 'r')
		verticesDict = {} #vertex name -> vertex object

		while True:
			vertexLine = graphText.readline() 
			if not vertexLine:
				break

			lineValues = vertexLine.split(" ")
			vertexName = lineValues[0]
			vertex = verticesDict.get(vertexName, Vertex(vertexName))
			verticesDict[vertexName] = vertex
			neighborsNames = lineValues[1].strip().split(",")
			for neighborName in neighborsNames:
				neighbor = verticesDict.get(neighborName, Vertex(neighborName))
				verticesDict[neighborName] = neighbor
				vertex.neighbors.append(neighbor)

		graphText.close()

		vertices = []
		for verticeNames in verticesDict:
			vertices.append(verticesDict[verticeNames])

		return vertices


