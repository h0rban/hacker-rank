from unittest import TestCase

from misc.is_leap_year import is_leap_year


class Test(TestCase):

    def test(self):
        self.assertFalse(is_leap_year(1990))

    def test1(self):
        self.assertTrue(is_leap_year(2000))

    def test2(self):
        self.assertTrue(is_leap_year(2400))

    def test3(self):
        self.assertFalse(is_leap_year(1800))

    def test4(self):
        self.assertFalse(is_leap_year(1900))

    def test5(self):
        self.assertFalse(is_leap_year(2100))

    def test6(self):
        self.assertFalse(is_leap_year(2200))

    def test7(self):
        self.assertFalse(is_leap_year(2300))

    def test8(self):
        self.assertFalse(is_leap_year(2500))

    def test9(self):
        self.assertTrue(is_leap_year(1992))
