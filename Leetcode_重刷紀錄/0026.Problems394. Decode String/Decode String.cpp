class Solution {
public:
    string decodeString(string s) {
      stack<string> chars; // 用來儲存字母
        stack<int> counts; // 用來儲存數字
        string res = ""; // 當前處理的結果字符串
        int idx = 0; // 當前解析到的字符串的索引
        
        while (idx < s.length()) {
            if (isdigit(s[idx])) {
                int count = 0;
                // 讀取整個數字
                while (isdigit(s[idx])) {
                    count = 10 * count + (s[idx] - '0');
                    idx++;
                }
                counts.push(count);
            } else if (s[idx] == '[') {
                // 推入目前的res到棧，並重置res
                chars.push(res);
                res = "";
                idx++;
            } else if (s[idx] == ']') {
                string temp = chars.top(); chars.pop();
                int repeatTimes = counts.top(); counts.pop();
                // 重複res指定的次數，並與temp拼接
                for (int i = 0; i < repeatTimes; i++) {
                    temp += res;
                }
                res = temp;
                idx++;
            } else {
                // 正常字符，加入到res中
                res += s[idx];
                idx++;
            }
        }
        
        return res;  
    }
};

/////

class Solution {
public:
    string decodeString(string s) {
        int pos = 0;
        return helper(pos, s);
    }
    
    string helper(int& pos, const string& s) {
        stringstream word; // 使用 stringstream 来拼接字符串
        int num = 0;
        while (pos < s.size()) {
            char cur = s[pos];
            if (cur == '[') {
                string curStr = helper(++pos, s);
                for (; num > 0; num--) word << curStr;
            } else if (isdigit(cur)) {
                num = num * 10 + cur - '0';
            } else if (cur == ']') {
                return word.str();
            } else {    // Normal characters
                word << cur;
            }
            ++pos;
        }
        return word.str();
    }
};