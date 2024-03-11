public class Solution {
    public int longestSubarray(int[] nums) {
        int maxLen = 0;
        int left = 0; // 視窗的左邊界
        int zeroCount = 0; // 視窗內0的數量
       
        // 遍歷數組，右邊界不斷擴展
        for (int right = 0; right < nums.length; right++) {
            // 如果遇到0，增加0的數
            if (nums[right] == 0) {
                zeroCount++;
            }
           
            // 當視窗內的0的數量超過1時，移動左邊界直到視窗內最多含一個0
            while (zeroCount > 1) {
                if (nums[left] == 0) {
                    zeroCount--;
                }
                left++;
            }
           
            // 更新最大長度，注意這裡不包含目前的0，因為題目要求刪除一個元素
            maxLen = Math.max(maxLen, right - left);
        }
       
        return maxLen;
    }
}