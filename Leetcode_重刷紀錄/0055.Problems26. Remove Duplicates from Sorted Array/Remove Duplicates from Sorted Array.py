class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # 處理空陣列的特殊情況
            return 0

        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow - 1]:
                nums[slow] = nums[fast]
                slow += 1
        return slow