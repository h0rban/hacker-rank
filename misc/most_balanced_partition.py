import numpy as np


def most_balanced_partition(parent_list, files_size):

    """
    Problem Solving (Basic)

    completed om 2022-03-11
    """

    parents, totals = {}, {}
    for i in range(len(parent_list)):
        parent, value = parent_list[i], files_size[i]
        parents[i], totals[i] = parent, value
        while parent != -1:
            totals[parent] += value
            parent = parents[parent]

    return (totals[0] - 2 * np.array(list(totals.values()))).__abs__().min()
