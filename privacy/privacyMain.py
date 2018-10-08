import scanner
import privacy.util as util
import numpy as np
import privacy.novelEntropy as ne

if __name__ == '__main__':

    x, y = scanner.readDataAsInts("../data/adult.csv")
    # transpose = list(map(list, zip(*x)))
    x = np.asarray(x)
    transpose = np.rot90(x)
    for i in range(len(transpose)):
        ageProb = util.probabibilityDict(transpose[i])
        p = list(ageProb.values())
        print(ne.novelEntropyBasedMeasure(p))
