from unittest import TestCase

from data_structures.trees.tree_preorder_traversal import *

class TestPreOrderTraversal(TestCase):

    def setUp(self) -> None:
        self.tree = BinarySearchTree()
        for i in [1, 2, 5, 3, 6, 4]:
            self.tree.create(i)

    def test0(self):
        print(self.tree)
        self.tree.root.display()
