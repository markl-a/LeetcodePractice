"""
1780. Check if Number is a Sum of Powers of Three

Difficulty: Medium
Topics: Math

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 2:
                return False
            n //= 3
        return True
