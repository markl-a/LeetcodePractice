//別人寫的最易於理解的，但最慢
class Solution {
public:
    string removeStars(string s) {
      string st = "";
        for (auto ch : s) {
            if (ch == '*') {
                st.pop_back();
            } else {
                st += ch;
            }
        }
        return st;  
    }
};

//相對較快,記憶體也用得少的
class Solution {
public:
    string removeStars(string s) {
        int wIdx = 0;  // 記錄下一個要寫入的位置索引
        for (char c : s) {
            if (c != '*') {
                s[wIdx++] = c;  // 寫入字元,同時遞增 wIdx
            } else {
                wIdx--;  // 如果有前一個字元,則將 wIdx 遞減
            }
        }
        return s.substr(0, wIdx);  // 返回前 wIdx 個字元
    }
};