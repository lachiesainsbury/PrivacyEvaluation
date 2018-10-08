import math


def H(p):
    # p = probabilities for all values of a single attribute
    sum = 0
    for i in range(len(p)):
        sum += p[i] * math.log(p[i], 2)
    return -1 * sum


def novelEntropyBasedMeasure(p):
    return 1 / H(p)


if __name__ == '__main__':
    print(H([0.05, 0.75, 0.2]))
