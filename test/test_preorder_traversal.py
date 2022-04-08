import numpy as np
import pandas as pd
from unittest import TestCase
from timer.timer import time_func
from data_structures.trees.tree_preorder_traversal import *
from data_structures.trees.binary_search_tree import BinarySearchTree, make_bst

log = False
tree_str = r'''
1
 \
 2__
    \
   _5
  /  \
  3  6
   \
   4
'''[1:-1]  # removes first and last \n
rand_preorder = [521, 411, 136, 76, 59, 23, 10, 30, 54, 39, 70, 66, 63, 67, 101, 96, 88, 107, 280, 174, 139, 210, 198,
                 209, 235, 221, 218, 277, 261, 275, 319, 312, 299, 296, 292, 289, 307, 318, 371, 346, 328, 327, 370,
                 382, 513, 499, 439, 436, 493, 451, 737, 660, 626, 549, 527, 522, 542, 543, 548, 621, 584, 570, 578,
                 601, 590, 589, 617, 604, 636, 652, 678, 662, 687, 679, 692, 714, 740, 859, 811, 761, 741, 753, 787,
                 764, 837, 820, 826, 973, 938, 899, 883, 879, 866, 902, 901, 924, 947, 986, 974, 998]


class TestPreOrderTraversal(TestCase):

    def version_helper(self, expected, *args, n_loops=100000):
        results = []
        for func in [pre_order_v1, pre_order_v2]:
            if log:
                results.append(time_func(func, *args, n_loops=n_loops))
            self.assertEqual(func(*args), expected, func.__name__)

        if log:
            print(f'args: {args}', pd.DataFrame(results), '', sep='\n')

    def setUp(self) -> None:
        self.tree = make_bst(1, 2, 5, 3, 6, 4)
        self.random_tree = make_bst(*np.random.RandomState(42).choice(1000, size=100, replace=False))

    def test0(self):
        self.assertEqual(self.tree.__str__(), tree_str)

    def test1(self):
        self.version_helper([1, 2, 5, 3, 4, 6], self.tree.root)

    def test2(self):
        self.version_helper(rand_preorder, self.random_tree.root)
