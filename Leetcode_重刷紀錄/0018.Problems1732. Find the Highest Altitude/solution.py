"""
1732. Find the Highest Altitude

Difficulty: Easy
Topics: Array, Prefix Sum

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
       return max(accumulate(gain, initial=0))
