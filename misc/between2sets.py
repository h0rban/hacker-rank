from unittest import TestCase
from functools import reduce


def getTotalX(a: list, b: list) -> int:
    return len(ints_between_sets(set(a), set(b)))


def factors(n):
    # https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def ints_between_sets(a: set, b: set) -> set:
    """
    There will be two arrays of integers. Determine all integers that satisfy the
    following two conditions:
        1. The elements of the first array are all factors of the integer being considered
        2. The integer being considered is a factor of all elements of the second array
    :param a: list of integers
    :param b: list of integers
    :return: set of integers that are between sets
    """

    # find intersection of all factors of all elements in b
    b_factors = None
    for n in b:
        factors_of_n = factors(n)
        if b_factors is None:
            b_factors = factors_of_n
        else:
            b_factors &= factors_of_n

    # add factor from b_factors if all elements in a are factors of it
    return {n for n in b_factors if all(n % a_i == 0 for a_i in a)}


class TestBetween2Sets(TestCase):
    def test_between2sets(self):
        self.assertEqual(ints_between_sets({2, 6}, {24, 36}), {6, 12})
        self.assertEqual(ints_between_sets({2, 4}, {16, 32, 96}), {4, 8, 16})
