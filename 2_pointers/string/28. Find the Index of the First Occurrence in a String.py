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
    def strStr(self, haystack: str, needle: str) -> int:
        n_i = 0
        h_i = 0
        upcoming_h_i = None
        while h_i < len(haystack):
            if (
                h_i != 0
                and n_i != 0
                and haystack[h_i] == needle[0]
                and upcoming_h_i is None
            ):
                upcoming_h_i = h_i
            if haystack[h_i] == needle[n_i]:
                if n_i == len(needle) - 1:
                    return h_i - n_i
                n_i += 1
                h_i += 1
            else:
                n_i = 0
                if upcoming_h_i:
                    h_i = upcoming_h_i
                    upcoming_h_i = None
                else:
                    h_i += 1
        return -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.strStr("sadbutsad", "sad"), 0)
        self.assertEqual(t.strStr("leetcode", "leeto"), -1)
        self.assertEqual(t.strStr("mississippi", "issip"), 4)


if __name__ == "__main__":
    unittest.main()
