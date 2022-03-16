from unittest import TestCase

from misc.most_balanced_partition import most_balanced_partition


class Test(TestCase):
    def test1(self):
        self.assertEqual(2, most_balanced_partition([-1, 0, 1, 2], [-1, 0, 1, 2]))

    def test2(self):
        self.assertEqual(0, most_balanced_partition([-1, 0, 0, 1, 1, 2], [1, 2, 2, 1, 1, 1]))

    def test3(self):
        self.assertEqual(19, most_balanced_partition([-1, 0, 0, 0], [10, 11, 10, 10]))
