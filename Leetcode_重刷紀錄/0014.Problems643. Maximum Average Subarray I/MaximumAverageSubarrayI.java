//1679. Max Number of K-Sum Pairs
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int vectorSize = nums.length;
        int i = 0;
        double maxSum = 0.0, curSum = 0.0;

        do {
            maxSum += nums[i];
        }while(++i < k);
        // now i == k
        curSum = maxSum;

        // 会有 i == k == vectorSize 的情况
        // 所以不能使用 do while
        while (i < vectorSize) {
            curSum += nums[i] - nums[i - k];
            if (maxSum < curSum) {
                maxSum = curSum;
            }
            i++;
        }

        return maxSum / k;
    }
}


