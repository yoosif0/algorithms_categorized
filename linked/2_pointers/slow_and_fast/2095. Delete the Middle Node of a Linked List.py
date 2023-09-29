"""
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

1,3,4,7,1,2,6
s   f

slow and fast pointer but this time the fast pointer started 2 steps further to allow to delete "slow.next" at the end
#remove
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
        if not head or not head.next:
            return None
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        tree = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        res = t.deleteMiddle(tree)
        print(res)
        tree = ListNode(2, ListNode(1))
        res = t.deleteMiddle(tree)
        print(res)


if __name__ == "__main__":
    unittest.main()
