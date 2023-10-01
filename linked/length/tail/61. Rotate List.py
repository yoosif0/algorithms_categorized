"""
https://leetcode.com/problems/rotate-list/
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
[1,2,3,4,5], k = 2
 l     m r

5,1,2,3,4
r l     m

5,1,2,3,4
l m     r

r.next,m.next = l,None
r,l = m,r

pick a place to break bonds

"""


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Find length of chain and determine breaking point to form 2 lists
        r = ListNode(0, head)
        len = 0
        while r and r.next:
            r = r.next
            len += 1
        # connect tail to head
        r.next = head
        # find breaking point
        if len == 0:
            return head
        k = k % len
        break_point = len - k
        # Go to the breaking point
        p = ListNode(0, head)
        pos = 0
        while pos != break_point:
            p = p.next
            pos += 1
        # break where required
        p.next, ans = None, p.next
        return ans


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
        print(t.rotateRight(tree, 2))
        tree = ListNode(1)
        print(t.rotateRight(tree, 0))
        tree = ListNode(1, ListNode(2))
        print(t.rotateRight(tree, 0))
        tree = None
        print(t.rotateRight(tree, 0))


if __name__ == "__main__":
    unittest.main()
