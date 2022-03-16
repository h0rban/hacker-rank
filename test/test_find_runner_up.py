from unittest import TestCase

from misc.find_runner_up import find_runner_up, find_second


class Test(TestCase):

    def test0(self):
        self.assertEqual(1, find_runner_up([1, 2]))

    def test02(self):
        self.assertEqual(1, find_runner_up([2, 1]))

    def test1(self):
        self.assertEqual(5, find_runner_up([2, 3, 6, 6, 5]))

    def test2(self):
        self.assertEqual(0, find_runner_up([0, 0, 1]))

    def test3(self):
        self.assertEqual(0, find_runner_up([1, 1, 0]))

    def test4(self):
        self.assertEqual(-1, find_runner_up([1, 1, -1, 1]))

    def test5(self):
        self.assertEqual(5, find_runner_up([5, 3, 6, 6, 2]))

    def test6(self):
        self.assertEqual(2, find_second([2, 1], maximum=False))

    def test7(self):
        self.assertEqual(2, find_second([1, 2], maximum=False))

    def test8(self):
        self.assertEqual(1, find_second([1, 2]))

    def test9(self):
        self.assertEqual(1, find_second([2, 1]))

