"""
https://leetcode.com/problems/sort-list
"""

from typing import Optional
import unittest

from algoutils.list_node import ListNode, ll


class Solution:
    def merge(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        d = ListNode()
        c = d
        while l1 and l2:
            if l1.val <= l2.val:
                c.next = l1
                l1 = l1.next
            else:
                c.next = l2
                l2 = l2.next
            c = c.next
        # in case one of the lists still did not end yet
        c.next = l1 or l2
        return d.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        d, s, f = ListNode(0), head, head
        d.next = head
        while f and f.next:
            s, d, f = s.next, d.next, f.next.next
        d.next = None
        return self.merge(self.sortList(s), self.sortList(head))


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.sortList(ll([4, 2, 1, 3])).arr(), [1, 2, 3, 4])
        self.assertEqual(t.sortList(None), None)


if __name__ == "__main__":
    unittest.main()
