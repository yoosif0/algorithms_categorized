"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

"""
import unittest


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for ch in s:
            if not st or ch != st[-1][0]:
                st.append([ch, 1])
            else:
                st[-1][1] += 1
                if st[-1][1] == k:
                    st.pop()
        ans = []
        for el in st:
            for _ in range(el[1]):
                ans.append(el[0])
        return "".join(ans)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.removeDuplicates("abcd", 2), "abcd")
        self.assertEqual(t.removeDuplicates("deeedbbcccbdaa", 3), "aa")


if __name__ == "__main__":
    unittest.main()
