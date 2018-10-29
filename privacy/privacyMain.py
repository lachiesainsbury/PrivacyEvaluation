import os
import time

import matplotlib.pyplot as plt

import scanner
import privacy.util as util
import privacy.entropy as ne
from privacy import AttributeEquivocation as ae


def att_equivalence_equiv(input_folders):
    for folder in input_folders:
        for entry in os.scandir("data/{}".format(folder)):
            if entry.is_file():
                start_time = time.time()
                file = entry.name
                name = "=== conf_equivalence_equivo_{}_{}".format(os.path.dirname(folder).replace("/", "_"),
                                                            os.path.splitext(file)[0])
                print(name, "starting")
                x = scanner.read_data_columns_equiv("data/{}{}".format(folder, file))
                ae.equivalence_equivocate(x)
                print("{} finished {:0.3f}".format(name, time.time() - start_time))


# filter is applied to whole folder, ie all files in that folder should be instances of same dataset (just more or less anonymised
def att_equivalence_equiv_filter(input_folders):
    for folder_filter in input_folders:
        folder = folder_filter[0]
        filter_values = folder_filter[1]
        for entry in os.scandir("data/{}".format(folder)):
            if entry.is_file():
                file = entry.name
                name = "conf_equivalence_equivo_filter_{}_{}".format(os.path.dirname(folder).replace("/", "_"),
                                                                   os.path.splitext(file)[0])
                print(name, "starting")
                x = scanner.read_data_columns_equiv_filter("data/{}{}".format(folder, file), filter_values)
                ae.equivalence_equivocate(x)


# iterate over list of given datasets, output a graph in out directory for each dataset
def att_equiv_graphs(input_files, graph_out_dir):
    if not os.path.exists(graph_out_dir):
        os.makedirs(graph_out_dir)

    for input_file_path in input_files:
        if os.path.isfile(input_file_path):
            name = "conf_attr_equiv_{}".format(os.path.splitext(os.path.split(input_file_path)[-1])[0])
            read_data_col = scanner.read_data_columns("data/{}".format(input_file_path))
            ae.export_attribute_equivocation_graph(name, read_data_col[list(read_data_col.keys())[-1]], graph_out_dir)

