import numpy as np
from scanner import readHierarchy
import glob


def probabilities(data):
    x = np.asarray(data)
    transpose = np.rot90(x)
    probabilities = [probabibilityDict(i) for i in transpose]
    probabilities.reverse()
    newProbabilities = adultGeneralisedProbability(probabilities)
    return newProbabilities


def probabibilityDict(x):
    unique, counts = np.unique(x, return_counts=True)
    prob = []
    for i in counts:
        prob.append(i / len(x))

    prob = dict(zip(unique, prob))
    return prob


def adultGeneralisedProbability(probabilities):
    heirarchy = buildHierarchies()

    for row in range(len(probabilities)):
        keys = list(probabilities[row].keys())
        for k in keys:
            if k in heirarchy[row]:#k is generalised
                #print(k)
                kProb = probabilities[row].pop(k) # remove generalised term from probabilities & get the prob
                lessGeneralised = heirarchy[row][k]
                for i in lessGeneralised:
                    currentProb = 0
                    if i in probabilities[row]:
                        currentProb = probabilities[row][i]
                    probabilities[row][i] = (kProb/len(lessGeneralised)) + currentProb

    return probabilities





def buildHierarchies():
    filenames = glob.glob("../data/arx/hierarchies/adult/*.csv")
    fileHierarchies = []
    for file in filenames:
        hierarchy = readHierarchy(file)
        [i.reverse() for i in hierarchy]# most generalised on the left, original on the right
        h = {}
        for path in hierarchy:
            for i in range(len(path)-1):
                if path[i] not in h:
                    h[path[i]] = set()
                h[path[i]].add(path[-1])
        fileHierarchies.append(h)



    return fileHierarchies



if __name__ == "__main__":
    for i in buildHierarchies():
        print(i)