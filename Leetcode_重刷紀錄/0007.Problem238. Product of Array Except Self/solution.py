"""
238. Product of Array Except Self

Difficulty: Medium
Topics: Array, Prefix Sum

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length

        for i in range(1, length):
            answer[i] = answer[i - 1] * nums[i - 1]

        R = 1
        for i in range(length - 1, -1, -1):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer
