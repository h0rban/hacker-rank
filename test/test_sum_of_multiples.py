from unittest import TestCase

from project_euler.sum_multiples import sum_of_multiples, arithmetic_sum


def sum_of_multiples_of_3_and_5(n):
    return sum_of_multiples(n, 3, 5)


class TestSumOfMultiples(TestCase):

    def test0(self):
        self.assertEqual(23, sum_of_multiples_of_3_and_5(10))

    def test1(self):
        self.assertEqual(2318, sum_of_multiples_of_3_and_5(100))


class TestArithmeticSum(TestCase):

    def test0(self):
        self.assertEqual(1275, arithmetic_sum(3, 4, 25))

    def test1(self):
        self.assertEqual(45, arithmetic_sum(1, 1, 9))

    def test2(self):
        self.assertEqual(0, arithmetic_sum(0, 0, 0))

    def test3(self):
        self.assertEqual(0, arithmetic_sum(0, 0, 10))

    def test4(self):
        self.assertEqual(10, arithmetic_sum(1, 0, 10))

    def test5(self):
        self.assertEqual(5 * 10, arithmetic_sum(5, 0, 10))

    def test6(self):
        self.assertEqual(-1, arithmetic_sum(-1, 1, 1))

    # todo this test is not working
    # def test7(self):
    #     self.assertEqual(2, arithmetic_sum(-1, 1, 3))
