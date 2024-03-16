class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 統計列表中每個數字出現的次數
        occurrences = Counter(arr)
        # 檢查每個數字出現的次數是否唯一
        return len(occurrences.values()) == len(set(occurrences.values()))