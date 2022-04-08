from unittest import TestCase
from data_structures.linked_lists.reverse_doubly_linked_list import *
from data_structures.linked_lists.doubly_linked_list import make_dll


class TestReverseDoublyLinkedList(TestCase):

    def setUp(self) -> None:
        self.dll = make_dll(1, 2, 3, 4)
        self.dll_rev = make_dll(4, 3, 2, 1)

    def test0(self):
        self.assertEqual(self.dll, self.dll)
        self.assertNotEqual(self.dll, self.dll_rev)

    def test1(self):
        self.assertEqual(self.dll.head, reverse_dll_inplace(self.dll_rev.head))
