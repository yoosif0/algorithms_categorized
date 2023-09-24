"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray


find the max index of a value that is lower than what's before (end index)
#not_solved

"""
import unittest


class Test(unittest.TestCase):
    def test(self):
        pass
        # obj = Solution()
        # self.assertEqual(obj.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]), 5)
        # self.assertEqual(obj.findUnsortedSubarray([1, 2, 3, 4]), 0)
        # self.assertEqual(obj.findUnsortedSubarray([1]), 0)
        # self.assertEqual(obj.findUnsortedSubarray([5, 4, 3, 2, 1]), 5)
        # self.assertEqual(obj.findUnsortedSubarray([1, 3, 2, 2, 2]), 4)
        # self.assertEqual(obj.findUnsortedSubarray([2, 3, 3, 2, 4]), 3)
        # self.assertEqual(obj.findUnsortedSubarray([1, 2, 4, 5, 3]), 3)
        # self.assertEqual(obj.findUnsortedSubarray([1, 3, 5, 2, 4]), 4)
        # self.assertEqual(obj.findUnsortedSubarray([1, 3, 5, 4, 2]), 4)


if __name__ == "__main__":
    unittest.main()
