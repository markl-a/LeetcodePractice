# 使用 itertools accumulate 函數，網路上看到最短的解
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
       return max(accumulate(gain, initial=0))