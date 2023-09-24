"""
https://leetcode.com/problems/reverse-linked-list/description/

In linked lists, usually you can't go to the end of the list then start do changes because when you
go to the end, you don't have access to the beginning values
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
      <-1     2  ->  3 -> 4 -> 5
p0     p1        

      <-1  <-  2  <-  3 <- 4 <- 5
                               p0   p1        


p1.next,p1,p0 = p0,p1.next,p1
"""


class Solution:
    def reverseList(self, p1: Optional[ListNode]) -> Optional[ListNode]:
        p0 = None
        while p1:
            p1.next, p1, p0 = p0, p1.next, p1
        return p0


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        tree = ListNode(
            1,
            ListNode(
                2,
                ListNode(3, ListNode(4, ListNode(5))),
            ),
        )
        print(t.reverseList(tree))


if __name__ == "__main__":
    unittest.main()
