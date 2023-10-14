//392. Is Subsequence
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i=0,j = 0;
        while (i < t.size()) {
            if (s[j] == t[i]) {
                j++;
                if(j >= s.size()){
                    break;
                }
            }
            ++i;
        }
        return j == s.size();
    }
};

//一點小修改
class Solution {
public:
    bool isSubsequence(string s, string t) {
        if(s.size()==0){
            return true;
        }
        int i=0,j = 0;
        while (i < t.size()) {
            if (s[j] == t[i]) {
                j++;
                if(j >= s.size()){
                    return true;
                }
            }
            ++i;
        }
        return false;
        
        
    }
};

