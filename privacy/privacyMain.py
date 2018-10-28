import os

import matplotlib.pyplot as plt

import scanner
import privacy.util as util
import privacy.novelEntropy as ne
from privacy import AttributeEquivocation as ae


# iterate over list of given folders, output a graph in out directory for each dataset
def att_equiv_graphs(input_folders, graph_out_dir):
    if not os.path.exists(graph_out_dir):
        os.makedirs(graph_out_dir)

    for folder in input_folders:
        for entry in os.scandir("../data/{}".format(folder)):
            if entry.is_file():
                file = entry.name
                name = "{}_{}".format(os.path.dirname(folder).replace("/", "_"), os.path.splitext(file)[0])
                x = scanner.read_data_columns("../data/{}{}".format(folder, file))
                attribute = list(x.keys())[-1]
                ae.export_attribute_equivocation_graph("{}_{}".format(name, attribute), x[attribute],
                                                       graph_out_dir)


if __name__ == '__main__':
    # x, y = scanner.readData("../data/full-anonymised.csv")
    # prob = util.probabilities(x)
    # for i in prob:
    #     p = list(i.values())
    #     print(ne.novelEntropyBasedMeasure(p))

    att_equiv_graphs(["",
               "adult/income-values/",
               "bike-sharing/"], "../graphs/AttEquiv/")
