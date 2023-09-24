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
    def n_value_iterative(self, l1: Optional[ListNode], index: int) -> int:
        for _ in range(index):
            if not l1:
                break
            l1 = l1.next
        return l1.val if l1 else -1

    def n_value_recurs(self, head: Optional[ListNode], index: int) -> int:
        i = 0

        def recurs(node: Optional[ListNode]):
            nonlocal i
            if not node:
                return -1
            if i == index:
                return node.val
            i += 1
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
        self.assertEqual(t.n_value_iterative(tree, 4), 5)
        self.assertEqual(t.n_value_iterative(tree, 7), -1)
        self.assertEqual(t.n_value_recurs(tree, 4), 5)
        self.assertEqual(t.n_value_recurs(tree, 7), -1)


if __name__ == "__main__":
    unittest.main()
