"""
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

d   1 2 3 4
d     l     r

slow and fast pointer but this time the fast pointer started 2 steps further to allow to delete "slow.next" at the end
#remove
#dummy
#return_d.next

  [1,3,4,7,1,2,6]
d        l       r
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


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0, head)
        s = d
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        s.next = s.next.next
        return d.next


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        print(t.deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
        print(t.deleteMiddle(ListNode(2, ListNode(1))))


if __name__ == "__main__":
    unittest.main()
