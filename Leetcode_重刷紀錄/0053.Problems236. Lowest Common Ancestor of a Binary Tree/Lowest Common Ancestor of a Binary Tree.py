# 二叉樹節點的定義
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        在二叉樹中找到兩個節點 p 和 q 的最低共同祖先（LCA）。

        參數：
            root: 二叉樹的根節點
            p: 第一個節點
            q: 第二個節點

        返回：
            p 和 q 的最低共同祖先
        """

        # 基本情況
        if root is None:
            return None
        if root == p or root == q:
            return root

        # 遞迴步驟
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # 合併結果
        if left_lca is not None and right_lca is not None:
            return root  # p 和 q 分別在不同的子樹中
        elif left_lca is not None:
            return left_lca  # p 和 q 都在左子樹中
        elif right_lca is not None:
            return right_lca  # p 和 q 都在右子樹中
        else:
            return None  # p 和 q 都不在以 root 為根的子樹中