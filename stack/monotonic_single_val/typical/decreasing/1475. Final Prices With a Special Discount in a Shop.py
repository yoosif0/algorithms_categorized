"""
https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
"""
import unittest


class Solution:
    def finalPrices(self, a: list[int]) -> list[int]:
        st = []
        for i in range(len(a)):
            while st and a[i] <= a[st[-1]]:
                a[st.pop()] -= a[i]
            st.append(i)
        return a


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.finalPrices([8, 4, 6, 2, 3]), [4, 2, 4, 2, 3])


if __name__ == "__main__":
    unittest.main()
