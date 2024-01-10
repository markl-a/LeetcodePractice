//1004. Max Consecutive Ones III
/* 這邊是實作sliding window 的方法，實現方式類似雙指針，不過主要裝的是同一區域的數值
*/
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int left = 0, right = 0;
        int max_length = 0;
        int zero_count = 0;

        while (right < nums.size()) {
            if (nums[right] == 0) {
                zero_count++;
            }

            while (zero_count > k) {
                if (nums[left] == 0) {
                    zero_count--;
                }
                left++;
            }

            max_length = max(max_length, right - left + 1);
            right++;
        }

        return max_length;
    }
};


