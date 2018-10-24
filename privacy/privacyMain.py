import scanner
import privacy.util as util
import numpy as np
import privacy.novelEntropy as ne

if __name__ == '__main__':

    x, y = scanner.readData("../data/full-anonymised.csv")
    # transpose = list(map(list, zip(*x)))
    prob = util.probabilities(x)
    for i in prob:
        p = list(i.values())
        print(ne.novelEntropyBasedMeasure(p))