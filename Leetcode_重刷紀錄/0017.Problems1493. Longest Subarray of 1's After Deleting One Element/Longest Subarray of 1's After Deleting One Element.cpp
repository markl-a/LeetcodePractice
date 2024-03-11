//1004. Max Consecutive Ones III
/* 最佳化點說明：

• 透過hasZero標記變量，我們可以知道數組中是否存在0，從而在最後判斷是否需要減1（當數組全為1時）。
• 此程式碼在遍歷過程中只進行必要的長度更新，減少了不必要的計算。
• 在循環外最後一次更新maxLen是為了處理數組結尾是1的情況，這保證了最後一段連續1也被考慮在內。
• 此解法的時間複雜度依然是O(n)，但是透過減少計算和簡化邏輯，它在實際運作時可能會更快一些。
*/
#include <vector>
#include <algorithm>

class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size(); 
        int currentLength = 0; // 當前連續1的長度
        int previousLength =0;
        int maxLength = 0;
        /**
        if (nums[0] == 1) {
                ++currentLength;
        }**/
        currentLength += nums[0];
        // 遍歷數組計算連續1的長度
        for (int i = 1; i < n; ++i) {
            if (nums[i]) {//nums[i] ==1
                ++currentLength;
            } else {
                if(!nums[i-1]){//排除兩個零的狀況 nums[i-1] == 0
                    previousLength = currentLength = 0;
                }else if (currentLength > 0 ) {
                    maxLength =  std::max(maxLength, previousLength + currentLength);
                    previousLength = currentLength;
                    currentLength = 0;
                }
            }
        }
        if(nums[n-1]){//nums[n-1] ==1
            maxLength =  std::max(maxLength, previousLength + currentLength);
        }
        // 如果沒有0，則需要刪除一個1
        if (maxLength == n) {
            maxLength --;
        }

        return maxLength;  
    }
};


