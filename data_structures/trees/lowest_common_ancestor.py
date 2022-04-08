def is_in_tree(node, val):
    if not node:
        return False
    if node.info < val:
        return is_in_tree(node.right, val)
    elif node.info > val:
        return is_in_tree(node.left, val)
    else:
        return True


def lca(node, v1, v2):
    """
    completed on 2022-04-08
    """
    if node.left and is_in_tree(node.left, v1) and is_in_tree(node.left, v2):
        return lca(node.left, v1, v2)

    if node.right and is_in_tree(node.right, v1) and is_in_tree(node.right, v2):
        return lca(node.right, v1, v2)
    return node
