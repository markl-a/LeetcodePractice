//Greatest Common Divisor of Strings

import java.math.BigInteger;

public class Solution {
    public String gcdOfStrings(String str1, String str2) {
        return ((str1 + str2).equals(str2 + str1))? str1.substring(0, BigInteger.valueOf(str1.length()).gcd(BigInteger.valueOf(str2.length())).intValue()):"";
    }
}

//下面為不使用遞歸的版本

public class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if (str1.length() < str2.length()) {
            return gcdOfStrings(str2, str1);  // 保證 str1 不比 str2 短
        }
        if (!str1.startsWith(str2)) {
            return "";  // 如果 str1 不以 str2 開頭，則它們不可能有公共前綴
        }
        if (str2.isEmpty()) {
            return str1;
        }
        return gcdOfStrings(str1.substring(str2.length()), str2);
    }
    
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}