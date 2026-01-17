"""
889. Construct Binary Tree from Preorder and Postorder Traversal

Difficulty: Medium
Topics: Array, Hash Table, Divide and Conquer, Tree, Binary Tree

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
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        n = len(pre)
        # 為了快速查找，把後序遍歷轉成字典，記錄每個值的位置
        post_map = {x: i for i, x in enumerate(post)}
        
        def helper(pre_start: int, pre_end: int, post_start: int, post_end: int) -> Optional[TreeNode]:
            # 如果範圍無效，返回空
            if pre_start > pre_end:
                return None
            # 如果只有一個節點，直接返回
            if pre_start == pre_end:
                return TreeNode(pre[pre_start])
                
            # 創建當前節點
            root = TreeNode(pre[pre_start])
            
            # 找左子樹的根在後序遍歷中的位置
            left_root_val = pre[pre_start + 1]
            left_root_post_idx = post_map[left_root_val]
            
            # 計算左子樹的大小
            left_size = left_root_post_idx - post_start + 1
            
            # 遞迴構建左右子樹
            root.left = helper(
                pre_start + 1,                 # 左子樹前序起點
                pre_start + left_size,         # 左子樹前序終點
                post_start,                    # 左子樹後序起點
                left_root_post_idx            # 左子樹後序終點
            )
            
            root.right = helper(
                pre_start + left_size + 1,     # 右子樹前序起點
                pre_end,                       # 右子樹前序終點
                left_root_post_idx + 1,        # 右子樹後序起點
                post_end - 1                   # 右子樹後序終點
            )
            
            return root
            
        return helper(0, n-1, 0, n-1)
