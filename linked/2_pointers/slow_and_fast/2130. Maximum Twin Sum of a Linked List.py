"""
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

None  <-  5 <- 4 <- 6       2     8    1
                   p0       h               f


reverse either the first half or second half then sum merge of each pair

#fast_slow_pointers
#2_lists
#reverse

"""
from collections import deque
from typing import Optional
import unittest
from algoutils.list_node import ListNode


# O(1) space
class Solution:
    def pairSum(self, h: Optional[ListNode]) -> int:
        # reverse first half of list to have 2 lists where each node in a list
        # have the same index with its pair in the other list
        d = None
        f = h
        while f and f.next:
            f = f.next.next
            h.next, d, h = d, h, h.next

        # get sum for each pair and compare with max
        ans = 0
        while p0:
            sum = p0.val + h.val
            ans = max(ans, sum)
            p0, h = p0.next, h.next
        return ans


# # O(n) space
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         a = deque([])
#         while head:
#             a.append(head.val)
#             head = head.next

#         ans = -sys.maxsize
#         while len(a):
#             sum = a.pop() + a.popleft()
#             ans = max(ans, sum)

#         return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        tree = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        self.assertEqual(t.pairSum(tree), 5)


if __name__ == "__main__":
    unittest.main()
