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

ARGC = 6


def main():
    argv = sys.argv[1:]
    """
        0 - file name
        1 - classifier index
        2 - attribute separator
        3 - set split proportion
        4 - k for k-validation
        5 - number of runs
    """
    if len(argv) == ARGC:
        file_name = argv[0]
        classifier_idx = int(argv[1])
        separator = argv[2]
        set_split_proportion = float(argv[3])
        k = int(argv[4])
        runs = int(argv[5])
        predict_test_k_validate(file_name, classifier_idx, separator, k, runs)
    else:
        predict_test_k_validate('agaricus-lepiota.data', 0, ',', 4, 5)


if __name__ == '__main__':
    main()
