import scanner
import math


def calcDiscernibilityMetric(kv, ds):


    x, y = scanner.readData("data/adult.csv")

    equivalenceClassArray, equivalenceClassSizes = scanner.returnEQArray(ds)

    k = kv
    dm = 0

    for i in range(len(equivalenceClassArray)):
        if equivalenceClassSizes[i] >= k:
            dm = dm + (equivalenceClassSizes[i] ** 2)

        else:
            dm = dm + (len(x) + equivalenceClassSizes[i])

    return str(dm)

