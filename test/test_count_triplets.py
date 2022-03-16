from unittest import TestCase

from interview_prep_kit.dictionaries_and_hashmaps.count_triplets import count_triplets


class Test(TestCase):

    def test1(self):
        self.assertEqual(2, count_triplets([1, 2, 2, 4], 2))

    def test2(self):
        self.assertEqual(6, count_triplets([1, 3, 9, 9, 27, 81], 3))

    def test3(self):
        self.assertEqual(4, count_triplets([1, 5, 5, 25, 125], 5))

    def test4(self):
        self.assertEqual(3, count_triplets([1, 2, 1, 2, 4], 2))

    def test5(self):
        self.assertEqual(0, count_triplets([4, 2, 1], 2))

    def test6(self):
        self.assertEqual(1, count_triplets([1, 4, 2, 8, 4], 2))
