"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.sample import *

READ_FILE = 'r'
PATH = '../data/'
EMPTY_LIST = []


def read_dataset_from_file(file_name, separator):
    dataset = []
    dictionary = []
    file_name = PATH + file_name

    with open(file_name, READ_FILE, newline='\n') as file:
        for line in file:
            attributes = line.strip().split(separator)

            if not dictionary:  # jeśli pusty słownik
                for _ in attributes:
                    dictionary.append(EMPTY_LIST)

            for i in range(len(attributes)):
                if attributes[i] not in dictionary[i]:
                    dictionary[i].append(attributes[i])

            dataset.append(Sample(attributes))

    return dataset, dictionary
