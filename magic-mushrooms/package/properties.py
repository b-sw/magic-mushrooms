"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from math import log, floor
from package.mushroom import *

TRAINING_SET_PROPORTION = 0.8

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
    subsets = []

    for value in values:
        subsets.append([])

    for element in collection:
        sample_value = element.attributes[attribute]
        subset_idx = values.index(sample_value)

        subsets[subset_idx].append(element)

    return values, subsets


def subcollection_by_attribute(attribute_idx, attribute_value, collection):
    subcollection = []

    for i in range(len(collection)):
        if collection[i].attributes[attribute_idx] == attribute_value:
            subcollection.append(collection[i])

    return subcollection


def entropy(collection):
    classifiers = [EDIBLE, POISONOUS]
    eta = 0  # entropia to z definicji eta(X)

    for classifier in classifiers:
        freq = class_proportion(classifier, collection)  # na wykładzie oznaczone jako f_i
        if freq != 0:
            eta += freq * log(freq)

    return -eta


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


def split_dataset(dataset):
    split_idx = floor(len(dataset) * TRAINING_SET_PROPORTION)
    training_set = dataset[:split_idx]
    test_set = dataset[split_idx:]

    return training_set, test_set
    