"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import matplotlib
import matplotlib.pyplot as plt

COLOR = 'maroon'
WIDTH = 0.1


def plot_graph(proportions, accuracies):
    fig, ax = plt.subplots()

    ax.set_title('Accuracies')
    ax.set_xlabel('Proportion')
    ax.set_ylabel('Accuracy[%]')

    for i in range(len(proportions)):
        proportions[i] = str(proportions[i])

    ax.bar(proportions, accuracies, color=COLOR, width=WIDTH)
    plt.show()
