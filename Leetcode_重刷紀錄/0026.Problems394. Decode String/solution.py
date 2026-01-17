"""
394. Decode String

Difficulty: Medium
Topics: String, Stack, Recursion

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                # 建立目前數字（可以是多位數字）
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # 將目前數字和字串壓入堆疊
                stack.append((current_string, current_num))
                # 重置新的子字串
                current_string = ""
                current_num = 0
            elif char == ']':
                # 從堆疊中彈出以獲取前一個字串並重複計數
                last_string, repeat_times = stack.pop()
                # 將目前重複的字串'repeat_times'追加到'last_string'
                current_string = last_string + current_string * repeat_times
            else:
                # 將字元累加到目前字串
                current_string += char

        return current_string
