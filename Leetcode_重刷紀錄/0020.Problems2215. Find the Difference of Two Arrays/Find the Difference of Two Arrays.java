import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;

class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        for (int num : nums1) {
            set1.add(num);
        }

        Set<Integer> set2 = new HashSet<>();
        for (int num : nums2) {
            set2.add(num);
        }

        List<List<Integer>> ans = new ArrayList<>();
        ans.add(new ArrayList<>()); // 对于nums1中独有的元素
        ans.add(new ArrayList<>()); // 对于nums2中独有的元素

        // 查找在nums1中但不在nums2中的元素，并从set1中移除已经处理过的元素
        for (int num : nums1) {
            if (set2.contains(num)) {
                set1.remove(num);
                set2.remove(num);
            }
        }

        // 添加剩余在set1中的元素到结果列表
        for (int num : set1) {
            ans.get(0).add(num);
        }

        // 添加剩余在set2中的元素到结果列表
        for (int num : nums2) {
            if (set1.contains(num)) {
                set2.remove(num);
            } else if (set2.contains(num)) {
                ans.get(1).add(num);
                set2.remove(num);
            }
        }

        return ans;
    }
}
