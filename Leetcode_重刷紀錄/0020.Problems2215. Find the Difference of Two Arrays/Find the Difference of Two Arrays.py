class Solution:
     def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
         # 將清單轉換為集合移除重複元素，並且方便後續操作
         set1, set2 = set(nums1), set(nums2)

         # 使用集合的差集運算來找到僅存在於一個集合中的元素
         unique_to_nums1 = set1 - set2
         unique_to_nums2 = set2 - set1

         # 將結果轉換為清單格式並傳回
         return [list(unique_to_nums1), list(unique_to_nums2)]