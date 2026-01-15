"""
1372. Longest ZigZag Path in a Binary Tree

Difficulty: Medium
Topics: Tree, DFS, Dynamic Programming, Binary Tree

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0

        def dfs(node):
            if not node:
                return (-1, -1)

            left_left, left_right = dfs(node.left)
            right_left, right_right = dfs(node.right)

            left = left_right + 1
            right = right_left + 1

            self.max_length = max(self.max_length, left, right)

            return (left, right)

        dfs(root)
        return self.max_length
