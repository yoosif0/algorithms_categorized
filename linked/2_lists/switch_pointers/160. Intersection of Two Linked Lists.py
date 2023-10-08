"""
https://leetcode.com/problems/intersection-of-two-linked-lists/

O(1) space solution involves switching pointers between 2 lists. The idea here is that we want
the 2 pointers meet at the intersection. One pointer usually takes more time to reach there before the other.
If we let pa point to listB when pa reaches tail and vice versa, they will meet at the same point.
This is like having 2 different starting points in a track. If we have 2 players and both have the
same speed. If we let them race twice back to back, they'll reach the same position.
"""


from typing import Optional
import unittest
from algoutils.list_node import ListNode


# O(n) space
# class Solution:
#     def getIntersectionNode(
#         self, headA: ListNode, headB: ListNode
#     ) -> Optional[ListNode]:
#         s = set()
#         while headA:
#             s.add(headA)
#             headA = headA.next
#         while headB:
#             if headB in s:
#                 return headB
#             s.add(headB)
#             headB = headB.next
#         return None


# O(1) space
class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        pa = headA
        pb = headB
        while True:
            if pa == pb:
                return pa
            if not pa:
                pa = headB
                pb = pb.next
            elif not pb:
                pb = headA
                pa = pa.next
            else:
                pb, pa = pb.next, pa.next


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        c_list = ListNode(8, ListNode(4, ListNode(5)))
        a_list = ListNode(4, ListNode(1, c_list))
        b_list = ListNode(5, ListNode(6, ListNode(1, c_list)))
        print(t.getIntersectionNode(a_list, b_list))


if __name__ == "__main__":
    unittest.main()
