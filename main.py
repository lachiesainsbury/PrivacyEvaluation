import scanner
import utility.genILoss as gl
import utility.aecsm as aecsm


if __name__ == '__main__':

    x, y = scanner.readData("data/adult.csv")
    # print(x[0], y[0])

    gl.calcGenILoss(x, y)
    aecsmresult = aecsm.calculateAECSM()
    print(aecsmresult)
