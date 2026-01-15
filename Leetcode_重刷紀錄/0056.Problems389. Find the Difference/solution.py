"""
389. Find the Difference

Difficulty: Easy
Topics: Hash Table, String, Bit Manipulation, Sorting

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for char in s + t:
            result ^= ord(char)
        return chr(result)
