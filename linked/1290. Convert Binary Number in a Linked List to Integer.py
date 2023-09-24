"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
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
    def getDecimalValue(self, l1: Optional[ListNode]) -> int:
        arr = []
        while l1:
            arr.append(str(l1.val))
            l1 = l1.next
        s = "".join(arr)
        return int(s, 2)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        tree = ListNode(
            1,
            ListNode(
                0,
                ListNode(1),
            ),
        )
        self.assertEqual(t.getDecimalValue(tree), 5)


if __name__ == "__main__":
    unittest.main()
