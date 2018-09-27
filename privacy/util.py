def probabibilityDict(x):
    probability = {}

    for i in x:
        probability[i] = x.count(i)/len(x)
    return probability