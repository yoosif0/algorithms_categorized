"""
https://leetcode.com/problems/merge-two-sorted-lists/
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


"""
         1 ---> 2 -> 4
        l1

  1 -> 3 -> 4
l2
----------------------
         1 ---> 1 -> 3 -> 4
               l1

2 -> 4
l2
----------------------
         1 ---> 1 -> 2 -> 4
                    l1

3 -> 4
l2
----------------------
         1 ---> 1 -> 2 -> 3 -> 4
                          l1

4
l2
"""


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1 or not l2:
            return l2 or l1
        l1, l2 = (l2, l1) if l2.val < l1.val else (l1, l2)
        ans = l1
        while l1 and l1.next and l2:
            if l1.next and l2.val < l1.next.val:
                l1.next, l2 = l2, l1.next
            l1 = l1.next
        l1.next = l2
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        tree = ListNode(
            1,
            ListNode(
                2,
                ListNode(4),
            ),
        )
        tree2 = ListNode(
            1,
            ListNode(3, ListNode(4)),
        )
        print(t.mergeTwoLists(tree, tree2))
        print(t.mergeTwoLists(None, ListNode(0)))
        print(t.mergeTwoLists(ListNode(2), ListNode(1)))


if __name__ == "__main__":
    unittest.main()
