class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 檢查兩個單詞是否具有相同的唯一字符集
        if set(word1) != set(word2):
            return False

        # 使用Counter來計算每個字母的出現頻率
        count1, count2 = Counter(word1), Counter(word2)
        
        # 比較兩個單詞中各字母出現頻率的集合是否相同
        return sorted(count1.values()) == sorted(count2.values())