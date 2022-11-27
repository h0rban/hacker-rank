from data_structures.trees.node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def __str__(self):
        lines, *_ = self.root.display_aux()
        return '\n'.join(map(str.rstrip, lines))


def make_bst(*vals):
    bst = BinarySearchTree()
    for val in vals:
        bst.insert(val)
    return bst
