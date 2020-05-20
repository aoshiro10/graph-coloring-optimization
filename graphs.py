from colors import *
import random

class Vertex:
	def __init__(self, name):
		self.name = name
		self.color = Colors.BLACK
		self.neighbors = []

	def setColor(self, color):
		self.color = color

	def differentColorNeighbor(self):
		for neighbor in self.neighbors:
			if neighbor.color == self.color:
				return False
		return True

	'''def __repr__(self):
		neighborNames = ""
		for neighbor in self.neighbors:
			neighborNames += (neighbor.name + " ")
		return "Vertex: " + self.name + "\n" + "Neighbors: " + neighborNames'''

	def __repr__(self):
		return str(self.name)

class Graph:
	def __init__(self, filename, colorNum):
		self.vertices = Graph.buildVertices(filename)
		self.colorNum = colorNum

	def getVertices(self):
		return self.vertices

	def setRandomColoring(self):
		for vertex in self.vertices:
			vertex.color = list(Colors)[random.randint(0,self.colorNum-1)]

	@staticmethod
	def buildVertices(filename):
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
