"""
1524. Number of Sub-arrays With Odd Sum

Difficulty: Medium
Topics: Array, Math, Dynamic Programming, Prefix Sum

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        prefix = 0
        odd = 0
        even = 1  # 初始前綴和為 0，是偶數
        result = 0
        
        for num in arr:
            prefix += num
            if prefix % 2 == 1:
                result += even
                odd += 1
            else:
                result += odd
                even += 1
        
        return result % MOD
