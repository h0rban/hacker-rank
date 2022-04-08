def pre_order_v1(node):
    """
    completed on 2022-04-07
    """
    if not node:
        return []
    return [node.info] + pre_order_v1(node.left) + pre_order_v1(node.right)


def pre_order_v2(node):
    accum = []

    while node:
        if not node.left:
            accum.append(node.info)
            node = node.right
        else:
            prev = node.left

            while prev.right and prev.right != node:
                prev = prev.right

            if prev.right:
                prev.right = None
                node = node.right
            else:
                prev.right = node
                accum.append(node.info)
                node = node.left

    return accum
