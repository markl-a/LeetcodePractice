//別人的最優解，我想不到更快的
class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        int count = 0;
        set<vector<int>> res;
        unordered_map<int, vector<int>> dupe;

        for(int i = 0; i < grid.size(); ++i){
            if(res.find(grid[i]) != res.end()) {
                dupe[i] = grid[i];
                //如果該行已經存在，那麼如果有重複，則必須多次計數
            } 
            res.insert(grid[i]);
        }
        for(int i = 0; i < grid.size(); ++i){
            vector<int> temp;
            for(int j = 0; j <  grid.size(); ++j){
                temp.push_back(grid[j][i]);
            }
            if(res.find(temp) != res.end()) {
                for(auto& it: dupe){
                //透過 dupe unordered_map 進行迭代以新增重複行
                    if(it.second == temp){
                        ++count;
                    }
                }
                ++count;
                cout << i << " ";
            } 
        }


        return count;
    }
};