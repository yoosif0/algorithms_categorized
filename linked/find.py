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
    def find_iteratve(self, l1: Optional[ListNode], target: int) -> bool:
        while l1:
            if l1.val == target:
                return True
            l1 = l1.next
        return False

    def find_recurs(self, head: Optional[ListNode], target: int) -> bool:
        def recurs(node: Optional[ListNode]):
            if not node:
                return False
            if node.val == target:
                return True
            return recurs(node.next)

        return recurs(head)


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
        self.assertEqual(t.find_iteratve(tree, 4), True)
        self.assertEqual(t.find_iteratve(tree, 7), False)
        self.assertEqual(t.find_recurs(tree, 4), True)
        self.assertEqual(t.find_recurs(tree, 7), False)


if __name__ == "__main__":
    unittest.main()
