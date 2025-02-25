class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(curr, openCount, closeCount):
            # 若組合長度達到 2*n，代表生成完畢
            if len(curr) == 2 * n:
                ans.append("".join(curr))
                return
            
            # 若可放左括號，繼續放
            if openCount < n:
                curr.append("(")
                backtrack(curr, openCount + 1, closeCount)
                curr.pop()  # 回溯

            # 若可放右括號，繼續放
            if closeCount < openCount:
                curr.append(")")
                backtrack(curr, openCount, closeCount + 1)
                curr.pop()  # 回溯

        backtrack([], 0, 0)
        return ans


