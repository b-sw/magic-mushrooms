"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import sys
from package.algorithm import *
from package.file import *

FILE_NAME_IDX = 0
ARGC = 1  # source set file name


def main():
    argv = sys.argv[1:]

    if len(argv) == ARGC:
        file_name = argv[FILE_NAME_IDX]
        collection = get_collection_from_file(file_name)

    else:
        collection = get_collection_from_file('agaricus-lepiota.data')

        # TESTOWANKO
        input_attributes = []
        classifiers = [EDIBLE, POISONOUS]
        for i in range(1, 22):
            input_attributes.append(i)
        print(input_attributes)

        root = id3(classifiers, input_attributes, collection)
        print('node\'y czytać od dołu do góry\n')
        print('Atrybut przyjmuje wartosci:\n{}'.format(root.values))

        # for i in range(len(collection)):
        #     if collection[i].attributes[16] == 'u':
        #         print(collection[i].attributes)


if __name__ == '__main__':
    main()
