"""
11. Container With Most Water

Difficulty: Medium
Topics: Array, Two Pointers, Greedy

Problem:
You are given an integer array height of length n. There are n vertical lines drawn such that
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The max area is between index 1 and 8, area = min(8,7) * (8-1) = 49

Example 2:
    Input: height = [1,1]
    Output: 1

Constraints:
    - n == height.length
    - 2 <= n <= 10^5
    - 0 <= height[i] <= 10^4
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Finds maximum water container using two pointers.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            height: Array of line heights

        Returns:
            Maximum area of water container
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


class SolutionBruteForce:
    """Brute force solution for educational purposes"""

    def maxArea(self, height: List[int]) -> int:
        """
        Checks all pairs of lines. O(n^2) time complexity.
        """
        n = len(height)
        max_area = 0

        for i in range(n):
            for j in range(i + 1, n):
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)

        return max_area
