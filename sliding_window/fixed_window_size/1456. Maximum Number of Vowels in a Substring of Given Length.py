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
        ans = 0
        window_vowel_count = 0

        def and_to_window(index: int):
            nonlocal window_vowel_count
            char = s[index]
            if char in vowels:
                window_vowel_count += 1

        def remove_form_window(index: int):
            nonlocal window_vowel_count
            char = s[index]
            if char in vowels:
                window_vowel_count -= 1

        def update_ans_if_applicable():
            nonlocal ans
            ans = max(ans, window_vowel_count)

        # initial window
        for i in range(k):
            and_to_window(i)
        update_ans_if_applicable()

        # slide window
        for i in range(k, len(s)):
            and_to_window(i)
            remove_form_window(i - k)
            update_ans_if_applicable()

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
