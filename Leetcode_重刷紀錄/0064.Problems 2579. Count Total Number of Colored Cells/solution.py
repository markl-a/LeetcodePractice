"""
2579. Count Total Number of Colored Cells

Difficulty: Medium
Topics: Math, Geometry

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * (n - 1) + 1
