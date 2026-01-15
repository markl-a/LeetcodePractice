"""
2375. Construct Smallest Number From DI String

Difficulty: Medium
Topics: String, Backtracking, Stack, Greedy

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = []
        used = [False] * 10  

        def backtrack(index: int, current_num: int):


            if index == n + 1:  
                return True

            if index == 0: 
                for i in range(1, 10):
                    if not used[i]:
                        used[i] = True
                        res.append(str(i))
                        if backtrack(index + 1, i):
                            return True
                        used[i] = False  
                        res.pop()
                return False


            if pattern[index - 1] == 'I':
                for next_num in range(current_num + 1, 10):  
                    if not used[next_num]:
                        used[next_num] = True
                        res.append(str(next_num))
                        if backtrack(index + 1, next_num):
                            return True
                        used[next_num] = False  
                        res.pop()

            else:  # pattern[index - 1] == 'D'
                for next_num in range(1, current_num):  
                    if not used[next_num]:
                        used[next_num] = True
                        res.append(str(next_num))
                        if backtrack(index + 1, next_num):
                            return True
                        used[next_num] = False  
                        res.pop()

            return False  

        backtrack(0, 0)  
        return "".join(res)
