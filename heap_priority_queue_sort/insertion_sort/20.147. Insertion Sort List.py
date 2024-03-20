"""
https://leetcode.com/problems/insertion-sort-list/
6.5.3.1.8.7.2.4
 
    6.5.3.1.8.7.2.4
d a b c                 

if c.val < a.next.val:
    insert c before a

"""

from typing import Optional
import unittest

from algoutils.list_node import ListNode, ll


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(None, head)
        b, c = head, head.next
        while c:
            a = d
            while a:
                if c.val < a.next.val:
                    # insert c directly after a
                    old_c_nxt = c.next
                    old_a_nxt = a.next
                    a.next = c
                    c.next = old_a_nxt
                    b.next = old_c_nxt
                    c = old_c_nxt
                    break
                elif a.next.val == b.val:
                    c, b = c.next, c
                    break
                a = a.next
        return d.next


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.insertionSortList(ll([6, 5, 3, 1, 8, 7, 2, 4])).arr(),
            [1, 2, 3, 4, 5, 6, 7, 8],
        )
        self.assertEqual(t.insertionSortList(ll([4, 2, 1, 3])).arr(), [1, 2, 3, 4])
        # self.assertEqual(t.insertionSortList(None), None)


if __name__ == "__main__":
    unittest.main()
