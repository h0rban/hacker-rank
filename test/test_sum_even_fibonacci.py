import numpy as np
import pandas as pd
from timeit import Timer
from unittest import TestCase
from project_euler.sum_even_fibonacci import *

log = False
n_loops = 10
imports = """
from math import sqrt, floor, log
from decimal import Decimal, Context, setcontext, ROUND_HALF_UP
from project_euler.sum_even_fibonacci import sum_even_fibonacci_v1, sum_even_fibonacci_v2, sum_even_fibonacci_v3
"""


class TestSumEvenFibonacci(TestCase):

    def version_helper(self, limit, expected):

        if log:
            results = []
        for func in [sum_even_fibonacci_v1, sum_even_fibonacci_v2, sum_even_fibonacci_v3]:
            if log:
                arr = np.array(Timer(f'{func.__name__}({limit})', setup=imports).repeat(repeat=n_loops, number=1))
                results.append({'name': func.__name__, 'mean': arr.mean(), 'std': arr.std()})

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
