class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
     max_len = 0 # 儲存最大長度
     left = 0 # 滑動視窗的左邊界
     zero_count = 0 # 視窗內0的數量
    
     for right in range(len(nums)):
         if nums[right] == 0:
             zero_count += 1
            
         # 當視窗內0的數量超過1時，移動左邊界
         while zero_count > 1:
             if nums[left] == 0:
                 zero_count -= 1
             left += 1
            
         # 更新最大長度。 注意：依照題目要求，最終長度需要排除一個0，因此實際長度為 right - left
         max_len = max(max_len, right - left)
    
     return max_len