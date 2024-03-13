class Solution {
public:
    int pivotIndex(vector<int>& nums) {
                int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        
        int leftSum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            // 如果左侧之和等于右侧之和（总和减去左侧之和再减去当前元素）
            if (leftSum == totalSum - leftSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }
        
        return -1;
    }
};