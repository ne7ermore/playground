def delete_min(node):
    if not node.left.node:
        return node.right.node

    node.left.node = delete_min(node.left.node)
    return node


def min_node(node):
    if not node.left.node:
        return node

    return min_node(node.left.node)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


class AvlTree:
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    def insert(self, value):
        n = TreeNode(value)
        if not self.node:
            self.node = n
            self.node.left = AvlTree()
            self.node.right = AvlTree()

        elif value < self.node.value:
            self.node.left.insert(value)

        elif value > self.node.value:
            self.node.right.insert(value)

        self.re_balance()

    def re_balance(self):
        self.update_heights(False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    # LR
                    self.node.left.rotate_left()
                    self.update_balances()
                    self.update_heights()

                # LL
                self.rotate_right()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    # RL
                    self.node.right.rotate_right()
                    self.update_heights()
                    self.update_balances()

                # RR
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def rotate_right(self):
        new_root = self.node.left.node
        new_sub_left = new_root.right.node
        old_root = self.node
        new_root.right.node = old_root
        old_root.left.node = new_sub_left
        self.node = new_root

    def rotate_left(self):
        new_root = self.node.right.node
        new_sub_right = new_root.left.node
        old_root = self.node
        new_root.left.node = old_root
        old_root.right.node = new_sub_right
        self.node = new_root

    def update_heights(self, recursive=True):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_heights()

                if self.node.right:
                    self.node.right.update_heights()

            self.height = 1+max(self.node.left.height, self.node.right.height)
        else:
            self.height = -1

    def update_balances(self, recursive=True):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()

                if self.node.right:
                    self.node.right.update_balances()

            self.balance = self.node.left.height-self.node.right.height
        else:
            self.balance = 0

    def delete_node(self, value):
        if not self.node:
            return

        if value > self.node.value:
            self.node.right.delete_node(value)
        elif value < self.node.value:
            self.node.left.delete_node(value)
        else:
            if not self.node.left.node:
                self.node = self.node.right.node
            elif not self.node.right.node:
                self.node = self.node.left.node
            else:
                new_node = min_node(self.node.right.node)
                new_node.right.node = delete_min(self.node.right.node)
                new_node.left = self.node.left
                self.node = new_node

        self.update_heights()
        self.update_balances()

    def in_order_traverse(self):
        result = []

        if not self.node:
            return result

        result.extend(self.node.left.in_order_traverse())
        result.append(self.node.value)
        result.extend(self.node.right.in_order_traverse())
        return result


if __name__ == "__main__":
    avl = AvlTree()

    for v in [1, 2, 3, 4, 5, 6, 7]:
        avl.insert(v)

    assert avl.node.value == 4

    assert avl.node.left.node.value == 2
    assert avl.node.right.node.value == 6

    assert avl.node.right.node.left.node.value == 5
    assert avl.node.right.node.right.node.value == 7
    assert avl.node.left.node.left.node.value == 1
    assert avl.node.left.node.right.node.value == 3
    assert avl.balance == 0

    avl.delete_node(3)
    assert avl.node.left.node.value == 2
    assert avl.node.left.node.right.node is None
    assert avl.height == 2
    assert avl.balance == 0

    avl.delete_node(2)
    assert avl.balance == -1

    avl.delete_node(6)
    assert avl.balance == -1
    assert avl.node.right.node.value == 7
    assert avl.node.right.node.left.node.value == 5
