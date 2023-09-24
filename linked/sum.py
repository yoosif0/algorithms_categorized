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
    def sum_iteratve(self, l1: Optional[ListNode]) -> int:
        sum = 0
        while l1:
            sum += l1.val
            l1 = l1.next
        return sum

    def sum_recurs(self, head: Optional[ListNode]) -> int:
        sum = 0

        def recurs(node: Optional[ListNode]):
            nonlocal sum
            if not node:
                return
            sum += node.val
            recurs(node.next)

        recurs(head)
        return sum


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
        result = t.sum_iteratve(tree)
        self.assertEqual(result, 15)
        result = t.sum_recurs(tree)
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
