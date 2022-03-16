from unittest import TestCase

from misc.is_balanced import is_balanced


class Test(TestCase):

    def test1(self):
        self.assertTrue(is_balanced('{(([])[])[]}'))

    def test2(self):
        self.assertTrue(is_balanced('{(([])[])[]}[]'))

    def test4(self):
        self.assertTrue(is_balanced('{[()]}'))

    def test6(self):
        self.assertTrue(is_balanced('{{[[(())]]}}'))

    def test7(self):
        self.assertTrue(is_balanced('{{([])}}'))

    def test3(self):
        self.assertFalse(is_balanced('{(([])[])[]]}'))

    def test5(self):
        self.assertFalse(is_balanced('{[(])}'))

    def test8(self):
        self.assertFalse(is_balanced('{{)[](}}'))

    def test9(self):
        self.assertFalse(is_balanced(']['))

    def test10(self):
        self.assertFalse(is_balanced('()['))
