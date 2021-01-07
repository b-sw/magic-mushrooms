"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from tests.predict_test import *
from package.visuals import *


def main():
    plot_graph(TEST_PROPORTIONS, predict_test())


if __name__ == '__main__':
    main()
