"""
https://leetcode.com/problems/linked-list-cycle-ii/
    2  0  -4
      sf    
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


# # O(n) space
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         s = set()
#         while head:
#             if head in s:
#                 return head
#             s.add(head)
#             head = head.next
#         return None


# O(1) space
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # try to make 2 pointers meet
        if not head:
            return None
        s = head
        f = head
        while s and f and f.next and f != s:
            s = s.next
            f = f.next.next
        # if the 2 pointers can't meet, we know we don't have a cycle
        if not f or not s or f.val != s.val:
            return None
        # otherwise
        f = f.next
        cycle_length = 1
        while f and f.val != s.val:
            f = f.next
            cycle_length += 1
        print(cycle_length)

        # measure distance


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        node_4 = ListNode(-4)
        node0 = ListNode(0, node_4)
        node2 = ListNode(2, node0)
        node3 = ListNode(3, node2)
        # self.assertEqual(obj.detectCycle(node3), None)
        node_4.next = node2
        obj.detectCycle(node3)


if __name__ == "__main__":
    unittest.main()
