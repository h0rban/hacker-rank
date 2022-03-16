from unittest import TestCase

from interview_prep_kit.dictionaries_and_hashmaps.frequency_queries import freq_query


class Test(TestCase):

    def test1(self):
        self.assertEqual([0, 1], freq_query([(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]))
