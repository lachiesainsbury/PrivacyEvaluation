import scanner
import privacy.util as util
import numpy as np
import privacy.novelEntropy as ne
from privacy import AttributeEquivocation

if __name__ == '__main__':

    x, y = scanner.readData("../data/full-anonymised.csv")
    # transpose = list(map(list, zip(*x)))
    prob = util.probabilities(x)
    for i in prob:
        p = list(i.values())
        print(ne.novelEntropyBasedMeasure(p))

    x, y = scanner.read_data_columns("../data/confidentialAttributeTesting.csv")

    for attribute in x:
        probabilities = util.probabibilityDict(x[attribute])

        item = []
        item_prob = []
        for tup in sorted(probabilities):
            item.append(tup)
            item_prob.append(probabilities[tup])

        print(AttributeEquivocation.equivocate(item, item_prob))
