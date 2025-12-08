"""
392. Is Subsequence

Difficulty: Easy
Topics: Two Pointers, String, Dynamic Programming

Problem:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the
remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false

Constraints:
    - 0 <= s.length <= 100
    - 0 <= t.length <= 10^4
    - s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9,
and you want to check one by one to see if t has its subsequence. In this scenario,
how would you change your code?
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Checks if s is a subsequence of t using two pointers.

        Time Complexity: O(n) where n = len(t)
        Space Complexity: O(1)

        Args:
            s: String to check as subsequence
            t: String to check against

        Returns:
            True if s is a subsequence of t, False otherwise
        """
        if len(s) == 0:
            return True

        j = 0  # Pointer for string s
        for char in t:
            if s[j] == char:
                j += 1
                if j == len(s):
                    return True
        return False


class SolutionIterator:
    """Solution using iterator"""

    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Uses iterator to check subsequence.

        Time Complexity: O(n)
        Space Complexity: O(n) for iterator
        """
        t_iter = iter(t)
        return all(char in t_iter for char in s)


class SolutionRecursive:
    """Recursive solution for educational purposes"""

    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Recursively checks if s is a subsequence of t.

        Time Complexity: O(n + m)
        Space Complexity: O(n + m) for recursion stack
        """
        if not s:
            return True
        if not t:
            return False

        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        else:
            return self.isSubsequence(s, t[1:])
