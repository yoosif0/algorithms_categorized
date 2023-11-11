"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

"sadbutsad" "sad"
 i           j
"sadbutsad" "sad"
  i           j
"sadbutsad" "sad"
   i           j
 
"mississippi" "issip"
      i            j
"mississippi" "issip"
     i         j



"""
import unittest


class Solution:
    def strStr(self, s: str, s2: str) -> int:
        for r in range(len(s)):
            if s[r] == s2[-1] and r + 1 >= len(s2):
                l = r - len(s2) + 1
                if s[l : r + 1] == s2:
                    return l
        return -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.strStr("sadbutsad", "sad"), 0)
        self.assertEqual(t.strStr("leetcode", "leeto"), -1)
        self.assertEqual(t.strStr("mississippi", "issip"), 4)


if __name__ == "__main__":
    unittest.main()
