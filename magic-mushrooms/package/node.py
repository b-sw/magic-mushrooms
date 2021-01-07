"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
LEFT_CHILD = 0
RIGHT_CHILD = 1


class Node:

    def __init__(self, attribute, values):
        self.attribute = attribute
        self.values = values
        self.children = []
