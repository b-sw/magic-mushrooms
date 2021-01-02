"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import sys
from package.inf_gain import *

FILE_NAME_IDX = 0
ARGC = 1  # source set file name


def main():
    argv = sys.argv[1:]

    if len(argv) == ARGC:
        file_name = argv[FILE_NAME_IDX]
        print('ok1')
    else:
        print('ok2')


if __name__ == '__main__':
    main()
