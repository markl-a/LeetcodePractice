#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> countMap; // 映射來儲存每個數字的計數
        for (int num : arr) {
            countMap[num]++;
        }

        unordered_set<int> occurrencesSet; // 設定儲存唯一出現次數
        for (auto& it : countMap) {
            // 如果我們無法插入它，則存在重複出現計數
            if (!occurrencesSet.insert(it.second).second) {
                return false;
            }
        }

        return true;
    }
};