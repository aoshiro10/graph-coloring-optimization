import numpy as np
from graphs import *
from geneticAlgorithm import *
from visualizeGraph import *
import sampleParents
import pdb

colorNum = 3
graphPath = "graph1.gx"
population = createInitialPopulation(graphPath, colorNum)
bestGraph = None
generations = 0
MAX_GENS = int(1e3)
mating_fn = matingHalfHalf
verbose = True
while True or generations > MAX_GENS:
    generations += 1
    fitnessScores, bestGraph = evaluateGeneration(population)

    if verbose:
        print("Sum of Fitness Scores: ", np.sum(fitnessScores))

    if fitness(bestGraph) == 1:
        break

    parents = sampleParents.sampleBestParents(fitnessScores)
    newPopulation = [bestGraph]
    parents = parents[:-1] # get rid of one set of parents to make room for bestGraph
    for (idxParent1, idxParent2) in parents:
        parent1, parent2 = population[idxParent1], population[idxParent2]
        child = mating_fn(parent1, parent2)
        newPopulation.append(child)

    population = newPopulation
    mutateGeneration(population)

plotGraph(bestGraph)
print(generations)
