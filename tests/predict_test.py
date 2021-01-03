"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.file import *
from package.algorithm import *

PREDICT_FILE_NAME = 'test-predict.data'
DATASET_FILE_NAME = 'agaricus-lepiota.data'


def predict_test():
    samples_file_name = PATH + PREDICT_FILE_NAME
    dataset_file_name = PATH + DATASET_FILE_NAME

    samples = get_samples_to_predict_from_file(samples_file_name)

    classifiers = [EDIBLE, POISONOUS]
    input_attributes = generate_input_attributes()
    dataset = get_dataset_from_file(dataset_file_name)

    decision_tree = id3(classifiers, input_attributes, dataset)

    for i in range(len(samples)):
        print(predict_edibility(samples[i], decision_tree))
