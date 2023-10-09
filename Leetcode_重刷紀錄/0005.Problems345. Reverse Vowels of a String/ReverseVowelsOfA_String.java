// 345. Reverse Vowels of a String
import java.util.HashSet;
import java.util.Set;

public class Solution {
    public String reverseVowels(String s) {
        char[] chars = s.toCharArray();
        int i = 0, j = s.length() - 1;
        String vowels = "aeiouAEIOU";
        
        while (i < j) {
            while (i < j && vowels.indexOf(chars[i]) == -1) {
                i++;
            }
            while (i < j && vowels.indexOf(chars[j]) == -1) {
                j--;
            }
            char temp = chars[i];
            chars[i] = chars[j];
            chars[j] = temp;
            i++;
            j--;
        }
        
        return new String(chars);
    }
}
