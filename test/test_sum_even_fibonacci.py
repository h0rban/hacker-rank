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

    def version_helper(self, expected, *args, n_loops=10):
        results = []
        for func in [sum_even_fibonacci_v1, sum_even_fibonacci_v2, sum_even_fibonacci_v3]:
            if log:
                results.append(time_func(func, *args, n_loops=n_loops))
            self.assertEqual(func(*args), expected, func.__name__)

        if log:
            print(*args, pd.DataFrame(results), '', sep='\n')

    def test0(self):
        self.version_helper(10, 10)

    def test1(self):
        self.version_helper(44, 100)

    def test2(self):
        self.version_helper(798, 1000)

    def test3(self):
        self.version_helper(1089154, 1e6)

    def test4(self):
        self.version_helper(652484772464328, 1e15)

    def test5(self):
        self.version_helper(11708364174233842, 1e16)

    def test6(self):
        self.version_helper(49597426547377748, 4e16)
