"""
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

#store_index
#last_index
#seen
#st_set

not totally my solution

cbacdcbc
acdb

"""
import unittest


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        st = []
        # set that represents what's in the stack.
        st_set = set()
        for i in range(len(s)):
            if s[i] in st_set:
                continue
            while st and s[i] < st[-1] and last[st[-1]] > i:
                st_set.remove(st.pop())
            st.append(s[i])
            st_set.add(s[i])
        return "".join(st)


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.smallestSubsequence("bcabc"), "abc")
        self.assertEqual(obj.smallestSubsequence("cbacdcbc"), "acdb")
        self.assertEqual(obj.smallestSubsequence("cdadabcc"), "adbc")
        self.assertEqual(obj.smallestSubsequence("cbacdcbcd"), "abcd")
        self.assertEqual(
            obj.smallestSubsequence("baababaaaaababbbbbbaababaababa"), "ab"
        )
        self.assertEqual(obj.smallestSubsequence("cbaacabcaaccaacababa"), "abc")


if __name__ == "__main__":
    unittest.main()
