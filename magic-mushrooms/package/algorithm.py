"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.properties import *
from package.node import *


def id3(classifiers, input_attributes, dataset):
    # na początek sprawdzamy dwie wyjątkowe sytuacje
    if is_deterministic(dataset):  # zawiera tylko jedną klasę
        return dataset[0].attributes[CLASSIFIER_IDX]

    elif empty_input(input_attributes):  # wyczerpaliśmy nasze atrybuty wejściowe
        return most_common_class(classifiers, dataset)

    d = arg_max_inf_gain(input_attributes, dataset)
    d_values, sub_datasets = sub_datasets_by_values(d, dataset)
    input_attributes.remove(d)

    root = Node(d, d_values)
    sub_nodes = []

    for i in range(len(d_values)):
        sub_nodes.append(id3(classifiers, input_attributes, sub_datasets[i]))

    print('Atrybut nr {}'.format(d))
    print(sub_nodes)
    print('\n')

    root.children = sub_nodes
    return root
