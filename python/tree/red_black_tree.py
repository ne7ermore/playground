class RBNode:
    def __init__(self, value, is_red,  parent=None, left=None, right=None):
        self.value = value
        self.color = is_red  # 1-red 0-black
        self.parent = parent
        self.left = left
        self.right = right


class RBTree:
    def __init__(self):
        self.root = None

    def left_rotate(self, node):
        new_root = node.right
        if new_root is None:
            return

        node.right = new_root.left
        if new_root.left is not None:
            new_root.left.parent = node

        if node.parent is None:
            self.root = new_root
        elif node is node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root

        new_root.left = node
        node.parent = new_root

    def right_rotate(self, node):
        new_root = node.left
        if new_root is None:
            return

        node.left = new_root.right
        if new_root.right is not None:
            new_root.right.parent = node

        if node.parent is None:
            self.root = new_root
        elif node is node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root

        new_root.right = node
        node.parent = new_root

    def insert(self, node):
        insert_node_parent = None
        root = self.root

        while root is not None:
            insert_node_parent = root
            if insert_node_parent.value < node.value:
                root = root.right
            else:
                root = root.left

        node.parent = insert_node_parent
        if insert_node_parent is None:
            self.root = node
        elif insert_node_parent.value > node.value:
            insert_node_parent.left = node
        else:
            insert_node_parent.right = node

        node.left = None
        node.right = None
        node.color = 1
        self.fix_insert(node)

    def fix_insert(self, node):
        if node.parent is None:
            node.color = 0
            self.root = node
            return

        while node.parent and node.parent.color is 1:
            if node.parent is node.parent.parent.left:
                uncle_node = node.parent.parent.right
                if uncle_node and uncle_node.color is 1:
                    node.parent.color = 0
                    uncle_node.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                    continue

                elif node is node.parent.right:
                    node = node.parent
                    self.left_rotate(node)

                node.parent.color = 0
                node.parent.parent.color = 1
                self.right_rotate(node.parent.parent)

            else:
                uncle_node = node.parent.parent.right
                if uncle_node and uncle_node.color is 1:
                    node.parent.color = 0
                    uncle_node.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                    continue

                elif node is node.parent.left:
                    node = node.parent
                    self.right_rotate(node)

                node.parent.color = 0
                node.parent.parent.color = 1
                self.left_rotate(node.parent.parent)

        self.root.color = 0

    def minimum(self, node):
        temp_node = node
        while temp_node.left:
            temp_node = temp_node.left
        return temp_node

    def maximum(self, node):
        temp_node = node
        while temp_node.right:
            temp_node = temp_node.right
        return temp_node

    def transplant(self, node_o, node_n):
        if node_o is None:
            self.root = node_n

        elif node_o is node_o.parent.left:
            node_o.parent.left = node_n

        elif node_o is node_o.parent.right:
            node_o.parent.right = node_n

        if node_n:
            node_n.parent = node_o.parent

    def delete(self, node):
        node_color = node.color
        if node.left is None:
            temp_node = node.right
            self.transplant(node, node.right)
        elif node.right is None:
            temp_node = node.left
            self.transplant(node, node.left)
        else:
            node_min = self.minimum(node.right)
            node_color = node_min.color
            temp_node = node_min.right

            if node_min.parent != node:
                self.transplant(node_min, node_min.right)
                node_min.right = node.right
                node_min.right.parent = node_min
            self.transplant(node, node_min)
            node_min.left = node.left
            node_min.left.parent = node_min
            node_min.color = node.color

        if node_color == 0:
            self.delete_fixup(temp_node)

    def delete_fixup(self, node):
        while node != self.root and node.color == 0:
            if node == node.parent.left:
                # node is left node
                node_brother = node.parent.right

                # case 1: node's red, can not get black node
                # set brother is black and parent is red
                if node_brother.color == 1:
                    node_brother.color = 0
                    node.parent.color = 1
                    self.left_rotate(node.parent)
                    node_brother = node.parent.right

                # case 2: brother node is black, and its children node is both black
                if (node_brother.left is None or node_brother.left.color == 0) and (
                        node_brother.right is None or node_brother.right.color == 0):
                    node_brother.color = 1
                    node = node.parent
                else:

                    # case 3: brother node is black , and its left child node is red and right is black
                    if node_brother.right is None or node_brother.right.color == 0:
                        node_brother.color = 1
                        node_brother.left.color = 0
                        self.right_rotate(node_brother)
                        node_brother = node.parent.right

                    # case 4: brother node is black, and right is red, and left is any color
                    node_brother.color = node.parent.color
                    node.parent.color = 0
                    node_brother.right.color = 0
                    self.left_rotate(node.parent)
                node = self.root
                break
            else:
                node_brother = node.parent.left
                if node_brother.color == 1:
                    node_brother.color = 0
                    node.parent.color = 1
                    self.left_rotate(node.parent)
                    node_brother = node.parent.right
                if (node_brother.left is None or node_brother.left.color == 0) and (
                        node_brother.right is None or node_brother.right.color == 0):
                    node_brother.color = 1
                    node = node.parent
                else:
                    if node_brother.left is None or node_brother.left.color == 0:
                        node_brother.color = 1
                        node_brother.right.color = 0
                        self.left_rotate(node_brother)
                        node_brother = node.parent.left
                    node_brother.color = node.parent.color
                    node.parent.color = 0
                    node_brother.left.color = 0
                    self.right_rotate(node.parent)
                node = self.root
                break
        node.color = 0

    def inorder(self):
        res = []
        if not self.root:
            return res
        stack = []
        root = self.root
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append({'val': root.value, 'color': root.color})
            root = root.right
        return res


if __name__ == "__main__":
    rb = RBTree()
    children = [11, 2, 14, 1, 7, 15, 5, 8, 4]
    for child in children:
        node = RBNode(child, 1)
        print(child)
        rb.insert(node)
    print(rb.inorder())
