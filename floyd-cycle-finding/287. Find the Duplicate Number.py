"""
https://leetcode.com/problems/find-the-duplicate-number/

1,3,4,2,2
      f s                

[3, 1, 3, 4, 2]
    s  f            
[4,4,17,15,2,1,19,11,12,13,3,18,4,4,5,9,7,14,4,16]
[4,2,17,4,5,1,19,11,12,13,3,18,4,4,15,9,7,14,4,16]




1,3,4,2,2

"""


import unittest


# class Solution:
#     def findDuplicate(self, arr: list[int]) -> int:
#         for i in range(len(arr) - 1):
#             should_be = i + 1
#             num = arr[i]
#             while num != should_be:
#                 if num == arr[num - 1]:
#                     return num
#                 arr[num - 1], arr[i] = num, arr[num - 1]
#                 num = arr[i]
#         return arr[-1]


class Solution:
    def findDuplicate(self, arr: list[int]) -> int:
        slow = 1
        while True:
            slow = arr[slow]
            fast = arr[slow]
            print(slow, fast)
            if arr[slow] == arr[fast] and slow != fast:
                return arr[slow]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        # self.assertEqual(obj.findDuplicate([1, 3, 4, 2, 2]), 2)
        self.assertEqual(obj.findDuplicate([3, 1, 3, 4, 2]), 3)
        # self.assertEqual(
        #     obj.findDuplicate(
        #         [4, 4, 17, 15, 2, 1, 19, 11, 12, 13, 3, 18, 4, 4, 5, 9, 7, 14, 4, 16]
        #     ),
        #     4,
        # )
        # self.assertEqual(obj.findDuplicate([9, 4, 9, 5, 7, 2, 8, 9, 3, 9]), 9)


if __name__ == "__main__":
    unittest.main()
