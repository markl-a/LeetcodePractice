# 1679. Max Number of K-Sum Pairs
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        vectorSize = len(nums)
        i = 0
        maxSum = 0.0
        curSum = 0.0

        for i in range(k):
            maxSum += nums[i]
        i = k
        curSum = maxSum

        while i < vectorSize:
            curSum += nums[i] - nums[i - k]
            if maxSum < curSum:
                maxSum = curSum
            i += 1

        return maxSum / k

# 別人給的解法，速度差不多 稍微慢一點點

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Initialize currSum and maxSum to the sum of the initial k elements
        currSum = maxSum = sum(nums[:k])

        # Start the loop from the kth element 
        # Iterate until you reach the end
        for i in range(k, len(nums)):

            # Subtract the left element of the window
            # Add the right element of the window
            currSum += nums[i] - nums[i - k]
            
            # Update the max
            maxSum = max(maxSum, currSum)

        # Since the problem requires average, we return the average
        return maxSum / k