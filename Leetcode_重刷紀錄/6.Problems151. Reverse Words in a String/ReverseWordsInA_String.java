// 151. Reverse Words in a String
class Solution {
    public String reverseWords(String s) {
        // Trim the input string to remove leading and trailing spaces
        String[] str = s.trim().split("\\s+");

        // Initialize the output string
        s = "";
        int i = str.length - 1;

        // Iterate through the words in reverse order
        while (i > 0) {
            // Append the current word and a space to the output
            s += str[i--] + " ";
        }

        // Append the first word to the output (without trailing space)
        return s + str[0];
    }
}

import java.util.stream.Collectors;
import java.util.Arrays;

public class Solution {
    public String reverseWords(String s) {
       // Split the string by spaces
        List<String> words = Arrays.asList(s.trim().split("\\s+"));
        
        // Reverse the list of words
        Collections.reverse(words);
        
        // Join the words back together
        return String.join(" ", words);
    }
}
