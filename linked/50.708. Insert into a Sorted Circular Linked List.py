"""
https://leetcode.ca/2017-11-07-708-Insert-into-a-Sorted-Circular-Linked-List/
"""

from typing import Optional
import unittest

from algoutils.list_node import ListNode, circ_ll


class Solution:
    def insertionSortList(
        self, head: Optional[ListNode], insertVal: int
    ) -> Optional[ListNode]:
        if head is None:
            return ListNode(insertVal)
        # insert when the val is between a and b
        # if val is less than min or more than max, then insert after max (when b is less than a).
        a = head
        b = head.next
        while not (a.val <= insertVal and b.val >= insertVal) and not (
            a.val > b.val and (insertVal >= a.val or insertVal <= b.val)
        ):
            a, b = b, b.next
        a.next = ListNode(insertVal, b)
        return head


class Test(unittest.TestCase):

    # insert val is between 2 of the vals in array
    def test(self):
        t = Solution()
        l = t.insertionSortList(circ_ll([3, 4, 1]), 2)
        self.assertEqual(l.val, 3)
        self.assertEqual(l.next.val, 4)
        self.assertEqual(l.next.next.val, 1)
        self.assertEqual(l.next.next.next.val, 2)
        self.assertEqual(l.next.next.next.next.val, 3)

    # insert val is larger than all values: should be inserted after max value
    def test(self):
        t = Solution()
        l = t.insertionSortList(circ_ll([3, 4, 1]), 5)
        self.assertEqual(l.next.next.next.val, 5)

    # insert val is less than all values: should be inserted after max value
    def test(self):
        t = Solution()
        l = t.insertionSortList(circ_ll([3, 4, 1]), 0)
        self.assertEqual(l.next.next.val, 0)

    # insert val is the same as one of the items in arr
    def test(self):
        t = Solution()
        l = t.insertionSortList(circ_ll([3, 4, 1]), 3)
        self.assertEqual(l.next.val, 3)

        # self.assertEqual(t.insertionSortList(None), None)


if __name__ == "__main__":
    unittest.main()
