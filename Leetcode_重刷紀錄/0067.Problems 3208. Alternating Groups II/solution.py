"""
3208. Alternating Groups II

Difficulty: Medium
Topics: Array, Sliding Window

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        # 若 k 遠大於 n 或者 n < 3，直接檢查
        if n < 3 or k < 3:
            return 0
        
        # 1) 擴充陣列，避免每次取模
        #    ext 的長度 = n + (k - 1)
        ext = colors + colors[:k-1]
        
        ans = 0
        alt = 1           # 當前連續交替長度
        prev = ext[0]     # 上一個顏色
        
        # 2) 單次 for 迴圈
        for i in range(1, len(ext)):
            c = ext[i]
            # XOR == 1 代表兩顏色不同 => 可延續交替
            if (prev ^ c) == 1:
                alt += 1
            else:
                alt = 1
            # 只要 alt >= k，就表示最後 k 塊已達成交替
            if alt >= k:
                ans += 1
            prev = c
        
        return ans
