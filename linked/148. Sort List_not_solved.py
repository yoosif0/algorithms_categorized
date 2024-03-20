"""
https://leetcode.com/problems/sort-list

2 1 3 4
    h i 

"""


import unittest
from typing import Optional
from algoutils.list_node import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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