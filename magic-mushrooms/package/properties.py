"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from math import log2, floor
from package.mushroom import *

TRAINING_SET_PROPORTION = 0.8
LEFT_SUBSET = 0
RIGHT_SUBSET = 1
PRIMARY_VALUE_IDX = 0


def is_deterministic(collection):
    to_compare = collection[0].attributes[CLASSIFIER_IDX]

    for element in collection:
        if element.attributes[CLASSIFIER_IDX] != to_compare:
            return False

    return True


def empty_input(input_attributes):
    if not input_attributes:
        return True
    else:
        return False


def class_proportion(classifier, collection):
    samples = 0

    for element in collection:
        if element.attributes[CLASSIFIER_IDX] == classifier:
            samples += 1

    return samples / len(collection)


def most_common_class(classifiers, collection):
    best_proportion = class_proportion(classifiers[0], collection)
    most_common_classifier = classifiers[0]

    for i in range(1, len(classifiers)):
        tmp_proportion = class_proportion(classifiers[i], collection)

        if tmp_proportion > best_proportion:
            best_proportion = tmp_proportion
            most_common_classifier = classifiers[i]

    return most_common_classifier


def only_class(collection):
    return collection[0].attributes[CLASSIFIER_IDX]


def possible_values(attribute_idx, collection):
    values = []

    for element in collection:
        sample_value = element.attributes[attribute_idx]
        if sample_value not in values:
            values.append(sample_value)

    return values


def subsets_by_values(attribute, collection):
    values = possible_values(attribute, collection)
    subsets = [[]]

    if len(values) > 1:
        subsets.append([])

    for element in collection:
        sample_value = element.attributes[attribute]

        if values.index(sample_value) == PRIMARY_VALUE_IDX:
            subsets[LEFT_SUBSET].append(element)
        else:
            subsets[RIGHT_SUBSET].append(element)

    return values, subsets


def subcollection_by_attribute(attribute_idx, attribute_value, collection):
    subcollection = []

    for element in collection:
        if element.attributes[attribute_idx] == attribute_value:
            subcollection.append(element)

    return subcollection


def entropy(collection):
    classifiers = [EDIBLE, POISONOUS]
    eta = 0  # entropia to z definicji eta(X)

    for classifier in classifiers:
        freq = class_proportion(classifier, collection)  # na wykładzie oznaczone jako f_i
        if freq != 0:
            eta += -1 * freq * log2(freq)

    return eta


def entropy_by_attribute(attribute_idx, collection):
    eta = 0
    attribute_values = possible_values(attribute_idx, collection)

    for value in attribute_values:
        subcollection = subcollection_by_attribute(attribute_idx, value, collection)
        eta += len(subcollection) / len(collection) * entropy(subcollection)

    return eta


def inf_gain(attribute_idx, collection):
    return entropy(collection) - entropy_by_attribute(attribute_idx, collection)


def arg_max_inf_gain(input_attributes, dataset):
    best_attribute_idx = 0
    best_inf_gain = 0

    for i in range(1, len(input_attributes)):
        current_inf_gain = inf_gain(i, dataset)

        if current_inf_gain > best_inf_gain:
            best_inf_gain = current_inf_gain
            best_attribute_idx = i

    return input_attributes[best_attribute_idx]


def split_dataset(dataset, proportion):
    split_idx = floor(len(dataset) * proportion)
    training_set = dataset[:split_idx]
    test_set = dataset[split_idx:]

    return training_set, test_set
