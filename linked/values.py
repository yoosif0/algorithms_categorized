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
    def fill_arr_iterative(self, l1: Optional[ListNode]) -> list[int]:
        arr = []
        while l1:
            arr.append(l1.val)
            l1 = l1.next
        return arr

    def fill_arr_recurs(self, head: Optional[ListNode]) -> list[int]:
        arr = []

        def recurs(node: Optional[ListNode]):
            if not node:
                return
            arr.append(node.val)
            recurs(node.next)

        recurs(head)
        return arr


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
        result = t.fill_arr_iterative(tree)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        result = t.fill_arr_recurs(tree)
        self.assertEqual(result, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
