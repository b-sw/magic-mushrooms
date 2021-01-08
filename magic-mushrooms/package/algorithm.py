"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.properties import *
from package.node import *

BOTH = 2


def id3(classifiers, input_attributes, training_set, classifier_idx):
    if is_deterministic(training_set, classifier_idx):
        return only_class(training_set, classifier_idx)

    elif empty_input(input_attributes):
        return most_common_class(classifiers, training_set, classifier_idx)

    else:
        d = arg_max_inf_gain(input_attributes, training_set, classifiers, classifier_idx)
        d_values, subsets = binary_tests(d, training_set)
        # print(d)
        # print(d_values)
        input_attributes.remove(d)

        root = Node(d, d_values)
        sub_nodes = []

        for subset in subsets:  # dwa pozdbiory
            sub_nodes.append(id3(classifiers, input_attributes, subset, classifier_idx))

        root.children = sub_nodes
        return root


def predict_classifier(sample, decision_tree_root, dictionary, classifier_idx):
    node = decision_tree_root

    while True:
        attribute_idx = node.attribute

        if sample.attributes[attribute_idx] not in node.values:
            return majority_classifier(node, dictionary[classifier_idx])

        if node.values.index(sample.attributes[attribute_idx]) == PRIMARY_VALUE_IDX:
            child_idx = LEFT_CHILD
        else:
            child_idx = RIGHT_CHILD

        if node.children[child_idx] in dictionary[classifier_idx]:
            break

        node = node.children[child_idx]

    return node.children[child_idx]


def majority_classifier(node, classifiers):
    count_array = []
    for _ in classifiers:
        count_array.append(0)

    count_classifiers(node, classifiers, count_array)

    most_common_classifier = 0
    for value in count_array:
        if value > most_common_classifier:
            most_common_classifier = value

    return classifiers[most_common_classifier]


def count_classifiers(node, classifiers, count_array):
    if node in classifiers:
        count_array[classifiers.index(node)] += 1

    else:
        if len(node.children) == BOTH:
            count_classifiers(node.children[LEFT_CHILD], classifiers, count_array)
            count_classifiers(node.children[RIGHT_CHILD], classifiers, count_array)
        else:
            count_classifiers(node.children[LEFT_CHILD], classifiers, count_array)
