"""
https://leetcode.com/problems/merge-two-sorted-lists/
#dummy
"""
from typing import Optional
import unittest
from algoutils.list_node import ListNode

"""

   4
   l    

 1 -> 1 -> 2-> 3 -> 4
               c   l2
"""


class Solution:
    def mergeTwoLists(
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
