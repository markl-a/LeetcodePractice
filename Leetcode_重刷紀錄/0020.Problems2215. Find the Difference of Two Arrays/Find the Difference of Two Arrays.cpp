#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        // 使用unordered_set分別存儲兩個向量的元素，以去除重複元素並提高查找效率
        unordered_set<int> set1(nums1.begin(), nums1.end()), set2(nums2.begin(), nums2.end());

        // 分別為nums1和nums2初始化結果向量
        vector<vector<int>> ans(2);
        
        // 查找在nums1中但不在nums2中的元素
        for (int num : set1) {
            if (!set2.count(num)) {
                ans[0].push_back(num);
            }
        }
        
        // 查找在nums2中但不在nums1中的元素
        for (int num : set2) {
            if (!set1.count(num)) {
                ans[1].push_back(num);
            }
        }
        
        return ans;
    }
};
