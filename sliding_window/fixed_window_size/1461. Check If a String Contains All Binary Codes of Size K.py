"""
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/
#set_size
#math
the trick here is to know that the set size should be 2**n
"""
import unittest


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k >= len(s):
            return False
        w = 0
        ss = set()
        # Slide window
        while True:
            cur = s[w : w + k]
            ss.add(cur)
            if w + k == len(s):
                break
            w += 1
        return len(ss) == 2**k


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.hasAllCodes("00110110", 2), True)
        self.assertEqual(t.hasAllCodes("0", 20), False)


if __name__ == "__main__":
    unittest.main()
