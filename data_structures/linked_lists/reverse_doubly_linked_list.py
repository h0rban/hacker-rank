def reverse_dll_inplace(current):
    """
    completed on 2022-04-07
    """
    prev = None
    while current:
        prev = current
        current.prev, current.next = current.next, current.prev
        current = current.prev

    return prev
