"""
345. Reverse Vowels of a String

Difficulty: Easy
Topics: Two Pointers, String

Problem:
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases,
more than once.

Example 1:
    Input: s = "hello"
    Output: "holle"

Example 2:
    Input: s = "leetcode"
    Output: "leotcede"

Constraints:
    - 1 <= s.length <= 3 * 10^5
    - s consist of printable ASCII characters.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Reverses only the vowels in a string using two pointers.

        Time Complexity: O(n) where n = len(s)
        Space Complexity: O(n) for converting string to list

        Args:
            s: Input string

        Returns:
            String with vowels reversed
        """
        vowels = set("aeiouAEIOU")
        s_list = list(s)
        left, right = 0, len(s_list) - 1

        while left < right:
            # Move left pointer to next vowel
            while left < right and s_list[left] not in vowels:
                left += 1

            # Move right pointer to next vowel (from right)
            while left < right and s_list[right] not in vowels:
                right -= 1

            # Swap vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return "".join(s_list)


class SolutionStack:
    """Alternative solution using a stack to store vowels"""

    def reverseVowels(self, s: str) -> str:
        """
        Reverses vowels using a stack approach.

        Time Complexity: O(n)
        Space Complexity: O(n) for the stack and result
        """
        vowels = set("aeiouAEIOU")

        # Collect all vowels in order
        vowel_stack = [char for char in s if char in vowels]

        # Rebuild string, replacing vowels from the end of the stack
        result = []
        for char in s:
            if char in vowels:
                result.append(vowel_stack.pop())
            else:
                result.append(char)

        return "".join(result)


class SolutionTwoPass:
    """Solution using two passes - first to collect vowels, second to rebuild"""

    def reverseVowels(self, s: str) -> str:
        """
        Reverses vowels using two-pass approach.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        vowels = set("aeiouAEIOU")

        # First pass: collect vowels and their positions
        vowel_chars = []
        vowel_positions = []

        for i, char in enumerate(s):
            if char in vowels:
                vowel_chars.append(char)
                vowel_positions.append(i)

        # Reverse the vowels
        vowel_chars.reverse()

        # Second pass: rebuild string
        s_list = list(s)
        for i, pos in enumerate(vowel_positions):
            s_list[pos] = vowel_chars[i]

        return "".join(s_list)
