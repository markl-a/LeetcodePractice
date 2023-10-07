//Greatest Common Divisor of Strings

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 != str2 + str1) {
            return "";
        }
        return str1.substr(0, gcd(str1.size(), str2.size()));
    }
    
    int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
};

//下面是直接使用C++ 內建的 C++ 標準程式庫（Standard Library）

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        return (str1 + str2 == str2 + str1)? str1.substr(0, gcd(size(str1),size(str2))): "";
    }
};
