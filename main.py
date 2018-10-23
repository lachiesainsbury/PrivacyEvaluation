import scanner
import utility.genILoss as gil
import utility.aecsm as aecsm
import utility.discMetric as dm


if __name__ == '__main__':

    aecsmarray = []
    kvalues = ["1", "2", "10", "50", "100"]
    dmarray = []

    x, y = scanner.readData("data/adult.csv")

    print("Generalized Information Loss: ", gil.calcGenILoss(x), "\n")


    # Average Equivalence Class Size Metric
    aecsmarray.append(aecsm.calculateAECSM(1, "data/adult.csv"))
    aecsmarray.append(aecsm.calculateAECSM(2, "data/2-anonymised.csv"))
    aecsmarray.append(aecsm.calculateAECSM(10, "data/10-anonymised.csv"))
    aecsmarray.append(aecsm.calculateAECSM(50, "data/50-anonymised.csv"))
    aecsmarray.append(aecsm.calculateAECSM(100, "data/100-anonymised.csv"))
    print("Average Equivalence Class Size Metric")
    for i in range(len(kvalues)):
        print("k = " + kvalues[i] + " -> " + aecsmarray[i])

    print("")
    #Discernibility Metric
    dmarray.append(dm.calcDiscernibilityMetric(1, "data/adult.csv"))
    dmarray.append(dm.calcDiscernibilityMetric(2, "data/2-anonymised.csv"))
    dmarray.append(dm.calcDiscernibilityMetric(10, "data/10-anonymised.csv"))
    dmarray.append(dm.calcDiscernibilityMetric(50, "data/50-anonymised.csv"))
    dmarray.append(dm.calcDiscernibilityMetric(100, "data/100-anonymised.csv"))
    print("Discernibility Metric")
    for i in(range(len(kvalues))):
        print("k = " + kvalues[i] + " -> " + dmarray[i])

