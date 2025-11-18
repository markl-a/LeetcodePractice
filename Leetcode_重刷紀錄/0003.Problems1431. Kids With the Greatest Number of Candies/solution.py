"""
1431. Kids With the Greatest Number of Candies

Difficulty: Easy
Topics: Array, Simulation

Problem:
There are n kids with candies. You are given an integer array candies, where each candies[i]
represents the number of candies the ith kid has, and an integer extraCandies, denoting the
number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid
all the extraCandies, they will have the greatest number of candies among all the kids, or false
otherwise.

Note that multiple kids can have the greatest number of candies.

Example 1:
    Input: candies = [2,3,5,1,3], extraCandies = 3
    Output: [true,true,true,false,true]
    Explanation: If you give all extraCandies to:
    - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest.
    - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest.
    - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest.
    - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest.
    - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest.

Example 2:
    Input: candies = [4,2,1,1,2], extraCandies = 1
    Output: [true,false,false,false,false]

Example 3:
    Input: candies = [12,1,12], extraCandies = 10
    Output: [true,false,true]

Constraints:
    - n == candies.length
    - 2 <= n <= 100
    - 1 <= candies[i] <= 100
    - 1 <= extraCandies <= 50
"""

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Determines which kids can have the most candies after receiving extra candies.

        Time Complexity: O(n) where n = len(candies)
        Space Complexity: O(n) for the result list

        Args:
            candies: List of candy counts for each kid
            extraCandies: Number of extra candies to distribute

        Returns:
            Boolean list indicating if each kid can have the maximum candies
        """
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]


class SolutionExplicit:
    """Alternative solution with explicit loop for clarity"""

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Determines which kids can have the most candies using explicit loop.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        max_candies = max(candies)
        result = []

        for candy in candies:
            result.append(candy + extraCandies >= max_candies)

        return result


class SolutionOnePass:
    """Solution that calculates max in the same pass (less efficient but demonstrates concept)"""

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Alternative approach calculating threshold.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Calculate the minimum candies needed to be the greatest
        threshold = max(candies) - extraCandies

        # Check if each kid's candies meet the threshold
        return [candy >= threshold for candy in candies]
