"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""
from typing import Optional
import unittest
from algoutils.list_node import ListNode

"""
1----->1,2
cur
------
1----->2
cur
------
1-->1-->1
cur
------
1-->1
cur
------
"""


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            # do not move cur unless what in front of it is not equal to it
            else:
                cur = cur.next
        return head


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        tree = ListNode(
            1,
            ListNode(
                1,
                ListNode(2),
            ),
        )
        print(t.deleteDuplicates(tree))
        tree = ListNode(
            1,
            ListNode(
                1,
                ListNode(1),
            ),
        )
        print(t.deleteDuplicates(tree))


if __name__ == "__main__":
    unittest.main()
