"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from enum import Enum

CLASSIFIER_IDX = 0
EDIBLE = 'e'
POISONOUS = 'p'
READ_FILE = 'r'


class Attributes(Enum):  # tak roboczo - mam przeczucie, że się przyda
    CAP_SHAPE = 1
    CAP_SURFACE = 2
    CAP_COLOR = 3
    BRUISES = 4
    ODOR = 5
    GILL_ATTACHMENT = 6
    GILL_SPACING = 7
    GILL_SIZE = 8
    GILL_COLOR = 9
    STALK_SHAPE = 10
    STALK_ROOT = 11
    STALK_SURFACE_ABOVE_RING = 12
    STALK_SURFACE_BELOW_RING = 13
    STALK_COLOR_ABOVE_RING = 14
    STALK_COLOR_BELOW_RING = 15
    VEIL_TYPE = 16
    VEIL_COLOR = 17
    RING_NUMBER = 18
    RING_TYPE = 19
    SPORE_PRINT_COLOR = 20
    POPULATION = 21
    HABITAT = 22


def get_collection_from_file(file_name):
    file = open(file_name, READ_FILE)
    pass


class Mushroom:
    def __init__(self, attributes):
        self.attributes = attributes
