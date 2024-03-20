class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stack;  // 使用vector來模擬棧
        for (int ast : asteroids) {
            bool isAlive = true;
            // 只有當當前小行星向左移動，且棧頂小行星向右移動時，才需要處理碰撞
            while (!stack.empty() && ast < 0 && stack.back() > 0) {
                if (stack.back() < -ast) {  // 如果棧頂小行星小於當前小行星的絕對值
                    stack.pop_back();  // 棧頂小行星被摧毀
                    continue;
                } else if (stack.back() == -ast) {  // 如果兩個小行星大小相同
                    stack.pop_back();  // 兩者都被摧毀
                }
                isAlive = false;  // 當前小行星被摧毀
                break;
            }
            if (isAlive) {  // 如果當前小行星存活（未發生碰撞或成功摧毀所有遇到的小行星）
                stack.push_back(ast);  // 將其加入棧中
            }
        }
        return stack;        
    }
};