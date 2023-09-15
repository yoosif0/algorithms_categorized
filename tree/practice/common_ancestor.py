"""
Convert tree to array.

[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
16 11 
7    5
3    2
1    0
"""
import unittest
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_parent(i: int):
    return (i - 2) // 2 if i % 2 == 0 else (i - 1) // 2


def bfs(root: "TreeNode", p_tree: "TreeNode", s_tree: "TreeNode"):
    ps = set({p_tree.val, s_tree.val})
    found_indecis = []
    q: deque[Optional[TreeNode]] = deque([root])
    visited = []
    while len(q) > 0 and len(found_indecis) < 2:
        node = q.popleft()
        if not node:
            visited.append(None)
        else:
            visited.append(node.val)
            if node.val in ps:
                found_indecis.append(visited[-1])
            q.append(node.left)
            q.append(node.right)
    return (visited, found_indecis)


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p_tree: "TreeNode", s_tree: "TreeNode"
    ) -> "TreeNode":
        (visited, found_indecis) = bfs(root, p_tree, s_tree)
        # find parent of bigger index that is close to smaller index
        parent_deep_node = get_parent(found_indecis[1])
        while parent_deep_node >= found_indecis[0]:
            parent_deep_node = get_parent(parent_deep_node)

        if parent_deep_node == found_indecis[0]:
            return visited[parent_deep_node]

        parent_shallow_node = get_parent(found_indecis[0])
        while parent_shallow_node >= 0 and parent_deep_node >= 0:
            if parent_shallow_node == parent_deep_node:
                return visited[parent_shallow_node]
            parent_deep_node = get_parent(parent_deep_node)
            if parent_shallow_node == parent_deep_node:
                return visited[parent_shallow_node]
            parent_shallow_node = get_parent(parent_shallow_node)
        return visited[0]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(get_parent(1), 0)
        self.assertEqual(get_parent(0), -1)
        child = TreeNode(4, TreeNode(5), TreeNode(6))
        child2 = TreeNode(7)
        tree = TreeNode(
            1,
            TreeNode(2, child, child2),
            TreeNode(3),
        )
        self.assertEqual(obj.lowestCommonAncestor(tree, child, child2), 2)


if __name__ == "__main__":
    unittest.main()
