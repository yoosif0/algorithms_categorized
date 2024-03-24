"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

[1,2,3,4,5,6,7,8]
[1,5,7,8,12,12,14]


"""

# import unittest


# class Solution:
#     def kSmallestPairs(self, a: list[int], a2: list[int], k: int) -> list[list[int]]:
#         ans = [[a[0], a2[0]]]
#         p = 0
#         p2 = 0
#         while len(ans) < k:
#             if p == len(a) or (p2 < len(a2) and a[p + 1] >= a2[p2 + 1]):
#                 p2 += 1
#             else:
#                 p += 1
#             ans.append([a[p], a2[p2]])
#         return ans


# class Test(unittest.TestCase):
#     def test(self):
#         obj = Solution()
#         self.assertEqual(
#             obj.kSmallestPairs([1, 7, 11], [2, 4, 6], 3), [[1, 2], [1, 4], [1, 6]]
#         )
#         self.assertEqual(obj.kSmallestPairs([1, 1, 2], [1, 2, 3], 2), [[1, 1], [1, 1]])


# if __name__ == "__main__":
#     unittest.main()
