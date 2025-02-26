
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = curr = 0
        
        for num in nums:
            curr += num
            max_sum = curr if curr > max_sum else max_sum
            min_sum = curr if curr < min_sum else min_sum
        
        return max_sum - min_sum