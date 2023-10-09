public class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder result = new StringBuilder();
        int i = 0, len1 = word1.length(), len2 = word2.length();
        int maxLen = Math.max(len1, len2);  // 新宣告的參數
        
        while (i < maxLen) {
            if (i < len1) {
                result.append(word1.charAt(i));
            }
            if (i < len2) {
                result.append(word2.charAt(i));
            }
            i++;
        }
        
        return result.toString();
    }
}