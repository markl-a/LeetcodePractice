"""
872. Leaf-Similar Trees

Difficulty: Easy
Topics: Tree, DFS, Binary Tree

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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_sequence(root):
            leaf_sequence = []

            def dfs(node):
                if not node:
                    return

                if not node.left and not node.right:
                    leaf_sequence.append(node.val)
                    return

                dfs(node.left)
                dfs(node.right)
            dfs(root)
            return leaf_sequence

        seq1 = get_leaf_sequence(root1)
        seq2 = get_leaf_sequence(root2)
        return seq1 == seq2
