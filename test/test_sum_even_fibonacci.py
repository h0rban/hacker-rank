import pandas as pd
from unittest import TestCase
from project_euler.sum_even_fibonacci import *
from timer.timer import time_func

log = True
n_loops = 10
imports = """
from math import sqrt, floor, log
from decimal import Decimal, Context, setcontext
from project_euler.sum_even_fibonacci import sum_even_fibonacci_v1, sum_even_fibonacci_v2, sum_even_fibonacci_v3
"""


class TestSumEvenFibonacci(TestCase):

    def version_helper(self, limit, expected):

        results = []

        for func in [sum_even_fibonacci_v1, sum_even_fibonacci_v2, sum_even_fibonacci_v3]:
            if log:
                results.append(time_func(func, limit, n_loops=10))
            self.assertEqual(func(limit), expected, func.__name__)

        if log:
            print(limit, pd.DataFrame(results), '', sep='\n')

    def test0(self):
        self.version_helper(10, 10)

    def test1(self):
        self.version_helper(100, 44)

    def test2(self):
        self.version_helper(1000, 798)

    def test3(self):
        self.version_helper(1e6, 1089154)

    def test4(self):
        self.version_helper(1e15, 652484772464328)

    def test5(self):
        self.version_helper(1e16, 11708364174233842)

    def test6(self):
        self.version_helper(4e16, 49597426547377748)
