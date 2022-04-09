import heapq
from data_structures.trees.binary_search_tree import Node


class MinHeap(object):
    def __init__(self, arr=None, not_found_value=-1):
        self.heap = []
        self.not_found_value = not_found_value
        if arr:
            self.heap = arr.copy()
            heapq.heapify(self.heap)

    def insert(self, val):
        heapq.heappush(self.heap, val)

    def get_heap(self):
        return self.heap.copy()

    def get_root(self):
        if self.heap:
            return self.heap[0]
        raise Exception("Heap is empty")

    def get_item_index(self, item):

        def find_starting_from(idx):
            if idx >= len(self):
                return self.not_found_value
            if self.heap[idx] == item:
                return idx

            left = find_starting_from(idx * 2 + 1)
            return left if left != self.not_found_value else find_starting_from(idx * 2 + 2)

        if not self or self.get_root() > item:
            return self.not_found_value

        return find_starting_from(0)

    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def delete(self, item):

        def sink(idx):
            to_swap = idx
            left, right = idx * 2 + 1, idx * 2 + 2

            if left < len(self) and self.heap[left] < self.heap[to_swap]:
                to_swap = left
            if right < len(self) and self.heap[right] < self.heap[to_swap]:
                to_swap = right
            if idx == to_swap:
                return
            self.swap(idx, to_swap)
            sink(to_swap)

        item_idx = self.get_item_index(item)
        if item_idx == self.not_found_value:
            raise Exception("Item not found")

        self.swap(item_idx, -1)
        self.heap.pop()

        sink(item_idx)

    def __len__(self):
        return len(self.heap)

    def __bool__(self):
        return len(self) > 0

    def __contains__(self, item):
        return self.get_item_index(item) != self.not_found_value

    def __str__(self):

        def make_tree(node, idx):

            left, right = idx * 2 + 1, idx * 2 + 2
            if left < len(self):
                node.left = Node(self.heap[left])
                make_tree(node.left, left)
            if right < len(self):
                node.right = Node(self.heap[right])
                make_tree(node.right, right)

        root = Node(self.heap[0])
        make_tree(root, 0)

        lines, *_ = root.display_aux()

        return str(self.heap) + "\n" + "\n".join(lines)
