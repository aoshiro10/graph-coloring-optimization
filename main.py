import numpy as np
from graphs import *
from geneticAlgorithm import *
from visualizeGraph import *
import sampleParents
import pdb

colorNum = 4
graphPath = "graph2.gx"
population = createInitialPopulation(graphPath, colorNum)
bestGraph = None
generations = 0
MAX_GENS = int(1e3)
mating_fn = matingHalfHalf
verbose = True

while generations < MAX_GENS:
    generations += 1

    fitnessScores, bestGraph = evaluateGeneration(population)

    plotGraph(bestGraph, generations)

    if verbose:
        print("fitness:", fitness(bestGraph))

    if fitness(bestGraph) == 1:
        break

    parents = sampleParents.sampleBestParents(fitnessScores)
    newPopulation = []
    for (idxParent1, idxParent2) in parents:
        parent1, parent2 = population[idxParent1], population[idxParent2]
        child = mating_fn(parent1, parent2)
        newPopulation.append(child)

    population = newPopulation
    population[0] = bestGraph.copy() # set best graph for mutation
    mutateGeneration(population)
    population[1] = bestGraph.copy() # want to make sure the best member stays

plotGraph(bestGraph, generations)
print(generations)

while True:
    pass

