// 443. String Compression
class Solution {
public:
    int compress(vector<char>& chars) {
        int write = 0, read = 0;
        
        while (read < chars.size()) {
            char currentChar = chars[read];
            int count = 0;
            
            while (read < chars.size() && chars[read] == currentChar) {
                read++;
                count++;
            }
            
            chars[write++] = currentChar;
            
            if (count > 1) {
                for (char c : to_string(count)) {
                    chars[write++] = c;
                }
            }
        }
        
        return write;
    }
};
