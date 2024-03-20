class Solution:
    def removeStars(self, s: str) -> str:
        wIdx = 0  # 記錄下一個要寫入的位置索引
        s_list = list(s)  # 將字符串轉換成列表，因為Python的字符串是不可變的
        
        for c in s:
            if c != '*':
                s_list[wIdx] = c
                wIdx += 1  # 寫入字符，同時遞增wIdx
            else:
                wIdx -= 1  # 如果有前一個字符，則將wIdx遞減
        
        return ''.join(s_list[:wIdx])  # 返回前wIdx個字符

# 使用stack

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []  # 使用列表模擬棧的行為
        for char in s:
            if char == '*':
                if stack:  # 確保棧不為空
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
