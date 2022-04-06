from unittest import TestCase

from misc.merge_the_tools import merge_the_tools


class Test(TestCase):

    # noinspection SpellCheckingInspection
    def test1(self):

        self.assertEqual(['AB', 'CA', 'AD'], merge_the_tools('AABCAAADA', 3))


