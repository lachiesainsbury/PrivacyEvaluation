import scanner
import graph
import utility.genILoss as gil
import utility.aecsm as aecsm
import utility.discMetric as dm
from privacy import privacyMain

if __name__ == '__main__':
    dmarray = []
    aecsmresults = []
    numclasses = []
    tablelength = []
    kvalues = [1, 2, 5, 10, 25, 50, 75, 100]
    kvalues2 = [2, 5, 25, 100]
    discernibilityKValues = [2, 5, 10, 25, 50, 75, 100]
    datasetsAdult = ["data/adult/income-values/adult.csv", "data/adult/income-values/2-anonymised.csv",
                "data/adult/income-values/5-anonymised.csv", "data/adult/income-values/10-anonymised.csv",
                "data/adult/income-values/25-anonymised.csv", "data/adult/income-values/50-anonymised.csv",
                "data/adult/income-values/75-anonymised.csv", "data/adult/income-values/100-anonymised.csv"]

    datasetsBikeSharing = ["data/bike-sharing/bike-sharing.csv", "data/bike-sharing/2-anonymised.csv",
                           "data/bike-sharing/5-anonymised.csv", "data/bike-sharing/10-anonymised.csv",
                           "data/bike-sharing/25-anonymised.csv", "data/bike-sharing/50-anonymised.csv",
                           "data/bike-sharing/75-anonymised.csv", "data/bike-sharing/100-anonymised.csv"]

    datasetsBike = ["data/bike-sharing/2-anonymised.csv", "data/bike-sharing/5-anonymised.csv",
                    "data/bike-sharing/25-anonymised.csv", "data/bike-sharing/100-anonymised.csv"]

    discernibilityBikeDataset = ["data/bike-sharing/2-anonymised.csv", "data/bike-sharing/5-anonymised.csv", "data/bike-sharing/10-anonymised.csv",
                    "data/bike-sharing/25-anonymised.csv", "data/bike-sharing/50-anonymised.csv", "data/bike-sharing/75-anonymised.csv",
                     "data/bike-sharing/100-anonymised.csv"]


    # Generalized Information Loss Metric -> Adult Dataset
    lossValues = []
    for i in range(len(datasetsAdult)):
        x, y = scanner.readData(datasetsAdult[i])
        lossValues.append(gil.calcGenILoss(x, "data/arx/hierarchies/adult/"))

    print("Generalized Information Loss Metric -> Adult Dataset")
    for i in range(len(lossValues)):
        print("k = " + str(kvalues[i]) + " GenILoss -> " + str("{0:.2f}".format(lossValues[i])))
    print("")


    # Generalized Information Loss Metric -> Bike Dataset
    lossValues = []
    for i in range(len(datasetsBikeSharing)):
        x, y = scanner.readData(datasetsBikeSharing[i])
        lossValues.append(gil.calcGenILoss(x, "data/arx/hierarchies/bike-sharing/"))

    print("Generalized Information Loss Metric -> Bike Sharing Dataset")
    for i in range(len(lossValues)):
        print("k = " + str(kvalues[i]) + " GenILoss -> " + str("{0:.2f}".format(lossValues[i])))
    print("")


    # Average Equivalence Class Size Metric -> Adult Dataset
    for i in range(len(kvalues)):
        a, b, c = aecsm.calculateAECSM(kvalues[i], datasetsAdult[i])
        tablelength.append(a)
        numclasses.append(b)
        aecsmresults.append(c)
    print("Average Equivalence Class Size Metric -> Adult Dataset")
    for i in range(len(kvalues)):
        print("k = " + str(kvalues[i]) + " |EQs| = " + numclasses[i] + " |T| = " + tablelength[i] + " CAVG -> " +
            aecsmresults[i])


    aecsmresults = []
    numclasses = []
    tablelength = []

    print("")
    # Average Equivalence Class Size Metric -> Bike Sharing Dataset
    for i in range(len(kvalues2)):
        a, b, c = aecsm.calculateAECSM(kvalues2[i], datasetsBike[i])
        tablelength.append(a)
        numclasses.append(b)
        aecsmresults.append(c)
    print("Average Equivalence Class Size Metric -> Bike Sharing Dataset")
    for i in range(len(kvalues2)):
        print("k = " + str(kvalues2[i]) + " |EQs| = " + numclasses[i] + " |T| = " + tablelength[i] + " CAVG -> " +
            aecsmresults[i])


    print("")
    # Discernibility Metric -> Adult Dataset
    for i in range(len(kvalues)):
        dmarray.append(dm.calcDiscernibilityMetric(kvalues[i], datasetsAdult[i]))
    print("Discernibility Metric -> Adult Dataset")
    for i in (range(len(kvalues))):
        print("k = " + str(kvalues[i]) + " -> " + dmarray[i])

    dmarray = []

    print("")
    # Discernibility Metric -> Bike Sharing Dataset
    for i in range(len(discernibilityKValues)):
        dmarray.append(dm.calcDiscernibilityMetric(discernibilityKValues[i], discernibilityBikeDataset[i]))
    print("Discernibility Metric -> Bike Sharing Dataset")
    for i in (range(len(discernibilityKValues))):
        print("k = " + str(discernibilityKValues[i]) + " -> " + dmarray[i])



    # PRIVACY MEASURES BELOW HERE

    # Bike data has been omitted for Confidential Attribute Equivocation and variants due to long processing time.
    print("=== Confidential Attribute Graphs")
    privacyMain.att_equiv_graphs(["confidentialAttributeTesting.csv",
                      "adult/income-values-not-suppressed/adult.csv"],
                     "graphs/AttEquiv/")
    print("=== Confidential Attribute Graphs Can be found in graphs/AttEquiv/")

    print("=== Confidential Equivalence Attribute Values")
    privacyMain.att_equivalence_equiv(
        ["", "adult/income-values-not-suppressed/"])

    print("=== Confidential Equivalence Attribute Values w/ Filter [Age, Education]")
    privacyMain.att_equivalence_equiv_filter(
        [["adult/income-values-not-suppressed/", ["Age", "Education"]]])



