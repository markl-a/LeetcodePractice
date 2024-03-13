class Solution:
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            # 如果左侧之和等于总和减去左侧之和再减去当前元素，则找到枢轴索引
            if left_sum == (total_sum - left_sum - num):
                return i
            left_sum += num
        return -1  # 如果遍历完数组后没有找到枢轴索引，返回-1
