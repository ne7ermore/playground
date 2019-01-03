class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


def build(arr):
    if len(arr) == 0:
        return None

    if len(arr) == 1:
        return Node(arr[0])

    mid = (len(arr))//2
    node = Node(arr[mid])
    node.left = build(arr[:mid])
    node.right = build(arr[mid+1:])

    return node


def closest_value(root, target):
    a = root.value
    kid = root.left if target < a else root.right
    if not kid:
        return a
    b = closest_value(kid, target)
    return min((a, b), key=lambda x: abs(target-x))


if __name__ == "__main__":
    arr = [1, 13, 17, 20, 24, 35, 46]
    node = build(arr)

    assert closest_value(node, 23) == 24
