from unittest import TestCase

from project_euler.max_prime_factor import max_prime_factor


class TestMaxPrimeFactor(TestCase):

    def test0(self):
        self.assertEqual(5, max_prime_factor(10))

    def test1(self):
        self.assertEqual(17, max_prime_factor(17))

    def test2(self):
        self.assertEqual(29, max_prime_factor(13195))

    def test3(self):
        self.assertEqual(5, max_prime_factor(1e12))

    def test4(self):
        self.assertEqual(9901, max_prime_factor(999999999999))

    def test5(self):
        self.assertEqual(168406871, max_prime_factor(999999999998))

    def test6(self):
        self.assertEqual(168406871, max_prime_factor(999999999998))

    def test7(self):
        self.assertEqual(211371803, max_prime_factor(999999999993))
