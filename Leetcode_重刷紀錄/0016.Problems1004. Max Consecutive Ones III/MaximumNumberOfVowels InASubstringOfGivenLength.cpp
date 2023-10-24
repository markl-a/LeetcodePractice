//1456. Maximum Number of Vowels in a Substring of Given Length
/* 這邊是實作sliding window 的方法，實現方式類似雙指針，不過主要裝的是同一區域的數值
*/
class Solution {
public:
    int maxVowels(string s, int k) {
        int vowels = 0,i=0 ;
        do {
            vowels+=isVowel(s[i]);
        } while(++i < k );        
        int maxVowels = vowels;
        while(i < s.length()) {
            vowels += (isVowel(s[i])) -(isVowel(s[i-k]));        
            maxVowels = max(maxVowels, vowels);
            ++i;
        }        
        return maxVowels;
    }
    
private:
    bool isVowel(char c) {
        return c=='a' || c=='e' || c=='i' || c=='o' || c=='u';
        /*
        switch(c){
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
                return true;
            default :
                return false;
        } */
    }
};


