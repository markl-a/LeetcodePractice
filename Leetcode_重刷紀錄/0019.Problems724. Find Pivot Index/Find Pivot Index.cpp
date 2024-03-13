/* 
這個方法因為使用了在C++語言裡面優化過到 vector loop所以會比單純使用 for loop 快一點
*/
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int highest = 0; // 初始海拔為0，所以最高海拔開始也設為0
        int currentHigh = 0; // 當前海拔
        for (auto& i : gain) {
            currentHigh += i; // 更新當前海拔
            highest = max(highest, currentHigh); // 更新最高海拔
        }
        return highest;
    }
};


/* 
下面這個是完全使用優化過的 C++ 標準函式庫以及減少了宣告函數的動作，所以速度的快了一點
*/
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        gain.insert(gain.begin(), 0);
        std::partial_sum(gain.begin(), gain.end(), gain.begin());
        return *std::max_element(gain.begin(), gain.end());
    }
};