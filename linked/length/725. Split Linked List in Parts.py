"""
https://leetcode.com/problems/split-linked-list-in-parts/
#dummy
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
1  2 3 4 5 6 7 8 9 10
h      p
"""


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> list[Optional[ListNode]]:
        ans: list[Optional[ListNode]] = []
        # Find length of chain
        r = ListNode(0, head)
        len = 0
        while r and r.next:
            r = r.next
            len += 1
        # min number of nodes in each list item
        min_count = len // k
        # remaining to be distributed one for each list item until finishes
        remaining = len % k
        # break chain for each list item
        while k != 0:
            node_count = min_count
            if remaining != 0:
                node_count += 1
                remaining -= 1
            p = ListNode(0, head)
            while node_count > 0:
                p = p.next
                node_count -= 1
            ans.append(head)
            k -= 1
            p.next, head = None, p.next
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        tree = ListNode(
            1,
            ListNode(
                2,
                ListNode(
                    3,
                    ListNode(
                        4,
                        ListNode(
                            5,
                            ListNode(
                                6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))
                            ),
                        ),
                    ),
                ),
            ),
        )
        print(t.splitListToParts(tree, 3))
        tree = ListNode(1, ListNode(2, ListNode(3)))
        print(t.splitListToParts(tree, 5))


if __name__ == "__main__":
    unittest.main()
