"""
1456. Maximum Number of Vowels in a Substring of Given Length

Difficulty: Medium
Topics: String, Sliding Window

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

asiiVo = defaultdict(int)
asiiVo['a'] = asiiVo['e'] = asiiVo['i'] = asiiVo['o'] = asiiVo['u'] = 1

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        j = [asiiVo[c] for c in s] # 全部字串先分辨一遍

        maxVos = Vos = sum(j[:k])      # 將前面k個相加

        for i in range(len(j) - k):         # 之後就是slide window的方法
            Vos += j[i + k] - j[i]       
            maxVos = max(Vos,maxVos)
            
        return maxVos
