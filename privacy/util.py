import numpy as np


def probabibilityDict(x):
    unique, counts = np.unique(x, return_counts=True)
    prob = []
    for i in counts:
        prob.append(i / len(x))

    prob = dict(zip(unique, prob))
    return prob
