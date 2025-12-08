"""
283. Move Zeroes

Difficulty: Easy
Topics: Array, Two Pointers

Problem:
Given an integer array nums, move all 0's to the end of it while maintaining the relative
order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:
    Input: nums = [0]
    Output: [0]

Constraints:
    - 1 <= nums.length <= 10^4
    - -2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you minimize the total number of operations done?
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all zeros to end while maintaining relative order of non-zeros.
        Uses two-pointer technique with single pass.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            nums: Input array to modify in-place
        """
        pos = 0  # Position to place next non-zero element

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1


class SolutionTwoPass:
    """Alternative solution using two passes"""

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Two-pass approach: first collect non-zeros, then fill zeros.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # First pass: move non-zero elements to front
        pos = 0
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1

        # Second pass: fill remaining positions with zeros
        while pos < len(nums):
            nums[pos] = 0
            pos += 1


class SolutionCountZeros:
    """Solution that counts zeros and rebuilds array"""

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Count zeros and rebuild: non-zeros first, then zeros.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        zero_count = nums.count(0)
        non_zeros = [x for x in nums if x != 0]

        # Rebuild array in place
        for i, val in enumerate(non_zeros):
            nums[i] = val
        for i in range(len(non_zeros), len(nums)):
            nums[i] = 0
