import numpy as np
from colors import *
from graphs import *
from geneticAlgorithm import NUM_INDIVIDUALS
import pdb

def getPrefixSums(lst):
    prefixSums = np.zeros((lst.shape))
    currSum = 0

    for i in range(lst.shape[0]):
        currSum += lst[i]
        prefixSums[i] = currSum
    totalSum = currSum
    
    return prefixSums, totalSum

def singleSample(prefixSums, totalSum):
    u = np.random.uniform(0, 1)
    target = u * totalSum

    low, high = 0, prefixSums.shape[0]
    while low < high:
        mid = low + (high - low) // 2
        if target > prefixSums[mid]:
            low = mid + 1
        else:
            high = mid

    return low

def sampleBestParents(fitnesses):
    fitnesses = np.array(fitnesses)
    prefixSums, totalSum = getPrefixSums(fitnesses)

    samples = np.zeros((NUM_INDIVIDUALS,))
    for i in range(NUM_INDIVIDUALS):
        samples[i] = singleSample(prefixSums, totalSum)

    return samples


def test_sampling():
    fitnesses = [0.1, 0.9]
    samples = sampleBestParents(fitnesses)
    proportions = [np.sum(samples == i) for i in np.unique(samples)]
    print(fitnesses)
    print(proportions)

    fitnesses = [0.23, 0.33, 0.10, 0.50, 0.45]
    samples = sampleBestParents(fitnesses)
    proportions = [np.sum(samples == i) for i in np.unique(samples)]
    print(fitnesses)
    print(proportions)

    fitnesses = np.array([16, 10, 40, 4, 30])
    fitnesses = fitnesses / np.sum(fitnesses)
    samples = sampleBestParents(fitnesses)
    proportions = [np.sum(samples == i) for i in np.unique(samples)]
    print(fitnesses)
    print(proportions)
    pdb.set_trace()

    return
