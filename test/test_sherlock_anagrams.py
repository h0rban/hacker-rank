from unittest import TestCase

from interview_prep_kit.dictionaries_and_hashmaps.sherlock_anagrams import sherlock_anagrams

log = False


# noinspection SpellCheckingInspection
class Test(TestCase):

    def test1(self):
        self.assertEqual(2, sherlock_anagrams('mom', log=log))

    def test2(self):
        self.assertEqual(4, sherlock_anagrams('abba', log=log))

    def test3(self):
        self.assertEqual(0, sherlock_anagrams('abcd', log=log))

    def test4(self):
        self.assertEqual(3, sherlock_anagrams('ifailuhkqq', log=log))

    def test5(self):
        self.assertEqual(10, sherlock_anagrams('kkkk', log=log))

    def test6(self):
        self.assertEqual(5, sherlock_anagrams('cdcd', log=log))
