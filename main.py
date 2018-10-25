import scanner
import utility.genILoss as gil
import utility.aecsm as aecsm
import utility.discMetric as dm


if __name__ == '__main__':
    aecsmarray = []
    kvalues = [1,2,10,50,100]
    datasets = ["data/adult.csv", "data/2-anonymised.csv", "data/10-anonymised.csv", "data/50-anonymised.csv", "data/100-anonymised.csv"]
    dmarray = []

    x, y = scanner.readData("data/2-anonymised.csv")

    print("Generalized Information Loss: ", gil.calcGenILoss(x), "\n")


    # Average Equivalence Class Size Metric
    for i in range(len(kvalues)):
        aecsmarray.append(aecsm.calculateAECSM(kvalues[i], datasets[i]))
    print("Average Equivalence Class Size Metric")
    for i in range(len(kvalues)):
        print("k = " + str(kvalues[i]) + " -> " + aecsmarray[i])


    print("")
    #Discernibility Metric
    for i in range(len(kvalues)):
        dmarray.append(dm.calcDiscernibilityMetric(kvalues[i], datasets[i]))
    # print(dm.calcDiscernibilityMetric(3, "data/test.csv"))
    print("Discernibility Metric")
    for i in(range(len(kvalues))):
       print("k = " + str(kvalues[i]) + " -> " + dmarray[i])

