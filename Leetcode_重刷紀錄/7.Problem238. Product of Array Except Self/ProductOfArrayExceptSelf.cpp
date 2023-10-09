// 238. Product of Array Except Self
#include <vector>
#include <algorithm>  
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int length = nums.size();
        int maxNum =1,zeroIndex = -1;
        bool InputHasZero = false;
        vector<int> answer(length);
        for (int i = 0; i < length; ++i) {
            if( nums[i]!=0){
                maxNum *= nums[i];  
            }else{
                if(InputHasZero){// if it has more than 1 zero
                    std::vector<int> vec(length); 
                    std::fill(vec.begin(), vec.end(), 0);
                    return vec;
                }else{
                    InputHasZero = true;
                    zeroIndex = i;
                }
            }                  
        }
        if(InputHasZero){
            std::vector<int> vec(length); 
            std::fill(vec.begin(), vec.end(), 0);
            vec[zeroIndex]= maxNum;
            return vec;
        }else{
            std::vector<int> vec(length);
            for (int i = 0; i < length; ++i) {
            vec[i]= maxNum/nums[i];
            }
            return vec;
        }

    }
};

//傳統解法

#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int length = nums.size();
        std::vector<int> left(length, 1);  // 前綴乘積
        std::vector<int> right(length, 1); // 後綴乘積
        std::vector<int> answer(length);

        // 計算前綴乘積
        for (int i = 1; i < length; ++i) {
            left[i] = left[i - 1] * nums[i - 1];
        }

        // 計算後綴乘積
        for (int i = length - 2; i >= 0; --i) {
            right[i] = right[i + 1] * nums[i + 1];
        }

        // 計算答案
        for (int i = 0; i < length; ++i) {
            answer[i] = left[i] * right[i];
        }

        return answer;
    }
};
