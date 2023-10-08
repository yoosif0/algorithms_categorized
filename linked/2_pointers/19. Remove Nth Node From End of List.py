"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#dummy
#slow_fast
#remove
#return_d.next
"""
from typing import Optional
import unittest
from algoutils.list_node import ListNode


"""
   1  2  3  4  5
d        l     r 
----------
   1   
dl r        
----------
   1  2  
dr   

"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0, head)
        r = d
        for _ in range(n):
            r = r.next
        l = d
        while r and r.next:
            r = r.next
            l = l.next
        l.next = l.next.next
        return d.next


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        print(
            t.removeNthFromEnd(
                ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2
            )
        )
        print(t.removeNthFromEnd(ListNode(1), 1))
        print(t.removeNthFromEnd(ListNode(1, ListNode(2)), 1))
        print(t.removeNthFromEnd(ListNode(1, ListNode(2)), 2))


if __name__ == "__main__":
    unittest.main()
