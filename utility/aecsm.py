import numpy as np
import scanner

# Average Equivalence Class Size Metric
# BEST CASE -> Each record is generalised in an EQ of k records -> Value of 1


def calculateAECSM(kv, ds):

    # T = Table
    x, y = scanner.readData(ds)
    # |T| = Number of Records
    z = len(x)
    # |EQs| = Number of Equivalence Classes
    num = scanner.numberOfEquivalenceClasses(ds)
    # k = Privacy Requirement -> k-anonymity
    k = kv
    # FORMULA -> T = |T| / |EQs| * k
    avg = z / (num * k)
    return ("%.2f" % avg)



