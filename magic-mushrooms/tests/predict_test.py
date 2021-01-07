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
TEST_PROPORTIONS = [0.3, 0.5, 0.75, 0.8, 0.9]
SCALE = 100


def predict_test():
    dataset = read_dataset_from_file(DATASET_FILE_NAME)
    classifiers = [EDIBLE, POISONOUS]

    accuracies = []

    for proportion in TEST_PROPORTIONS:
        print('Test set / data set proportion:\t{}'.format(proportion))
        input_attributes = generate_input_attributes()
        training_set, test_set = split_dataset(dataset, proportion)

        decision_tree = id3(classifiers, input_attributes, training_set)

        correct_predictions = 0
        for sample in test_set:
            if predict_edibility(sample, decision_tree) == sample.attributes[0]:
                correct_predictions += 1

        accuracies.append(round(correct_predictions / len(test_set), DECIMAL_POINTS) * SCALE)
        print('Accuracy:\t{}'.format(round(correct_predictions / len(test_set), DECIMAL_POINTS)))

    return accuracies
