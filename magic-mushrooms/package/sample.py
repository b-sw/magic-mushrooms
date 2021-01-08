"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""


def generate_input_attributes(dictionary):
    input_attributes = []
    for i in range(len(dictionary)):
        input_attributes.append(i)

    return input_attributes


class Sample:

    def __init__(self, attributes):
        self.attributes = attributes
