"""
2130. Maximum Twin Sum of a Linked List

Difficulty: Medium
Topics: Linked List, Two Pointers, Stack

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 第一步：快慢指標尋找中點
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 第二步：反轉 slow 之後的串列 (後半部)
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 反轉後，prev 就是「後半段反轉後」的起始節點
        # 第三步：配對計算最大和
        max_sum = 0
        p1 = head
        p2 = prev
        while p2:  # p2 走到底就結束
            max_sum = max(max_sum, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
        
        return max_sum
