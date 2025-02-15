# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0

            count = 0
            if node.val >= max_val:
                count = 1
                max_val = node.val

            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)

            return count

        return dfs(root, float('-inf'))  # 或者 dfs(root, root.val)