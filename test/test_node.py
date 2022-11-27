from unittest import TestCase
from data_structures.trees.node import Node


def print_node(node, sep=' ' * 5):
    if node.left:
        left_len = len(str(node.left.info))
    if node.right:
        right_len = len(str(node.right.info))

    center_len = len(str(node.info))

    left_padding = " " * left_len

    edges = '/   \\'
    center_padding = ' ' * ((len(edges) - center_len + (1 if center_len % 2 == 0 else 0)) // 2)

    print(left_padding + center_padding + str(node.info))
    print(left_padding + edges)
    print(str(node.left.info) + sep + str(node.right.info))

    # todo remove
    print()


class TestNode(TestCase):

    def test0(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)

        print_node(node)

        node = Node(13)
        node.left = Node(2345)
        node.right = Node(321)

        print_node(node)

        node = Node(456)
        node.left = Node(12345)
        node.right = Node(123)

        print_node(node)

        node.info = 1234
        node.left = Node(1234567)

        print_node(node)

        node.info = 123456789
        node.left.info = 0

        print_node(node)
