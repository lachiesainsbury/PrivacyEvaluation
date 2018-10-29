import scanner
import graph
import utility.genILoss as gil
import utility.aecsm as aecsm
import utility.discMetric as dm

if __name__ == '__main__':
    dmarray = []
    aecsmresults = []
    numclasses = []
    tablelength = []
    kvalues = [1, 2, 5, 10, 25, 50, 75, 100]
    datasets = ["data/adult/income-values/adult.csv", "data/adult/income-values/2-anonymised.csv",
                "data/adult/income-values/5-anonymised.csv", "data/adult/income-values/10-anonymised.csv",
                "data/adult/income-values/25-anonymised.csv", "data/adult/income-values/50-anonymised.csv",
                "data/adult/income-values/75-anonymised.csv", "data/adult/income-values/100-anonymised.csv"]

    datasets2 = ["data/bike-sharing/bike-sharing.csv", "data/bike-sharing/2-anonymised.csv",
                "data/bike-sharing/5-anonymised.csv", "data/bike-sharing/10-anonymised.csv",
                "data/bike-sharing/25-anonymised.csv", "data/bike-sharing/50-anonymised.csv",
                "data/bike-sharing/75-anonymised.csv", "data/bike-sharing/100-anonymised.csv"]

    gils1 = []
    gils2 = []

    x, y = scanner.readData("data/adult/k-anonymity-team/2-anonymised.csv")
    print(gil.calcGenILoss(x, "data/arx/hierarchies/k-anonymity-team/"))

    for i in range(len(datasets)):
        x, y = scanner.readData(datasets[i])
        gils1.append(gil.calcGenILoss(x, "data/arx/hierarchies/adult/"))

    for i in range(len(datasets2)):
        x, y = scanner.readData(datasets2[i])
        gils2.append(gil.calcGenILoss(x, "data/arx/hierarchies/bike-sharing/"))


    graph.plotTwo(kvalues, gils1, gils2, "Generalized Information Loss as k increases", "k", "Generalized Information Loss")


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