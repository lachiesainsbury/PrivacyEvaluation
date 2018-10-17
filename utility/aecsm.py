import numpy as np
import scanner

# Average Equivalence Class Size Metric
# BEST CASE -> Each record is generalised in an EQ of k records


def calculateAECSM():
    print("Average Equivalence Class Size Metric")

    # T = Table
    x, y = scanner.readData("data/adult.csv")
    # |T| = Number of Records
    z = len(x)
    # |EQs| = Number of Equivalence Classes
    num = scanner.numberOfEquivalenceClasses("data/adult.csv")
    # k = Privacy Requirement -> k-anonymity
    k = 1
    # FORMULA -> T = |T| / |EQs| * k
    avg = z / (num * k)
    print("Original Dataset -> " + "%.2f" % avg)



    # T = Table
    x, y = scanner.readData("data/2-anonymised.csv")
    # |T| = Number of Records
    z = len(x)
    # |EQs| = Number of Equivalence Classes
    num = scanner.numberOfEquivalenceClasses("data/2-anonymised.csv")
    # k = Privacy Requirement -> k-anonymity
    k = 2
    # FORMULA -> T = |T| / |EQs| * k
    avg = z / (num * k)
    print("k = 2 -> " + "%.2f" % avg)



    x, y = scanner.readData("data/10-anonymised.csv")
    # |T| = Number of Records
    z = len(x)
    # |EQs| = Number of Equivalence Classes
    num = scanner.numberOfEquivalenceClasses("data/10-anonymised.csv")
    # k = Privacy Requirement -> k-anonymity
    k = 10
    # FORMULA -> T = |T| / |EQs| * k
    avg = z / (num * k)
    print("k = 10 -> ""%.2f" % avg)



    x, y = scanner.readData("data/50-anonymised.csv")
    # |T| = Number of Records
    z = len(x)
    # |EQs| = Number of Equivalence Classes
    num = scanner.numberOfEquivalenceClasses("data/50-anonymised.csv")
    # k = Privacy Requirement -> k-anonymity
    k = 50
    # FORMULA -> T = |T| / |EQs| * k
    avg = z / (num * k)
    print("k = 50 -> ""%.2f" % avg)


    x, y = scanner.readData("data/100-anonymised.csv")
    # |T| = Number of Records
    z = len(x)
    # |EQs| = Number of Equivalence Classes
    num = scanner.numberOfEquivalenceClasses("data/100-anonymised.csv")
    # k = Privacy Requirement -> k-anonymity
    k = 100
    # FORMULA -> T = |T| / |EQs| * k
    avg = z / (num * k)
    print("k = 100 -> ""%.2f" % avg)




