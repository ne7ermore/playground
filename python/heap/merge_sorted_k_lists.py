from queue import PriorityQueue


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_k_lists(lists):
    dummy = ListNode(None)
    curr = dummy
    q = PriorityQueue()
    for node in lists:
        if node:
            q.put((node.val, node))
    while not q.empty():
        curr.next = q.get()[1]
        curr = curr.next
        if curr.next:
            q.put((curr.next.val, curr.next))
    return dummy.next


if __name__ == "__main__":
    a3 = ListNode(3)
    a2 = ListNode(2)
    a1 = ListNode(1)

    a1.next = a2
    a2.next = a3

    b3 = ListNode(13)
    b2 = ListNode(12)
    b1 = ListNode(11)

    b1.next = b2
    b2.next = b3
