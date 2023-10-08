"""
https://structy.net/problems/zipper-lists
  1 -> 2 -> 3 -> 4 -> 5 -> 77
ans,cur
       6 -> 7 -> 8 -> 9
receiving


1 -> 6 -> 
ans cur

    2 ->  
receiving


1 -> 6 -> 2 -> 
ans      cur

    7 ->  
receiving

"""
from typing import Optional
import unittest
from algoutils.list_node import ListNode


class Solution:
    def zipper_lists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans = l1
        while l1 and l2:
            l1.next, l2 = l2, l1.next
            l1 = l1.next
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        tree = ListNode(
            1,
            ListNode(2, ListNode(3)),
        )
        tree2 = ListNode(
            6,
            ListNode(
                7,
                ListNode(8, ListNode(9, ListNode(4, ListNode(5, ListNode(77))))),
            ),
        )
        print(t.zipper_lists(tree, tree2))
        tree = ListNode(
            1,
            ListNode(
                2,
                ListNode(
                    3,
                    ListNode(8, ListNode(9, ListNode(4, ListNode(5, ListNode(77))))),
                ),
            ),
        )
        tree2 = ListNode(
            6,
            ListNode(
                7,
            ),
        )
        print(t.zipper_lists(tree, tree2))


if __name__ == "__main__":
    unittest.main()
