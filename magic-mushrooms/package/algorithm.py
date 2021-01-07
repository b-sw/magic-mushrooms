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


def id3(classifiers, input_attributes, training_set):
    if is_deterministic(training_set):
        return only_class(training_set)

    elif empty_input(input_attributes):
        return most_common_class(classifiers, training_set)

    else:
        d = arg_max_inf_gain(input_attributes, training_set)
        d_values, subsets = subsets_by_values(d, training_set)
        input_attributes.remove(d)

        root = Node(d, d_values)
        sub_nodes = []

        for subset in subsets:
            sub_nodes.append(id3(classifiers, input_attributes, subset))

        # print(sub_nodes)
        root.children = sub_nodes
        return root


def predict_edibility(mushroom, decision_tree_root):
    node = decision_tree_root

    while True:
        attribute_idx = node.attribute

        if mushroom.attributes[attribute_idx] not in node.values:
            if majority_classifier(node) > 0:
                return EDIBLE
            else:
                return POISONOUS

        if node.values.index(mushroom.attributes[attribute_idx]) == PRIMARY_VALUE_IDX:
            child_idx = LEFT_CHILD
        else:
            child_idx = RIGHT_CHILD

        if node.children[child_idx] in [EDIBLE, POISONOUS]:
            break

        node = node.children[child_idx]

    return node.children[child_idx]


def majority_classifier(node):
    if node == EDIBLE:
        return 1
    elif node == POISONOUS:
        return -1
    else:
        if len(node.children) == BOTH:
            return majority_classifier(node.children[LEFT_CHILD]) + majority_classifier(node.children[RIGHT_CHILD])
        else:
            return majority_classifier(node.children[LEFT_CHILD])
