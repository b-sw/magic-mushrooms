"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from math import log2
from mushroom import *


def class_proportion(classifier, collection):
    samples = 0

    for i in range(len(collection)):
        if collection[i].attributes[CLASSIFIER_IDX] == classifier:
            samples += 1

    return samples / len(collection)


def possible_values(attribute_idx, collection):
    values = []

    for i in range(len(collection)):
        sample_value = collection[i].attributes[attribute_idx]
        if sample_value not in values:
            values.append(sample_value)

    return values


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
        fi = class_proportion(collection, classifiers[i])  # na wykładzie było oznaczone jako f_i
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
