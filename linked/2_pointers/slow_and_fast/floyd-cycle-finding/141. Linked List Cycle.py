"""
https://leetcode.com/problems/linked-list-cycle/
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


"""
2 solutions work here. The easier one is having a set with pointers to node. Once a node is repeated we know that
we're in a cycle. This solution takes O(n) space. The other which takes less space is to have 2 pointers. One is
fast and the other is slow. If they met, it means we have a cycle. It's like having a race between a hare and a 
tortoise. If the race track is circular they will meet. Otherwise not. This algo is called 
Robert W. Floyd's tortoise and hare algorithm 
"""


class Solution:
    def hasCycle(self, slow: Optional[ListNode]) -> bool:
        # head is the slow pointer
        if not slow:
            return False
        fast = slow.next
        while fast and slow:
            if fast == slow:
                return True
            if not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
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
