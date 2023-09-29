"""
https://leetcode.com/problems/reverse-words-in-a-string/
not_completely_solved
"""
import unittest


def reverse(arr: list[str], l: int, r: int):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1


def clean_spaces(s: list[str]):
    # clean spaces by moving cursors to left whenever there is space
    l = 0
    r = 0
    """
        example      good  a 
    l   r
    e    xample      good  a 
        l   r
    examplegood  a 
                l r
    
    """
    while r < len(s):
        while r < len(s) - 1 and s[r] == " ":  # skip spaces
            r += 1
        while r < len(s) and s[r] != " ":
            s[l], s[r] = s[r], s[l]  # shift chars to the left
        while r < len(s) - 1 and s[r] == " ":  # skip spaces
            r += 1
        r += 1
        l += 1
    return s


# reverse in place (in array since python strings are immutable)
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        # reverse all chars
        reverse(s, 0, len(s) - 1)

        # reverse each word
        l = 0
        while l < len(s):
            # skip spaces to know where should the word start
            while l < len(s) and s[l] == " ":
                l += 1
            r = l
            # skip non spaces to know where should the word end
            while r < len(s) and s[r] != " ":
                r += 1
            # reverse word
            reverse(s, l, r - 1)
            # jump
            l = r + 1

        clean_spaces(s)

        return "".join(s)


# class Solution:
#     def reverseWords(self, s: str) -> str:
#         sentence = s.split(" ")
#         arr_trim = []
#         for word in sentence:
#             if word == "":
#                 continue
#             arr_trim.append(word)
#         l = 0
#         r = len(arr_trim) - 1
#         while l < r:
#             arr_trim[l], arr_trim[r] = arr_trim[r], arr_trim[l]
#             l += 1
#             r -= 1
#         return " ".join(arr_trim)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        # self.assertEqual(t.reverseWords("the sky is blue"), "blue is sky the")
        # self.assertEqual(t.reverseWords("   hello world   "), "world hello")
        # self.assertEqual(t.reverseWords(" a  good      example   "), "example good a")
        self.assertEqual(
            clean_spaces(list("  there is a    space   ")), list("there is a space")
        )


if __name__ == "__main__":
    unittest.main()
