import scanner
import utility.genILoss as gil
import utility.aecsm as aecsm
import utility.discMetric as dm


if __name__ == '__main__':

    x, y = scanner.readData("data/adult.csv")

    print("Generalized Information Loss: ", gil.calcGenILoss(x), "\n")

    #aecsm.calculateAECSM()
    #dm.calcDiscernibilityMetric()
