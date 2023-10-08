"""
https://leetcode.com/problems/reorder-list/
best explanation: https://leetcode.com/problems/reorder-list/solutions/801883/python-3-steps-to-success-explained/



1       2       3       4     5
h,              s                  f

1       2       3 ->None       4     5
h,              s,p0                       f

1       2       3 ->None    None   4     5
h,                           p0    s                                   


merge
1       5       4 
h,p1                                                                          
            
2        3
p0                                       

#slow_fast
#merge 
#switch_pointers
#2_lists
"""


from typing import Optional
import unittest
from algoutils.list_node import ListNode


class Solution:
    def reorderList(self, h: Optional[ListNode]) -> None:
        # reverse second half of list
        # reach mid point for s (you know that when fast ptr no longer can move forward)
        s = h
        f = h.next
        while f and f.next:
            f = f.next.next
            s = s.next

        # reverse the second list
        l2 = s.next
        p0 = None
        while l2:
            l2.next, p0, l2 = p0, l2, l2.next

        # merge lists
        l2 = p0
        l1 = h
        while l1:
            l2, l1.next = l1.next, l2
            l1 = l1.next
        return h


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        tree = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        print(t.reorderList(tree))
        tree = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        print(t.reorderList(tree))


if __name__ == "__main__":
    unittest.main()
