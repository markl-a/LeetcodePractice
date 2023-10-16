# 1679. Max Number of K-Sum Pairs
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort() 
        left, right = 0, len(nums) - 1
        count = 0

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == k:
                count += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1

        return count    