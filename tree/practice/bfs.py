import unittest
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bfs(self, tree: Optional[TreeNode]):
        q = deque([tree])
        visited = []

        while len(q) > 0:
            node = q.popleft()
            if not node:
                visited.append(None)
            else:
                visited.append(node.val)
                q.append(node.left)
                q.append(node.right)

        return visited


#                   1
#        2                   3
#   4         7           null   null
# 5   6    null null
class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        tree = TreeNode(
            1,
            TreeNode(2, TreeNode(4, TreeNode(5), TreeNode(6)), TreeNode(7)),
            TreeNode(3),
        )
        self.assertEqual(obj.bfs(tree), [])


if __name__ == "__main__":
    unittest.main()
