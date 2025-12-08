"""
238. Product of Array Except Self

Difficulty: Medium
Topics: Array, Prefix Sum

Problem:
Given an integer array nums, return an array answer such that answer[i] is equal to the
product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

Constraints:
    - 2 <= nums.length <= 10^5
    - -30 <= nums[i] <= 30
    - The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculates product of array except self using prefix/suffix products.

        Time Complexity: O(n)
        Space Complexity: O(1) extra space (output array doesn't count)

        Args:
            nums: Input array of integers

        Returns:
            Array where answer[i] is product of all elements except nums[i]
        """
        length = len(nums)
        answer = [1] * length

        # Calculate prefix products (left to right)
        for i in range(1, length):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Calculate suffix products and combine (right to left)
        right_product = 1
        for i in range(length - 1, -1, -1):
            answer[i] = answer[i] * right_product
            right_product *= nums[i]

        return answer


class SolutionTwoArrays:
    """Solution using separate prefix and suffix arrays (more intuitive)"""

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Uses separate prefix and suffix product arrays.

        Time Complexity: O(n)
        Space Complexity: O(n) for prefix and suffix arrays
        """
        n = len(nums)

        # Prefix products: prefix[i] = product of nums[0..i-1]
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Suffix products: suffix[i] = product of nums[i+1..n-1]
        suffix = [1] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Result is prefix[i] * suffix[i]
        return [prefix[i] * suffix[i] for i in range(n)]


class SolutionWithDivision:
    """Solution using division (for educational purposes, violates constraint)"""

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Uses division - NOT allowed by problem constraints.
        Included for educational comparison only.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        total_product = 1
        zero_count = 0
        zero_index = -1

        for i, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                zero_index = i
            else:
                total_product *= num

        # Handle zero cases
        if zero_count > 1:
            return [0] * n
        elif zero_count == 1:
            result = [0] * n
            result[zero_index] = total_product
            return result
        else:
            return [total_product // num for num in nums]
