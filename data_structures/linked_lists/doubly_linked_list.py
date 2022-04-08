class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

    def __str__(self):
        next = self.next.data if self.next else 'null'
        prev = self.prev.data if self.prev else 'null'
        return f'({prev} <- {self.data} -> {next})'

    def __eq__(self, other):
        if not isinstance(other, DoublyLinkedListNode):
            return False
        current = self
        while current and other:
            if current.data != other.data:
                return False
            current = current.next
            other = other.next
        return current == other


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node
        self.length += 1

    def __str__(self):
        out = f'DLL len {self.length}: ->'
        current = self.head

        while current:
            out += f'{current.data}'
            current = current.next
            out += '<->' if current else '<-'
        return out

    def __eq__(self, other):
        if not isinstance(other, DoublyLinkedList):
            return False
        return self.head == other.head


def make_dll(*nums):
    dll = DoublyLinkedList()
    for num in nums:
        dll.insert_node(num)
    return dll
