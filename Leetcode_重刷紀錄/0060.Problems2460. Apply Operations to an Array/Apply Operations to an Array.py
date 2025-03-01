class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
        # 應用第一個操作：相鄰元素相等時，第一個乘以2，第二個設為0
        for i in range(n - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        # 使用原地操作將所有0移到末尾
        non_zero_idx = 0
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_idx] = nums[i]
                non_zero_idx += 1
        
        # 將剩餘位置填充為0
        for i in range(non_zero_idx, n):
            nums[i] = 0
        
        return nums
        