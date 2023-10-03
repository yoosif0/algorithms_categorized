"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/


Input: s = "abciiidef", k = 3
[abc]  ans = 0
[bci] 1
[cii] 2
[iii] 3
[iid] 2
[ide] 1
[def] 1


Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""


import unittest


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        w = 0
        # initial window
        for i in range(k):
            w += 1 if s[i] in vowels else 0
        ans = w
        # slide window
        i = k - 1
        while True:
            ans = max(ans, w)
            i += 1
            if i == len(s):
                break
            w += 1 if s[i] in vowels else 0
            w -= 1 if s[i - k] in vowels else 0
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxVowels("abciiidef", 3), 3)
        self.assertEqual(t.maxVowels("aeiou", 2), 2)
        self.assertEqual(t.maxVowels("leetcode", 3), 2)
        self.assertEqual(t.maxVowels("ibpbhixfiouhdljnjfflpapptrxgcomvnb", 33), 7)


if __name__ == "__main__":
    unittest.main()
