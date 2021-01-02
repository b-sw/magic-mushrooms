"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from math import log2
from package.mushroom import *


def is_deterministic(collection):
    to_compare = collection[0].attributes[CLASSIFIER_IDX]

    for i in range(1, len(collection)):
        if collection[i].attributes[CLASSIFIER_IDX] != to_compare:
            return False

    return True


def empty_input(input_attributes):
    if len(input_attributes) == 0:
        return True
    else:
        return False


def class_proportion(classifier, collection):
    samples = 0

    for i in range(len(collection)):
        if collection[i].attributes[CLASSIFIER_IDX] == classifier:
            samples += 1

    return samples / len(collection)


def most_common_class(classifiers, collection):
    if class_proportion(EDIBLE, collection) > class_proportion(POISONOUS, collection):
        return EDIBLE
    else:
        return POISONOUS


def possible_values(attribute_idx, collection):
    values = []

    for i in range(len(collection)):
        sample_value = collection[i].attributes[attribute_idx]
        if sample_value not in values:
            values.append(sample_value)

    return values


def sub_datasets_by_values(attribute, collection):
    values = possible_values(attribute, collection)
    sub_datasets = []

    for i in range(len(values)):
        sub_datasets.append([])

    for i in range(len(collection)):
        sample_value = collection[i].attributes[attribute]
        sub_dataset_idx = values.index(sample_value)

        sub_datasets[sub_dataset_idx].append(collection[i])

    return values, sub_datasets


def sub_collection_by_attribute(attribute_idx, attribute_value, collection):
    sub_collection = []

    for i in range(len(collection)):
        if collection[i].attributes[attribute_idx] == attribute_value:
            sub_collection.append(collection[i])

    return sub_collection


def entropy(collection):
    classifiers = [EDIBLE, POISONOUS]
    eta = 0  # bo entropia to z definicji H(X), gdzie H to nie 'H', a grecka litera eta

    for i in range(len(classifiers)):
        fi = class_proportion(classifiers[i], collection)  # na wykładzie było oznaczone jako f_i
        # print(fi)
        if fi != 0:
            eta += -1 * fi * log2(fi)

    return eta


def entropy_by_attribute(attribute_idx, collection):
    eta = 0
    attribute_values = possible_values(attribute_idx, collection)

    for i in range(len(attribute_values)):
        sub_collection = sub_collection_by_attribute(attribute_idx, attribute_values[i], collection)
        eta += len(sub_collection) / len(collection) * entropy(sub_collection)

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
