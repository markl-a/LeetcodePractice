"""
1980. Find Unique Binary String

Difficulty: Medium
Topics: Array, Hash Table, String, Backtracking

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append('1' if nums[i][i] == '0' else '0')
        return "".join(ans)
