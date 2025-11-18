"""
1071. Greatest Common Divisor of Strings

Difficulty: Easy
Topics: String, Math

Problem:
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated
with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

Example 2:
    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

Example 3:
    Input: str1 = "LEET", str2 = "CODE"
    Output: ""

Constraints:
    - 1 <= str1.length, str2.length <= 1000
    - str1 and str2 consist of English uppercase letters.
"""

import math


class Solution:
    """Optimized solution using mathematical GCD"""

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Finds the greatest common divisor string using GCD of lengths.

        Key Insight: If str1 and str2 have a common divisor, then str1 + str2 == str2 + str1
        The GCD string length is the GCD of the two string lengths.

        Time Complexity: O(n + m) where n = len(str1), m = len(str2)
        Space Complexity: O(n + m) for string concatenation

        Args:
            str1: First string
            str2: Second string

        Returns:
            The largest string that divides both str1 and str2, or "" if none exists
        """
        # Check if str1 and str2 have a common pattern
        if str1 + str2 != str2 + str1:
            return ""

        # The GCD string has length equal to GCD of the two lengths
        return str1[: math.gcd(len(str1), len(str2))]


class SolutionRecursive:
    """Recursive solution using Euclidean algorithm pattern"""

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Finds the greatest common divisor string recursively.

        Time Complexity: O(n + m)
        Space Complexity: O(n + m) for recursion stack

        Args:
            str1: First string
            str2: Second string

        Returns:
            The largest string that divides both str1 and str2, or "" if none exists
        """
        # Ensure str1 is not shorter than str2
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)

        # If str1 doesn't start with str2, no common divisor exists
        if not str1.startswith(str2):
            return ""

        # Base case: str2 is empty, return str1
        if not str2:
            return str1

        # Recursively find GCD of remainder and str2
        return self.gcdOfStrings(str1[len(str2) :], str2)


class SolutionBruteForce:
    """Brute force solution for educational purposes"""

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Finds the greatest common divisor string by checking all possible divisors.

        Time Complexity: O(min(n, m) * (n + m))
        Space Complexity: O(1)
        """
        min_len = min(len(str1), len(str2))

        # Check from longest to shortest possible divisor
        for length in range(min_len, 0, -1):
            # Check if this length divides both string lengths
            if len(str1) % length == 0 and len(str2) % length == 0:
                candidate = str1[:length]
                # Check if candidate divides both strings
                if self._divides(str1, candidate) and self._divides(str2, candidate):
                    return candidate

        return ""

    def _divides(self, s: str, t: str) -> bool:
        """Check if string t divides string s"""
        if len(s) % len(t) != 0:
            return False
        repeat_count = len(s) // len(t)
        return t * repeat_count == s
