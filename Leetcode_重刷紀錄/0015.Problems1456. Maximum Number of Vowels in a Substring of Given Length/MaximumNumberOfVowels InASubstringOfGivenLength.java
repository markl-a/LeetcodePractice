//1456. Maximum Number of Vowels in a Substring of Given Length
/* 這邊是實作sliding window 的方法，實現方式類似雙指針，不過主要裝的是同一區域的數值
*/

class Solution {
    public int maxVowels(String s, int k) {
        int vowels = 0,i=0;
        int [] asciiVo =new int[123];
        asciiVo['a']=1;
        asciiVo['e']=1;
        asciiVo['u']=1;
        asciiVo['i']=1;
        asciiVo['o']=1;
        
        do {
            vowels+= asciiVo[s.charAt(i)];            
        }while(++i < k);
        
        int maxVowels = vowels;
        
        while (i < s.length()) {
            vowels+= asciiVo[s.charAt(i)] - asciiVo[s.charAt(i - k)];
            maxVowels = Math.max(maxVowels, vowels);
            i++;
        }    
        return maxVowels;
    }
}


