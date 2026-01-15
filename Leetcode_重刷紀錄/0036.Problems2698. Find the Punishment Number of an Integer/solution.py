"""
2698. Find the Punishment Number of an Integer

Difficulty: Medium
Topics: Math, Backtracking

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    _punishment_numbers = []  # 類變數，儲存預先計算的懲罰數的平方

    def __init__(self):
        if not Solution._punishment_numbers:  # 僅在第一次創建 Solution 實例時計算
            self._precompute_punishment_numbers()

    def _precompute_punishment_numbers(self):
        def is_punishment_number(i: int) -> bool:
            square_str = str(i * i)
            square_len = len(square_str)

            def backtrack(index: int, current_sum: int) -> bool:
                if index == square_len:
                    return current_sum == i
                if current_sum > i:
                    return False
                for j in range(index + 1, square_len + 1):
                    substring = square_str[index:j]
                    substring_num = int(substring)
                    if substring_num > i:
                        continue
                    if backtrack(j, current_sum + substring_num):
                        return True
                return False

            return backtrack(0, 0)

        Solution._punishment_numbers = [i * i for i in range(1, 1001) if is_punishment_number(i)]

    def punishmentNumber(self, n: int) -> int:
        total_punishment_sum = 0
        for pn_squared in Solution._punishment_numbers:
            if pn_squared > n * n:
                break  # 提前終止，因為懲罰數的平方已經超過 n*n

            pn = int(pn_squared**0.5) # 開根號回去
            if pn <= n:  # 檢查開根號後的懲罰數本身是否在 1 到 n 的範圍內
              total_punishment_sum += pn_squared
        return total_punishment_sum
