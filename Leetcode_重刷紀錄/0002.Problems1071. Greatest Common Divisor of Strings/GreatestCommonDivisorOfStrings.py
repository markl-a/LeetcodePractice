# Greatest Common Divisor of Strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)  # 保證 str1 不比 str2 短
        if not str1.startswith(str2):
            return ""  # 如果 str1 不以 str2 開頭，則它們不可能有公共前綴
        if not str2:
            return str1
        return self.gcdOfStrings(str1[len(str2):], str2)
    
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

# 使用內建函數的優化版本

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:math.gcd(len(str1), len(str2))]

