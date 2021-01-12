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


def id3(classifiers, input_attributes, training_set, classifier_idx, depth):
    if is_deterministic(training_set, classifier_idx):
        final_class = only_class(training_set, classifier_idx)
        # print(' : {} ({})'.format(final_class[0], final_class[1]), end='')
        return final_class[0]

    elif empty_input(input_attributes):
        final_class = most_common_class(classifiers, training_set, classifier_idx)
        # print(' : {}'.format(final_class), end='')
        return final_class

    else:
        d = arg_max_inf_gain(input_attributes, training_set, classifiers, classifier_idx)
        d_values, subsets = binary_tests(d, training_set)
        # draw_depth = ''
        # for _ in range(depth):
        #     draw_depth += '| '

        root = Node(d, d_values, depth)
        sub_nodes = []

        # print('\n{}{} = {}'.format(draw_depth, ATTRS[d], d_values[0]), end='')
        sub_nodes.append(id3(classifiers, input_attributes, subsets[LEFT_SUBSET], classifier_idx, depth + 1))
        # print('\n{}{} != {}'.format(draw_depth, ATTRS[d], d_values[0]), end='')
        sub_nodes.append(id3(classifiers, input_attributes, subsets[RIGHT_SUBSET], classifier_idx, depth + 1))

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
    for i in range(len(count_array)):
        if count_array[i] > most_common_classifier:
            most_common_classifier = i

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
