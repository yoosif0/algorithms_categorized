"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
  1   2
      p
slow and fast pointer but this time the fast pointer started 2 steps further to allow to delete 
"slow.next" at the end



1   2
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ahead = head
        for _ in range(n):
            ahead = ahead.next
        # this happens when the node to be deleted is the head. we can't use p.next = p.next.next in this case
        if not ahead:
            return head.next
        late = head
        while ahead.next:
            ahead = ahead.next
            late = late.next
        late.next = late.next.next
        return head


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        tree = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        res = t.removeNthFromEnd(tree, 2)
        print(res)
        tree = ListNode(1)
        res = t.removeNthFromEnd(tree, 1)
        print(res)
        tree = ListNode(1, ListNode(2))
        res = t.removeNthFromEnd(tree, 1)
        print(res)
        tree = ListNode(1, ListNode(2))
        res = t.removeNthFromEnd(tree, 2)
        print(res)


if __name__ == "__main__":
    unittest.main()
