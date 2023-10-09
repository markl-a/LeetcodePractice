lass Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result;
        int len1 = word1.size(), len2 = word2.size(),resultlen=len1+len2;
        result.reserve(len1 + len2);  // 預分配記憶體
        
        int i = 0, j = 0;
        while (i + j< resultlen) {
            if (i < len1) {
                result.push_back(word1[i++]);
            }
            if (j < len2) {
                result.push_back(word2[j++]);
            }
        }
        return result;
    }
};