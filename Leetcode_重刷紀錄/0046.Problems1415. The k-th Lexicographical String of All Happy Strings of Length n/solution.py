"""
1415. The k-th Lexicographical String of All Happy Strings of Length n

Difficulty: Medium
Topics: String, Backtracking

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (2 ** (n-1)) if n > 0 else 0
        
        if k > total:
            return ""
        
        result = []
        k -= 1  
        
        first_char = chr(97 + k // (2 ** (n-1)))
        result.append(first_char)
        k %= (2 ** (n-1))
        
        for i in range(n-1):
            candidates = ['a', 'b', 'c']
            candidates.remove(result[-1])  
            next_char = candidates[k // (2 ** (n-2-i))]
            result.append(next_char)
            k %= (2 ** (n-2-i))
        
        return ''.join(result)
