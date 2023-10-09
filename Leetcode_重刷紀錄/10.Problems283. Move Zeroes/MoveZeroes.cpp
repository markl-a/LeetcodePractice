// 283. Move Zeroes
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int pos = 0,numSize = nums.size();       
        for (int i = 0; i < numSize; i++) {
            if (nums[i] != 0) {
                if (i != pos) { 
                    nums[pos] = nums[i];
                    nums[i] = 0;
                }
                pos++;
            }
        }
    }
};
