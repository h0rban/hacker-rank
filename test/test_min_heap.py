import heapq
from unittest import TestCase
from data_structures.heaps.min_heap import MinHeap


class TestMinHeap(TestCase):

    def setUp(self):
        self.heap0 = MinHeap()
        self.heap1 = MinHeap([3, 4, 1, 7, 2, 0, 9, 5, 8, 6])

    def test0(self):
        for i in range(-10, 0):
            self.assertFalse(i in self.heap0)
            self.assertFalse(i in self.heap1)

        for i in range(10):
            self.assertFalse(i in self.heap0)
            self.assertTrue(i in self.heap1)

        for i in range(10, 20):
            self.assertFalse(i in self.heap1)

    def test1(self):
        for i, value in enumerate(self.heap1.get_heap()):
            self.assertEqual(i, self.heap1.get_item_index(value))

    def test2(self):
        for i in self.heap1.get_heap():
            self.setUp()
            # print(self.heap1)
            # print('deleting', i)
            self.heap1.delete(i)
            # print(self.heap1)
            # print('\n\n')
            result = self.heap1.get_heap()
            heapified = result.copy()
            heapq.heapify(heapified)
            self.assertEqual(result, heapified)
