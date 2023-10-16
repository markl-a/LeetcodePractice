//1679. Max Number of K-Sum Pairs
//雙指針方法,暫時想不到更快的方法
class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end()); // 只在首次调用时进行排序
        int count = 0,check =0;
        int left = 0, right = nums.size() - 1;
        
        while (left < right) {
            check = nums[left] + nums[right]-k;
            
            if (check == 0) {
                count++;
                left++;
                right--;
            } else if (check < 0) {
                left++;
            } else {
                right--;
            }

        }
        
        return count;
    }
};

//chatgpt給的基於map的方法//比較抽象,也比較慢一點
class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int, int> numCount; // 用于跟踪数字出现的次数
        int count = 0;
        
        for (int num : nums) {
            int complement = k - num;
            
            if (numCount.find(complement) != numCount.end() && numCount[complement] > 0) {
                count++;
                numCount[complement]--;
            } else {
                numCount[num]++;
            }
        }
        
        return count;
    }
};
