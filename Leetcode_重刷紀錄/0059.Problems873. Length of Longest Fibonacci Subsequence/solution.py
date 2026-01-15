"""
873. Length of Longest Fibonacci Subsequence

Difficulty: Medium
Topics: Array, Hash Table, Dynamic Programming

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        index = {x: i for i, x in enumerate(arr)}
        dp = {}
        max_length = 0
        
        for j in range(n):
            for i in range(j):
                prev_val = arr[j] - arr[i]
                if prev_val < arr[i] and prev_val in index:
                    prev_index = index[prev_val]
                    dp[(i, j)] = dp.get((prev_index, i), 2) + 1
                    max_length = max(max_length, dp[(i, j)])
        
        return max_length if max_length >= 3 else 0
