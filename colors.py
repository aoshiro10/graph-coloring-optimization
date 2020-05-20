from enum import Enum

class Colors(Enum):
	RED = 0
	GREEN = 1
	BLUE = 2
	YELLOW = 3
	BLACK = 4
	PURPLE = 5
	WHITE = 6

plotColorsDict = dict()
plotColorsDict[Colors.RED] = "red"
plotColorsDict[Colors.GREEN] = "green"
plotColorsDict[Colors.BLUE] = "blue"
plotColorsDict[Colors.YELLOW] = "yellow"
plotColorsDict[Colors.BLACK] = "black"
plotColorsDict[Colors.PURPLE] = "purple"
plotColorsDict[Colors.WHITE] = "white"
