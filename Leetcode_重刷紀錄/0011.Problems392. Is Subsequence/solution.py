"""
392. Is Subsequence

Difficulty: Easy
Topics: Two Pointers, String, Dynamic Programming

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        j = 0
        for char in t:
            if s[j] == char:
                j += 1
                if j == len(s):
                    return True
        return False
