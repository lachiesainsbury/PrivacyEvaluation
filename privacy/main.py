import scanner
import privacy.util as util
import numpy as np

if __name__ == '__main__':

    x, y = scanner.readDataAsInts("../data/adult.csv")
    #transpose = list(map(list, zip(*x)))
    x = np.asarray(x)
    transpose = np.rot90(x)
    ageProb = util.probabibilityDict(transpose[-1])
    print(ageProb)
    sum = 0
    for i in ageProb:
        sum+=ageProb[i]
    print(sum)