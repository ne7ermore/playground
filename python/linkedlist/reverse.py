class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None


def arr2linked(arr):
    res = cur = Node(arr[0])
    for a in arr[1:]:
        cur.next = Node(a)
        cur = cur.next

    return res


def link2arr(link):
    list = []
    while link:
        list.append(link.val)
        link = link.next

    return list


def reverse(head):
    prev = None
    while head:
        cur = head
        head = head.next
        cur.next = prev
        prev = cur

    return prev


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6]
    head = arr2linked(list)
    head = reverse(head)

    assert link2arr(head) == [6, 5, 4, 3, 2, 1]
