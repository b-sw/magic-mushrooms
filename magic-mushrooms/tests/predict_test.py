"""
    Name: predict_test.py
    Purpose: test building of binary tree and prediction of edibility

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from random import shuffle
from package.file import *
from package.algorithm import *

DECIMAL_POINTS = 2
SCALE = 100
BEGIN_DEPTH = 0
TP = 0
FP = 1
FN = 2
TN = 3
BINARY = 2
EDIBLE = 'e'
POISONOUS = 'p'
MEAN_IDX = 0
MATRIX_IDX = 1
ATTRS = ['edible', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment',
         'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
         'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type',
         'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat']


def predict_test_k_validate(file_name, classifier_idx, separator, k, runs):
    dataset, dictionary = read_dataset_from_file(file_name, separator)
    input_attributes = generate_input_attributes(dictionary, classifier_idx)
    mean_accuracy = 0

    mean_confusion_matrix = [0, 0, 0, 0]
    for _ in range(runs):
        score = k_validate(dataset, dictionary, classifier_idx, input_attributes, k)
        mean_accuracy += score[MEAN_IDX]

        confusion_matrix = score[MATRIX_IDX]
        for i in range(len(confusion_matrix)):
            mean_confusion_matrix[i] += confusion_matrix[i]

    mean_accuracy /= runs
    for i in range(len(mean_confusion_matrix)):
        mean_confusion_matrix[i] /= runs

    print('Number of runs:\t {}'.format(runs))
    print('K-value:\t {}'.format(k))
    print('Average accuracy:\t{}'.format(round(mean_accuracy * 100, DECIMAL_POINTS)))
    print('Average confusion matrix([TP, FN, FP, TN]):\t {}'.format(mean_confusion_matrix))

    # draw final binary tree
    # print('\nFinal decision tree')
    # final_decision_tree = id3(dictionary[classifier_idx], input_attributes, dataset, classifier_idx, BEGIN_DEPTH)


def k_validate(dataset, dictionary, classifier_idx, input_attributes, k):
    # tablia pomyłek
    confusion_matrix = [0, 0, 0, 0]
    # przemieszaj zbiór
    shuffle(dataset)
    subsets = []
    classifiers = dictionary[classifier_idx]
    accuracies = 0

    training_set_len = len(dataset)
    chunk_size = int(training_set_len / k)

    # podziel na równe podzbiory
    for i in range(0, training_set_len, chunk_size):
        subsets.append(dataset[i:i + chunk_size])

    # wykonaj k-walidację krzyżową
    for i in range(k):
        training_set = []
        test_set = subsets[i]

        for j in range(k):
            if i != j:
                training_set += subsets[j]

        decision_tree = id3(classifiers, input_attributes, training_set, classifier_idx, BEGIN_DEPTH)

        correct_predictions = 0
        for sample in test_set:
            prediction = predict_classifier(sample, decision_tree, dictionary, classifier_idx)
            real = sample.attributes[classifier_idx]
            if prediction == real:
                correct_predictions += 1

            confusion_matrix = update_binary_evaluation(confusion_matrix, prediction, real)

        accuracy = correct_predictions / len(test_set)
        accuracies += accuracy

        print('\n')

    accuracies /= k

    return accuracies, confusion_matrix


def update_binary_evaluation(confusion_matrix, prediction, real):
    if prediction == EDIBLE and real == EDIBLE:
        confusion_matrix[TP] += 1
    elif prediction == POISONOUS and real == EDIBLE:
        confusion_matrix[FN] += 1
    elif prediction == EDIBLE and real == POISONOUS:
        confusion_matrix[FP] += 1
    elif prediction == POISONOUS and real == POISONOUS:
        confusion_matrix[TN] += 1

    return confusion_matrix
