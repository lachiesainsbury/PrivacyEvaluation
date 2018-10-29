import math

def entropy(p):
    sum = 0
    for i in range(len(p)):
        sum += p[i] * math.log2(p[i])
    H = -1 * sum

    return H
