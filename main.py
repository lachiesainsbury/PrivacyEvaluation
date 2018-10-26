import scanner
import utility.genILoss as gil
import utility.aecsm as aecsm
import utility.discMetric as dm

if __name__ == '__main__':
    dmarray = []
    aecsmresults = []
    numclasses = []
    tablelength = []
    kvalues = [2, 5, 10, 25, 50, 75, 100]
    datasets = ["data/adult/income-values/2-anonymised.csv", "data/adult/income-values/5-anonymised.csv",
                "data/adult/income-values/10-anonymised.csv", "data/adult/income-values/25-anonymised.csv",
                "data/adult/income-values/50-anonymised.csv", "data/adult/income-values/75-anonymised.csv",
                "data/adult/income-values/100-anonymised.csv"]

    x, y = scanner.readData("data/adult/income-values/adult.csv")

    print("Generalized Information Loss: ", gil.calcGenILoss(x), "\n")

    # Average Equivalence Class Size Metric
    for i in range(len(kvalues)):
        a, b, c = aecsm.calculateAECSM(kvalues[i], datasets[i])
        tablelength.append(a)
        numclasses.append(b)
        aecsmresults.append(c)
    print("Average Equivalence Class Size Metric")
    for i in range(len(kvalues)):
        print("k = " + str(kvalues[i]) + " |EQs| = " + numclasses[i] + " |T| = " + tablelength[i] + " CAVG -> " +
            aecsmresults[i])

    print("")
    # Discernibility Metric
    for i in range(len(kvalues)):
        dmarray.append(dm.calcDiscernibilityMetric(kvalues[i], datasets[i]))
    # print(dm.calcDiscernibilityMetric(3, "data/test.csv"))
    print("Discernibility Metric")
    for i in (range(len(kvalues))):
        print("k = " + str(kvalues[i]) + " -> " + dmarray[i])
