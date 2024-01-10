#1004. Max Consecutive Ones III
# 這邊是實作sliding window 的方法，實現方式類似雙指針，不過主要裝的是同一區域的數值

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=r=0    
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            if k<0:
                if nums[l] == 0:
                    k+=1
                l+=1
        return r-l+1