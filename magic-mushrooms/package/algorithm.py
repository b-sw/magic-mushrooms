"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.properties import *
from package.node import *

MUSHROOM_ATTR_OFFSET = -1


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

        for i in range(len(d_values)):
            sub_nodes.append(id3(classifiers, input_attributes, subsets[i]))

        # print('Atrybut nr {}'.format(d))
        # print(sub_nodes)
        # print('\n')

        root.children = sub_nodes
        return root


def predict_edibility(mushroom, decision_tree_root):
    node = decision_tree_root
    attribute_idx = node.attribute + MUSHROOM_ATTR_OFFSET
    child_idx = node.values.index(mushroom.attributes[attribute_idx])

    while node.children[child_idx] not in [EDIBLE, POISONOUS]:
        node = node.children[child_idx]
        attribute_idx = node.attribute + MUSHROOM_ATTR_OFFSET
        child_idx = node.values.index(mushroom.attributes[attribute_idx])

    return node.children[child_idx]
