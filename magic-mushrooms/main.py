"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import sys
from package.algorithm import *
from tests.predict_test import *

FILE_NAME_IDX = 0
ARGC = 1  # source set file name


def main():
    argv = sys.argv[1:]

    if len(argv) == ARGC:
        # todo: coś tam
        print('ok')
    else:
        # TESTOWANKO
        predict_test()


if __name__ == '__main__':
    main()
