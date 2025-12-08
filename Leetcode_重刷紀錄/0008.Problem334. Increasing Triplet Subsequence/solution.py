"""
334. Increasing Triplet Subsequence

Difficulty: Medium
Topics: Array, Greedy

Problem:
Given an integer array nums, return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.

Example 2:
    Input: nums = [5,4,3,2,1]
    Output: false
    Explanation: No triplet exists.

Example 3:
    Input: nums = [2,1,5,0,4,6]
    Output: true
    Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
    - 1 <= nums.length <= 5 * 10^5
    - -2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Finds if increasing triplet subsequence exists using greedy approach.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            nums: Input array of integers

        Returns:
            True if increasing triplet exists, False otherwise
        """
        first = float("inf")
        second = float("inf")

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False


class SolutionMinMax:
    """Solution using prefix min and suffix max arrays"""

    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Uses precomputed min from left and max from right.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        if n < 3:
            return False

        # min_left[i] = minimum value in nums[0:i+1]
        min_left = [0] * n
        min_left[0] = nums[0]
        for i in range(1, n):
            min_left[i] = min(min_left[i - 1], nums[i])

        # max_right[i] = maximum value in nums[i:n]
        max_right = [0] * n
        max_right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], nums[i])

        # Check if middle element exists
        for i in range(1, n - 1):
            if min_left[i - 1] < nums[i] < max_right[i + 1]:
                return True

        return False
