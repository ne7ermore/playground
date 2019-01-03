from bst import BST


def count_left_node(node):
    if node is None:
        return 0

    if node.left is None:
        return count_left_node(node.right)

    return 1+count_left_node(node.left)+count_left_node(node.right)


if __name__ == "__main__":
    bst = BST()
    for v in [9, 6, 12, 3, 8, 10, 15, 7, 18]:
        bst.insert(v)

    assert count_left_node(bst.root) == 4
