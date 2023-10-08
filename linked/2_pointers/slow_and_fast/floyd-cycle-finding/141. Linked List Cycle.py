"""
https://leetcode.com/problems/linked-list-cycle/
#dummy
"""
from typing import Optional
import unittest
from algoutils.list_node import ListNode

"""
2 solutions work here. The easier one is having a set with pointers to node. Once a node is repeated we know that
we're in a cycle. This solution takes O(n) space. The other which takes less space is to have 2 pointers. One is
fast and the other is slow. If they met, it means we have a cycle. It's like having a race between a hare and a 
tortoise. If the race track is circular they will meet. Otherwise not. This algo is called 
Robert W. Floyd's tortoise and hare algorithm 
"""


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = ListNode(0, head)
        f = head
        while f and s:
            if f == s:
                return True
            if not f.next:
                return False
            f = f.next.next
            s = s.next
        return False


# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         s = set()
#         cur = head
#         while cur:
#             if cur in s:
#                 return True
#             s.add(cur)
#             cur = cur.next
#         return False


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        third = ListNode(1)
        second = ListNode(5, third)
        first = ListNode(3, second)
        self.assertEqual(t.hasCycle(first), False)
        third.next = second
        self.assertEqual(t.hasCycle(first), True)


if __name__ == "__main__":
    unittest.main()
