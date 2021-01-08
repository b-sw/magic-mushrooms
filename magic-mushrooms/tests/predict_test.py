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
DECIMAL_POINTS = 2
SCALE = 100


def predict_test(file_name, classifier_idx, separator, proportion):
    dataset, dictionary = read_dataset_from_file(file_name, separator)
    classifiers = dictionary[classifier_idx]

    print('Test set / data set proportion:\t{}'.format(proportion))
    input_attributes = generate_input_attributes(dictionary)

    training_set, test_set = split_dataset(dataset, proportion)
    decision_tree = id3(classifiers, input_attributes, training_set, classifier_idx)

    correct_predictions = 0
    for sample in test_set:
        if predict_classifier(sample, decision_tree, dictionary, classifier_idx) == sample.attributes[classifier_idx]:
            correct_predictions += 1

    accuracy = (round(correct_predictions / len(test_set), DECIMAL_POINTS) * SCALE)
    print('Accuracy:\t{}'.format(round(correct_predictions / len(test_set), DECIMAL_POINTS)))

    return accuracy
