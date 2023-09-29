"""
https://leetcode.com/problems/palindrome-linked-list/

Reverse the second half.
#slow_fast_pointers
#reverse
#merge
"""

from collections import deque
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


# O(n) space
# class Solution:
#     def isPalindrome(self, h: Optional[ListNode]) -> bool:
#         q = deque([])
#         while h:
#             q.append(h.val)
#             h = h.next
#         while len(q) >= 2:
#             if q.pop() != q.popleft():
#                 return False
#         return True


# O(1) space
class Solution:
    def isPalindrome(self, h: Optional[ListNode]) -> bool:
        if not h or not h.next:
            return True
        # reverse second half of list
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

        # compare lists
        l1 = h
        l2 = p0
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1, l2 = l1.next, l2.next
        return True


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        tree = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        res = t.isPalindrome(tree)
        self.assertEqual(res, True)
        tree = ListNode(1, ListNode(2))
        res = t.isPalindrome(tree)
        self.assertEqual(res, False)
        tree = ListNode(1)
        res = t.isPalindrome(tree)
        self.assertEqual(res, True)
        tree = ListNode(1, ListNode(0, ListNode(1)))
        res = t.isPalindrome(tree)
        self.assertEqual(res, True)


if __name__ == "__main__":
    unittest.main()
