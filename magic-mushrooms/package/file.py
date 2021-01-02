"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.mushroom import *
from csv import *

READ_FILE = 'r'
SEPARATOR = ','
PATH = '../data/'


def get_collection_from_file(file_name):
    collection = []
    file_name = PATH + file_name

    with open(file_name, READ_FILE, newline='\n') as file:
        for line in file:
            attributes = line.strip().split(SEPARATOR)
            # print(attributes)
            collection.append(Mushroom(attributes))

    return collection
