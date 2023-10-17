//643. Maximum Average Subarray I
/* 這邊是實作sliding window 的方法，實現方式類似雙指針，不過主要裝的是同一區域的數值
*/
#include <vector>

using namespace std;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int vectorSize = nums.size(), i = 0;
        double maxSum = 0.0, curSum ;

        do {
            maxSum += nums[i];
        } while (++i < k);
        // now i == k
        curSum = maxSum;

        //會有  k == vectorSize 的狀況 i 會小於0
        //所以不能使用 do while
        while (i < vectorSize){
            curSum += nums[i] - nums[i - k];
            if (maxSum < curSum) {
                maxSum = curSum;
            }
            i++;
        } 

        return maxSum/= k;
    }
};


