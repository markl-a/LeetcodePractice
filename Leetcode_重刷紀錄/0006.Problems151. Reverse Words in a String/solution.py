"""
151. Reverse Words in a String

Difficulty: Medium
Topics: Two Pointers, String

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
