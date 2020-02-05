"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        host = ListNode(head.val-1)
        host.next = head

        now, prev = head.next, host
        while now:
            if prev.next.val != now.val:
                prev = prev.next
                now = now.next
            else:
                now = now.next
                while True:
                    if not now:
                        prev.next = now
                        break

                    if prev.next.val != now.val:
                        prev.next = now
                        now = now.next
                        break

                    now = now.next

        return host.next
