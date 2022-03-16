from unittest import TestCase

from misc.largest_rectangle import largest_rectangle, largest_rectangle_v1, largest_rectangle_v2


class Test(TestCase):

    def version_helper_test(self, expected, input_list):
        for func in [largest_rectangle, largest_rectangle_v1, largest_rectangle_v2]:
            self.assertEqual(expected, func(input_list))

    def test1(self):
        self.version_helper_test(9, [5, 4, 3, 2, 1])

    def test2(self):
        self.version_helper_test(18, [1, 3, 5, 9, 11])

    def test3(self):
        self.version_helper_test(50, [11, 11, 10, 10, 10])

    def test4(self):
        self.version_helper_test(28338, [10, 6320, 6020, 6098, 1332, 7263, 672, 9472, 28338, 3401, 9494])

    def test5(self):
        self.version_helper_test(10, [3, 2, 5, 6, 1, 4, 4])

    def test6(self):
        self.version_helper_test(5, [2, 1, 2, 3, 1])

    def test7(self):
        self.version_helper_test(9, [1, 2, 3, 4, 5])
