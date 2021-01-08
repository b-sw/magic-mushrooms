"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import sys
from tests.predict_test import *
from package.visuals import *

ARGC = 4


def main():
    argv = sys.argv[1:]
    """
        0 - file name
        1 - classifier index
        2 - attribute separator
        3 - set split proportion
    """
    if len(argv) == ARGC:
        file_name = argv[0]
        classifier_idx = int(argv[1])
        separator = argv[2]
        set_split_proportion = float(argv[3])
        predict_test(file_name, classifier_idx, separator, set_split_proportion)
    else:
        print('wrong arguments')


if __name__ == '__main__':
    main()
