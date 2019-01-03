class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


def array_to_bst(arr):
    if len(arr) == 0:
        return None

    if len(arr) == 1:
        return Node(arr[0])

    mid = (len(arr))//2
    node = Node(arr[mid])
    node.left = array_to_bst(arr[:mid])
    node.right = array_to_bst(arr[mid+1:])

    return node


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    node = array_to_bst(arr)
