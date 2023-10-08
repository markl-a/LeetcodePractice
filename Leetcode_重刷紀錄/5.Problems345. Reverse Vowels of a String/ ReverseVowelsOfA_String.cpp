// 345. Reverse Vowels of a String
//根據 chatgpt 給的修改, 但是跑得比較慢 記憶體佔用也很多
class Solution {
    public:
        string reverseVowels(string s) {
            int i = 0, j = s.size() - 1;
            string vowels = "aeiouAEIOU";    
            while (i < j) {
                while( vowels.find(s[i]) == string::npos && i < j) ++i;
                while( vowels.find(s[j]) == string::npos && i < j) --j;
                swap(s[i++], s[j--]);
            }     
            return s;
        }
    };

// 別人的程式碼 ,寫的很土砲但是跑得超快,記憶體佔用也比上面的程式碼少
class Solution {
public:
    bool isVowel(char c)
    {
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
        or c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') return true;
        return false;
    }
    string reverseVowels(string s) {
        int left=0,right = s.length()-1;
        while(left < right)
        {
            while(left < right && !isVowel(s[left]))
            {
                left++;
            }
            while(right > left && !isVowel(s[right]))
            {
                 right--;
            }
            if(isVowel(s[left]) && isVowel(s[right]))
            {
                char temp = s[left];
                s[left] = s[right];
                s[right] = temp;
                left++;
                right--;
            }
            else break;
        }
        return s;
    }
};
// 結合上面的修改版,這邊跑的還是沒有上面快,是swap那邊多佔了點時間，假如那邊沒做判斷的話，會多跑幾個迴圈

class Solution {
    public:
        bool notVowel(char c)
        {
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
        or c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') return false;
        return true;
        }
        string reverseVowels(string s) {
            int i = 0, j = s.size() - 1;    
            while (i < j) {
                while( notVowel(s[i]) && i < j) ++i;
                while( notVowel(s[j]) && i < j) --j;
                if(!notVowel(s[i])&&!notVowel(s[j]))
                swap(s[i], s[j]);
                i++,j--;

            }     
            return s;
        }
    };