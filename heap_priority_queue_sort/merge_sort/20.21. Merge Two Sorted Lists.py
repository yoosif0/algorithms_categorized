"""
https://leetcode.com/problems/merge-two-sorted-lists/
#dummy
"""

from typing import Optional
import unittest
from algoutils.list_node import ListNode, ll

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
        self.assertEqual(
            t.mergeTwoLists(ll([1, 2, 4]), ll([1, 3, 4])).arr(), [1, 1, 2, 3, 4, 4]
        )
        self.assertEqual(t.mergeTwoLists(ll([]), ll([0])).arr(), [0])
        self.assertEqual(t.mergeTwoLists(ll([2]), ll([1])).arr(), [1, 2])


if __name__ == "__main__":
    unittest.main()
