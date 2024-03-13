class Solution {
    public int pivotIndex(int[] nums) {
                int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        
        int leftSum = 0;
        for (int i = 0; i < nums.length; ++i) {
            // 当左侧之和等于右侧之和（总和减去左侧之和再减去当前元素）时，当前索引即为枢轴索引
            if (leftSum == totalSum - leftSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }
        
        return -1; // 如果没有找到枢轴索引，则返回 -1
    }
}