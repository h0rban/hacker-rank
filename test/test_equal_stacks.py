import random
import numpy as np
import pandas as pd
from unittest import TestCase
from timer.timer import time_func
from data_structures.stacks.equal_stacks import equal_stacks, equal_stacks_v2

log = False


class TestEqualStacks(TestCase):

    def version_helper(self, expected, *args, n_loops=100000):
        results = []
        for func in [equal_stacks, equal_stacks_v2]:
            if log:
                results.append(time_func(func, *args, n_loops=n_loops))
            self.assertEqual(func(*args), expected, func.__name__)

        if log:
            print(f'args: {args}', pd.DataFrame(results), '', sep='\n')

    def test0(self):
        self.version_helper(2, [1, 2, 1, 1], [1, 1, 2], [1, 1])

    def test1(self):
        self.version_helper(5, [3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1])

    def test2(self):
        for i in range(10):
            arr = []
            for h in range(3):
                arr.append(list(np.random.choice(10, size=random.randint(100, 200))))
            answer = equal_stacks(*arr)
            if log:
                print(answer)
            self.version_helper(answer, *arr)


