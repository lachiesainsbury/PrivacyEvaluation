import matplotlib.pyplot as plt

import scanner
import privacy.util as util
import privacy.novelEntropy as ne
from privacy import AttributeEquivocation

if __name__ == '__main__':

    # x, y = scanner.readData("../data/full-anonymised.csv")
    # prob = util.probabilities(x)
    # for i in prob:
    #     p = list(i.values())
    #     print(ne.novelEntropyBasedMeasure(p))

    x = scanner.read_data_columns("../data/confidentialAttributeTesting.csv")

    for attribute in x:
        probabilities = util.probabibilityDict(x[attribute])

        item = []
        item_prob = []
        for tup in sorted(probabilities):
            item.append(tup)
            item_prob.append(probabilities[tup])
        equiv = AttributeEquivocation.equivocate(item, item_prob)

        print(attribute, equiv)
        print(sum(equiv.values()))
        plt.step(list(equiv.keys()), list(equiv.values()), where="post")
        plt.ylim(0, 4)
        plt.xlim(0, 9)
        plt.grid(True)
        plt.show()
