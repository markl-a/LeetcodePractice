"""
11. Container With Most Water

Difficulty: Medium
Topics: Array, Two Pointers, Greedy

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area,w = 0 , right - left

        while w :
            w = right - left
            if height[left] < height[right]:
                max_area = max(max_area, height[left] * w )
                left += 1
            else:
                max_area = max(max_area, height[right] * w )
                right -= 1

        return max_area
