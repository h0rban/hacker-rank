from unittest import TestCase

from interview_prep_kit.arrays.new_year_chaos import minimum_bribes


class Test(TestCase):

    def test1(self):
        self.assertEqual(1, minimum_bribes([1, 2, 3, 5, 4, 6, 7, 8]))

    def test2(self):
        self.assertEqual(-1, minimum_bribes([4, 1, 2, 3]))

    def test3(self):
        self.assertEqual(3, minimum_bribes([2, 1, 5, 3, 4]))

    def test4(self):
        self.assertEqual(-1, minimum_bribes([5, 1, 2, 3, 7, 8, 6, 4]))

    def test5(self):
        self.assertEqual(7, minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4]))
