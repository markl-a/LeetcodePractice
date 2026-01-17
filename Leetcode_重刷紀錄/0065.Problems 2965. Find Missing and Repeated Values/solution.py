"""
2965. Find Missing and Repeated Values

Difficulty: Medium
Topics: Array, Hash Table, Math, Matrix

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        expected_nums = set(range(1, n*n + 1))
        repeated = None
        
        for row in grid:
            for num in row:
                if num in expected_nums:
                    expected_nums.remove(num)
                else:
                    repeated = num
        
        missing = next(iter(expected_nums))
        
        return [repeated, missing]
