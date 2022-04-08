from unittest import TestCase
from data_structures.trees.binary_search_tree import make_bst
from data_structures.trees.lowest_common_ancestor import lca, lca_v2

tree1 = r"""
  _4_
 /   \
 2    7
/ \ /
1 3 6
"""[1:-1]

tree2 = r"""
  _5__
 /    \
 3    _8
/ \ /
2 4 6
     \
     7
"""[1:-1]


class TestLowestCommonAncestor(TestCase):

    def version_helper(self, expected, *args):
        for func in [lca, lca_v2]:
            self.assertEqual(func(*args).info, expected, func.__name__)

    def setUp(self) -> None:
        self.tree1 = make_bst(4, 2, 3, 1, 7, 6)
        self.tree2 = make_bst(5, 3, 8, 2, 4, 6, 7)

    def lca_helper(self, expected, tree, v1, v2):
        self.version_helper(expected, tree.root, v1, v2)
        # self.assertEqual(expected, lca(tree.root, v1, v2).info)

    def test0(self):
        self.assertEqual(tree1, str(self.tree1))
        self.assertEqual(tree2, str(self.tree2))

    def test1(self):
        self.lca_helper(4, self.tree1, 1, 7)

    def test2(self):
        self.lca_helper(2, self.tree1, 1, 3)

    def test3(self):
        self.lca_helper(2, self.tree1, 1, 2)

    def test4(self):
        self.lca_helper(5, self.tree2, 7, 3)

    def test5(self):
        self.lca_helper(3, self.tree2, 2, 4)

    def test6(self):
        self.lca_helper(6, self.tree2, 6, 7)

    def test7(self):
        self.lca_helper(1, make_bst(1, 2), 1, 2)
