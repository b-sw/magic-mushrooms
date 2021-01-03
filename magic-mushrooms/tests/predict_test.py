"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.file import *
from package.algorithm import *

DATASET_FILE_NAME = 'agaricus-lepiota.data'


def predict_test():
    dataset_file_name = PATH + DATASET_FILE_NAME

    classifiers = [EDIBLE, POISONOUS]
    input_attributes = generate_input_attributes()
    dataset = read_dataset_from_file(dataset_file_name)
    training_set, test_set = split_dataset(dataset)

    decision_tree = id3(classifiers, input_attributes, training_set)

    for sample in test_set:
        print(predict_edibility(sample, decision_tree))
