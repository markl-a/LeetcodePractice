"""
735. Asteroid Collision

Difficulty: Medium
Topics: Array, Stack, Simulation

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for astro in asteroids: 
            if astro > 0:
                stk.append(astro)
            else:
                while(stk and stk[-1]>0):
                    if (abs(astro) > stk[-1]):
                        stk.pop()
                    elif (abs(astro) == stk[-1]):
                        stk.pop()
                        break
                    else:
                        break
                else:
                    stk.append(astro)
                
        return (stk)
