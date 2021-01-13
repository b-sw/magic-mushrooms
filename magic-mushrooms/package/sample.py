"""
    Name: sample.py
    Purpose: sample class definition

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""


def generate_input_attributes(dictionary, classifier_idx):
    input_attributes = []
    for i in range(len(dictionary)):
        if i is not classifier_idx:
            input_attributes.append(i)

    return input_attributes


class Sample:

    def __init__(self, attributes):
        self.attributes = attributes
