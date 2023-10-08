"""
https://leetcode.com/problems/middle-of-the-linked-list/
fast and slow pointer. Whenever the fast pointer reaches the end, we return the slow pointer.
"""
from typing import Optional
import unittest
from algoutils.list_node import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = s = head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        tree = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        res = t.middleNode(tree)
        self.assertEqual(res and res.val, 3)
        tree = ListNode(
            1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))
        )
        res = t.middleNode(tree)
        self.assertEqual(res and res.val, 4)


if __name__ == "__main__":
    unittest.main()
