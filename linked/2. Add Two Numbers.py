"""
https://leetcode.com/problems/add-two-numbers/
"""


import unittest
from typing import Optional
from algoutils.list_node import ListNode


def getAllVals(l: Optional[ListNode]):
    if l is None:
        return ""
    sFromList = str(l.val)
    return sFromList + getAllVals(l.next)


def strToListNode(s: str):
    if len(s) == 0:
        return None
    second_part = s[:-1]
    return ListNode(int(s[-1]), strToListNode(second_part))


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1 = int(getAllVals(l1)[::-1])
        num2 = int(getAllVals(l2)[::-1])
        return strToListNode(str(num1 + num2))


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        result = t.addTwoNumbers(
            ListNode(2, ListNode(4, ListNode(9))),
            ListNode(5, ListNode(6, ListNode(4, ListNode(9)))),
        )
        if result is not None:
            print(result.val)
            if result.next is not None:
                print(result.next.val)


if __name__ == "__main__":
    unittest.main()
