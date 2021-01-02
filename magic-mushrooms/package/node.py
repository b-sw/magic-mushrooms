"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""


class Node:

    def __init__(self, attribute, values):
        self.attribute = attribute
        self.values = values
        self.children = []
