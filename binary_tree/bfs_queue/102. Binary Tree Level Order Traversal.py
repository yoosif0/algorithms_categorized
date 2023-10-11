"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
This is a regular breadth first search with a small easy trick. We just need to attach to each node in the
queue its level since we would need that when appending to the visited arr
"""
import unittest
from collections import deque
from typing import Optional
from algoutils.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        visited = []
        q: deque[tuple[Optional[TreeNode], int]] = deque([(root, 0)])
        while len(q) > 0:
            (node, level) = q.popleft()
            if not node:
                continue
            if level == len(visited):
                visited.append([])
            visited[level].append(node.val)
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))
        return visited


#                   1
#        2                   3
#   4         7           50   null
# 5   6    null null
class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        tree = TreeNode(
            1,
            TreeNode(2, TreeNode(4, TreeNode(5), TreeNode(6)), TreeNode(7)),
            TreeNode(3, TreeNode(50)),
        )
        self.assertEqual(obj.levelOrder(tree), [])


if __name__ == "__main__":
    unittest.main()
