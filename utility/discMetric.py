import scanner


def calcDiscernibilityMetric():

    print("")
    print("Discernibility Metric")

    # Original Dataset
    x, y = scanner.readData("data/adult.csv")

    equivalenceClassArray, equivalenceClassSizes = scanner.returnEQArray("data/adult.csv")

    k = 1
    dm = 0

    for i in range(len(equivalenceClassArray)):
        if equivalenceClassSizes[i] >= k:
            dm = dm + (equivalenceClassSizes[i] * 2)

        else:
            dm = dm + (len(x) + equivalenceClassSizes[i])

    # print(equivalenceClassArray)
    # print(equivalenceClassSizes)
    # print("Discernibility Metric")
    print("Original Dataset -> " + str(dm))


    # k = 2
    x, y = scanner.readData("data/2-anonymised.csv")

    equivalenceClassArray, equivalenceClassSizes = scanner.returnEQArray("data/2-anonymised.csv")

    k = 2
    dm = 0

    for i in range(len(equivalenceClassArray)):
        if equivalenceClassSizes[i] >= k:
            dm = dm + (equivalenceClassSizes[i] * 2)

        else:
            dm = dm + (len(x) + equivalenceClassSizes[i])

    # print(equivalenceClassArray)
    # print(equivalenceClassSizes)
    # print("Discernibility Metric")
    print("k = 2 -> " + str(dm))



    # k = 10
    x, y = scanner.readData("data/10-anonymised.csv")

    equivalenceClassArray, equivalenceClassSizes = scanner.returnEQArray("data/10-anonymised.csv")

    k = 10
    dm = 0

    for i in range(len(equivalenceClassArray)):
        if equivalenceClassSizes[i] >= k:
            dm = dm + (equivalenceClassSizes[i] * 2)

        else:
            dm = dm + (len(x) + equivalenceClassSizes[i])

    # print(equivalenceClassArray)
    # print(equivalenceClassSizes)
    # print("Discernibility Metric")
    print("k = 10 -> " + str(dm))



    # k = 50
    x, y = scanner.readData("data/50-anonymised.csv")

    equivalenceClassArray, equivalenceClassSizes = scanner.returnEQArray("data/50-anonymised.csv")

    k = 50
    dm = 0

    for i in range(len(equivalenceClassArray)):
        if equivalenceClassSizes[i] >= k:
            dm = dm + (equivalenceClassSizes[i] * 2)

        else:
            dm = dm + (len(x) + equivalenceClassSizes[i])

    # print(equivalenceClassArray)
    # print(equivalenceClassSizes)
    # print("Discernibility Metric")
    print("k = 50 -> " + str(dm))



    # k = 100
    x, y = scanner.readData("data/100-anonymised.csv")

    equivalenceClassArray, equivalenceClassSizes = scanner.returnEQArray("data/100-anonymised.csv")

    k = 100
    dm = 0

    for i in range(len(equivalenceClassArray)):
        if equivalenceClassSizes[i] >= k:
            dm = dm + (equivalenceClassSizes[i] * 2)

        else:
            dm = dm + (len(x) + equivalenceClassSizes[i])

    # print(equivalenceClassArray)
    # print(equivalenceClassSizes)
    # print("Discernibility Metric")
    print("k = 100 -> " + str(dm))



