//1431. Kids With the Greatest Number of Candies

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int maxNum = *std::max_element(candies.begin(), candies.end());
        std::vector<bool> Ans;

        for (int num : candies) {
            Ans.push_back(num + extraCandies >= maxNum);
        }

        return Ans;
    }
};