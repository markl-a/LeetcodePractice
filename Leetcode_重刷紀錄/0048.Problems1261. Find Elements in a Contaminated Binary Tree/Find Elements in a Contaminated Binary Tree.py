# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.dfs = lambda r, v: r and (setattr(r, 'val', v), self.seen.add(v), 
            self.dfs(r.left, 2 * v + 1), self.dfs(r.right, 2 * v + 2))
        self.dfs(root, 0)
   
    def find(self, target: int) -> bool:
        return target in self.seen

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)