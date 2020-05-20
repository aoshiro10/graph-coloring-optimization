import numpy as np
from sampleParents import * 

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

    return

if __name__ == "__main__":
    test_sampling()
