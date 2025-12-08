"""
151. Reverse Words in a String

Difficulty: Medium
Topics: Two Pointers, String

Problem:
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated
by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include
any extra spaces.

Example 1:
    Input: s = "the sky is blue"
    Output: "blue is sky the"

Example 2:
    Input: s = "  hello world  "
    Output: "world hello"
    Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
    Input: s = "a good   example"
    Output: "example good a"
    Explanation: You need to reduce multiple spaces between two words to a single space.

Constraints:
    - 1 <= s.length <= 10^4
    - s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    - There is at least one word in s.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverses the order of words in a string using built-in methods.

        Time Complexity: O(n) where n = len(s)
        Space Complexity: O(n) for storing the result

        Args:
            s: Input string containing words separated by spaces

        Returns:
            String with words in reverse order, separated by single spaces
        """
        return " ".join(reversed(s.split()))


class SolutionTwoPointers:
    """Alternative solution using two pointers without built-in split/reverse"""

    def reverseWords(self, s: str) -> str:
        """
        Reverses words using manual parsing and two pointers.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        words = []
        n = len(s)
        i = 0

        while i < n:
            # Skip leading spaces
            while i < n and s[i] == " ":
                i += 1

            if i >= n:
                break

            # Find end of current word
            j = i
            while j < n and s[j] != " ":
                j += 1

            # Add word to front of list (reverse order)
            words.append(s[i:j])
            i = j

        # Join words in reverse order
        return " ".join(reversed(words))


class SolutionInPlace:
    """Solution that reverses in-place (for languages with mutable strings)"""

    def reverseWords(self, s: str) -> str:
        """
        Reverses words by first reversing entire string, then each word.

        Time Complexity: O(n)
        Space Complexity: O(n) - would be O(1) with mutable strings
        """
        # Split and filter empty strings
        words = s.split()

        # Reverse the list of words
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)
