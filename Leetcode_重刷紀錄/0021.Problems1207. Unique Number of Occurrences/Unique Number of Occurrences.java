import java.util.HashMap;
import java.util.HashSet;

class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> countMap = new HashMap<>();
        for (int num : arr) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        HashSet<Integer> occurrencesSet = new HashSet<>();
        for (int count : countMap.values()) {
            if (!occurrencesSet.add(count)) {
                // 如果無法添加，表示有重複的出現次數
                return false;
            }
        }

        return true;
    }
}
