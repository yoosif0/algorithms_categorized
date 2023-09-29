"""
https://leetcode.com/problems/middle-of-the-linked-list/
fast and slow pointer. Whenever the fast pointer reaches the end, we return the slow pointer.
"""
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.val) + "\n"
        if self.next:
            ret += self.next.__repr__(level + 1)
        return ret


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


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
