# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, current_sum, prefix_sums):
            if not node:
                return 0

            count = 0
            current_sum += node.val

            # 檢查是否存在符合條件的前綴和
            count += prefix_sums[current_sum - targetSum]

            # 更新目前前綴和的計數
            prefix_sums[current_sum] += 1

            # 遞迴走訪左右子樹
            count += dfs(node.left, current_sum, prefix_sums)
            count += dfs(node.right, current_sum, prefix_sums)

            # 回溯：移除目前前綴和
            prefix_sums[current_sum] -= 1

            return count

        prefix_sums = collections.defaultdict(int)
        prefix_sums[0] = 1  # 初始時，前綴和為 0 的出現次數為 1 (空路徑)
        return dfs(root, 0, prefix_sums)