"""
https://leetcode.com/problems/swap-nodes-in-pairs/
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
   1  2  3  4
l  m  r

   2  1  3  4
l  r  m
==================
   2  1  3 
l  r  m


"""


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        m = head
        r = head.next
        l = ListNode(0, m)
        # the head will always be the second element if 2 or more elements exists
        head = head.next
        while True:
            m.next, r.next = r.next, m
            l.next = r
            if m and m.next and m.next.next:
                l = l.next.next
                m = m.next
                r = r.next.next.next
            else:
                break
        return head


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        # tree = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        # print(t.swapPairs(tree))
        tree = ListNode(1, ListNode(2, ListNode(3)))
        print(t.swapPairs(tree))


if __name__ == "__main__":
    unittest.main()
