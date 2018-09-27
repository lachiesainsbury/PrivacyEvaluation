import scanner
import privacy.util as util

if __name__ == '__main__':

    x, y = scanner.readData("../data/adult.csv")
    transpose = list(map(list, zip(*x)))
    ageProb = util.probabibilityDict(transpose[0])
    sum = 0
    for i in ageProb:
        sum+=ageProb[i]
    print(sum)