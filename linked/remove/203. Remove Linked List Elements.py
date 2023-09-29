"""
https://leetcode.com/problems/remove-linked-list-elements/

#remove
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # The first while loop is for when the first element/s are val
        while head and head.val == val:
            head = head.next
        p = head
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        tree = ListNode(
            1,
            ListNode(
                2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))
            ),
        )
        print(t.removeElements(tree, 6))
        tree = ListNode(
            7,
            ListNode(7, ListNode(7, ListNode(7))),
        )
        print(t.removeElements(tree, 7))
        print(t.removeElements(None, 1))
        tree = ListNode(
            1,
            ListNode(2, ListNode(2, ListNode(1))),
        )
        print(t.removeElements(tree, 2))


if __name__ == "__main__":
    unittest.main()
