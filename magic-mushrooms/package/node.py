"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
LEFT_CHILD = 0
RIGHT_CHILD = 1
ATTRS = ['edible', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment',
         'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
         'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type',
         'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat']


class Node:

    def __init__(self, attribute, values, depth):
        self.attribute = attribute
        self.values = values
        self.children = []
        self.depth = depth
