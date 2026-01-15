"""
2095. Delete the Middle Node of a Linked List

Difficulty: Medium
Topics: Linked List, Two Pointers

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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果只有一個節點，返回 None
        if not head or not head.next:
            return None

        # 定義快慢指針
        slow = head
        fast = head
        prev = None

        # 快指針每次移動兩步，慢指針每次移動一步
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # 刪除中間節點
        if prev:
            prev.next = slow.next

        return head
