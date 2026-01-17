"""
443. String Compression

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

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write, read = 0, 0
        n = len(chars)

        while read < n:
            char = chars[read]
            count = 0

            while read < n and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
