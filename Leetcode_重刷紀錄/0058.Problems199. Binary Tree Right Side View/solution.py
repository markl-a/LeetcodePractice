"""
199. Binary Tree Right Side View

Difficulty: Medium
Topics: Tree, DFS, BFS, Binary Tree

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
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node, depth):
            if not node:
                return
            
            # 如果這是當前深度第一個訪問的節點，它一定是最右的
            if depth == len(result):
                result.append(node.val)
            
            # 先訪問右子樹，再訪問左子樹
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return result
