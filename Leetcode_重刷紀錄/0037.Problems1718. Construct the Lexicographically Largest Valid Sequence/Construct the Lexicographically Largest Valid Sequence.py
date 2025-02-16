class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2 * n - 1)
        used = [False] * (n + 1)  # used[i] 表示數字 i 是否已經被使用過

        def backtrack(index: int) -> bool:
            if index == len(ans):
                return True  # 找到一個合法的序列

            if ans[index] != 0:  # 目前位置已經填過數字了，直接跳到下一個位置
                return backtrack(index + 1)

            for num in range(n, 0, -1):  # 從大到小嘗試數字
                if not used[num]:
                    used[num] = True
                    ans[index] = num

                    if num == 1:
                        if backtrack(index + 1):
                            return True
                    else:
                        next_pos = index + num
                        if next_pos < len(ans) and ans[next_pos] == 0:
                            ans[next_pos] = num
                            if backtrack(index + 1):
                                return True
                            ans[next_pos] = 0  # 回溯：撤銷選擇

                    ans[index] = 0      # 回溯：撤銷選擇
                    used[num] = False

            return False  # 目前位置嘗試了所有數字都無法得到合法序列

        backtrack(0)
        return ans