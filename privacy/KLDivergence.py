import scanner
import privacy.util
import math

originalFile = ""

def KL(data):
    original, y = scanner.readData(originalFile)
    original = privacy.util.probabilities(original)

    anon = privacy.util.probabilities(data)

    attributeSums = 0
    for i in range(len(original)):
        classes = original[i].keys()
        probPairs = []
        # print(classes)
        for j in classes:
            #print(i,j)
            probPairs.append((original[i][j],anon[i][j]))
        # print(probPairs)
        sum = 0
        for i in probPairs:
            sum += dif(i)
        #print(sum)
        attributeSums +=sum
    return attributeSums


def dif(x):
    return (x[0] * (math.log(x[0]/x[1])))