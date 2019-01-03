class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


class BST:
    def __init__(self):
        self.root = None

    @property
    def get_root(self):
        return self.root

    def size(self):
        return self.recur_size(self.root)

    def recur_size(self, node):
        if not node:
            return 0

        return 1 + self.recur_size(node.left)+self.recur_size(node.right)

    def search(self, value):
        return self.recur_search(self.root, value)

    def recur_search(self, node, value):
        if node is None:
            return False

        if node.value == value:
            return True

        if node.value > value:
            return self.recur_search(node.left, value)

        return self.recur_search(node.right, value)

    def insert(self, value):
        if self.root:
            return self.recur_insert(self.root, value)

        self.root = Node(value)
        return True

    def recur_insert(self, node, value):
        if node.value == value:
            return False

        if node.value > value:
            if node.left is None:
                node.left = Node(value)
                return True
            return self.recur_insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
                return True
            return self.recur_insert(node.right, value)

    def delete(self, value):
        self.root = self.recur_del(self.root, value)

    def recur_del(self, node, value):
        if node is None:
            return None

        if node.value == value:
            if node.left:
                attach_node = node.left
                while attach_node.right:
                    attach_node = attach_node.right

                attach_node.right = node.right
                return node.left

            else:
                return node.right

        if node.value < value:
            node.rihgt = self.recur_del(node.right, value)
        else:
            node.left = self.recur_del(node.left, value)

        return node

    def depth_sum(self):
        if not self.root:
            return 0

        return self.recur_depth_sum(self.root, 1)

    def recur_depth_sum(self, node, n):
        if not node:
            return 0

        return n*node.value + self.recur_depth_sum(node.left, n+1)+self.recur_depth_sum(node.right, n+1)

    def height(self):
        return self.recur_height(self.root)

    def recur_height(self, node):
        if not node:
            return 0

        return 1 + max([self.recur_height(node.left), self.recur_height(node.right)])

    def kth_smallest(self, k):
        if not self.root:
            return None

        counts = []
        self.recur_kth_smallest(self.root, counts)

        return counts[k-1]

    def recur_kth_smallest(self, node, counts):
        if node:
            self.recur_kth_smallest(node.left, counts)
            counts.append(node.value)
            self.recur_kth_smallest(node.right, counts)

    def lowest_common_ancestor(self, a, b):
        node = self.root
        while node:
            if a > node.value < b:
                node = node.right
            elif a < node.value > b:
                node = node.left
            else:
                return node

    def num_empty(self):
        return self.recur_num_empty(self.root)

    def recur_num_empty(self, node):
        if not node:
            return 0

        if not node.left and not node.right:
            return 2

        if not node.left:
            return 1+self.recur_num_empty(node.right)

        if not node.right:
            return 1+self.recur_num_empty(node.left)

        return self.recur_num_empty(node.right) + self.recur_num_empty(node.left)

    def deepest_left(self):
        deeps = [0]
        self.recur_deepest_left(self.root, deeps, 1)
        return deeps[0]

    def recur_deepest_left(self, node, deeps, depth):
        if not node:
            return

        if depth > deeps[0]:
            deeps[0] = depth

        self.recur_deepest_left(node.left, deeps, depth+1)
        self.recur_deepest_left(node.right, deeps, depth+1)

    def reversed(self):
        self.recur_reversed(self.root)

    def recur_reversed(self, node):
        node.left, node.right = node.right, node.left
        if node.left:
            self.recur_reversed(node.left)

        if node.right:
            self.recur_reversed(node.right)

    def is_subtree(self, sub):
        def comp(a, b):
            if not a and not b:
                return True

            if a and b:
                return a.value == b.value and comp(a.left, b.left) and comp(a.right, b.right)

            return False

        nodes = [self.root]
        flag = False
        while nodes:
            node = nodes.pop(0)
            if node and node.value == sub.value:
                flag = comp(node, sub)
                break
            else:
                nodes.append(node.left)
                nodes.append(node.right)

        return flag

    def longest_consecutive(self):
        def dfs(node, val, kit, max_len):
            if not node:
                return

            if node.value == val:
                kit += 1

            else:
                kit = 1

            max_len[0] = max(kit, max_len[0])

            dfs(node.left, node.value-1, kit, max_len)
            dfs(node.right, node.value+1, kit, max_len)

        max_len = [0]
        dfs(self.root, self.root.value, 0, max_len)

        return max_len[0]

    def has_path_sum(self, summ):
        def path_sum(node, summ):
            if not node:
                return False

            if not node.left and not node.right and node.value == summ:
                return True

            summ -= node.value

            return path_sum(node.left, summ) or path_sum(node.right, summ)

        return path_sum(self.root, summ)


if __name__ == "__main__":
    # insert && search
    bst = BST()
    assert bst.insert(1)
    assert not bst.insert(1)
    assert bst.insert(3)
    assert bst.insert(2)
    assert bst.insert(4)
    assert bst.insert(7)
    assert bst.insert(5)
    assert bst.insert(9)
    assert bst.insert(10)
    assert bst.insert(12)
    assert bst.insert(14)
    assert bst.insert(19)

    assert bst.size() == 11

    assert bst.search(12)
    assert not bst.search(11)

    # delete node
    bst = BST()
    for v in [29, 8, 4, 3, 6, 18, 13, 28, 12]:
        bst.insert(v)

    bst.delete(8)
    assert bst.root.left.right.right.value == 18
    assert not bst.search(8)

    # depth sum && height && kth_smallest && num_empty
    bst = BST()
    for v in [9, 6, 12, 3, 8, 10, 15, 7, 18]:
        bst.insert(v)

    assert bst.depth_sum() == 253
    assert bst.height() == 4
    assert bst.num_empty() == 10

    bst.insert(2)
    bst.insert(1)

    assert bst.height() == 5
    assert bst.kth_smallest(3) == 3

    # lowest_common_ancestor
    bst = BST()
    for v in [6, 2, 8, 0, 4, 3, 5, 7, 9]:
        bst.insert(v)

    assert bst.lowest_common_ancestor(7, 3).value == 6

    bst = BST()
    for v in [9, 6, 12, 3, 8, 10, 15, 7, 18]:
        bst.insert(v)

    assert bst.deepest_left() == 4

    bst.insert(20)
    assert bst.deepest_left() == 5

    # is_subtree
    bst = BST()
    for v in [9, 6, 12, 3, 8, 10, 15, 7, 18]:
        bst.insert(v)

    bbst = BST()
    for v in [6, 3, 8, 7]:
        bbst.insert(v)

    assert bst.is_subtree(bbst.root)

    bbst = BST()
    for v in [6, 3, 8]:
        bbst.insert(v)

    assert not bst.is_subtree(bbst.root)

    #  longest_consecutive
    bst = BST()
    for v in [6, 3, 8, 7, 9, 2, 1, 4, 5]:
        bst.insert(v)

    assert bst.longest_consecutive() == 3

    bst.insert(0)
    assert bst.longest_consecutive() == 4

    bst.insert(10)
    bst.insert(11)
    bst.insert(12)
    assert bst.longest_consecutive() == 5

    # has_path_sum
    bst = BST()
    for v in [6, 2, 8, 0, 4, 3, 5, 7, 9]:
        bst.insert(v)

    assert bst.has_path_sum(15)
    assert bst.has_path_sum(21)
    assert not bst.has_path_sum(22)
