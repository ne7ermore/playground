/**
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
 * **/

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(0) {}
};

class Solution
{
  public:
    ListNode *reverseBetween(ListNode *head, int m, int n)
    {
        ListNode *res = new ListNode(0);
        res->next = head;
        ListNode *prev = res;
        ListNode *next = 0;

        for (int i = 1; i < m; i++)
            prev = prev->next;
        ListNode *cur = prev->next;
        for (int i = 0; i < n - m; i++)
        {
            next = cur->next;
            cur->next = next->next;
            next->next = prev->next;
            prev->next = next;
        }
        return res->next;
    }
};