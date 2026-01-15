"""
2161. Partition Array According to Given Pivot

Difficulty: Medium
Topics: Array, Two Pointers, Simulation

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than = []
        equal_to = []
        greater_than = []
        
        for num in nums:
            if num < pivot:
                less_than.append(num)
            elif num == pivot:
                equal_to.append(num)
            else:
                greater_than.append(num)
        
        return less_than + equal_to + greater_than
