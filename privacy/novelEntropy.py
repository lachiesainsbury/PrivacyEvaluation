import math

def novelEntropyBasedMeasure(p):
    sum = 0
    for i in range(len(p)):
        sum += p[i] * math.log(p[i], 2)
    H = -1 * sum

    return 1 / H


if __name__ == '__main__':
    print(H([0.05, 0.75, 0.2]))
