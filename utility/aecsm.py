import numpy as np
import scanner

# Average Equivalence Class Size Metric
# BEST CASE -> Each record is generalised in an EQ of k records


def calculateAECSM():
    # T = Table
    x, y = scanner.readData("data/2-anonymised.csv")
    # |T| = Number of Records
    z = len(x)
    # |EQs| = Number of Equivalence Classes
    num = scanner.numberOfEquivalenceClasses("data/2-anonymised.csv")
    # k = Privacy Requirement -> k-anonymity
    k = 2
    # FORMULA -> T = |T| / |EQs| * k
    avg = z / num * k
    print("Number of Records: ")
    print(z)
    print("Number of Equivalence Classes")
    print(num)
    print("Average Equivalence Class Size Metric")
    print(avg)



