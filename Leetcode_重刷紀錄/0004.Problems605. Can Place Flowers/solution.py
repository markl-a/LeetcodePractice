"""
605. Can Place Flowers

Difficulty: Easy
Topics: Array, Greedy

Problem:
You have a long flowerbed in which some of the plots are planted, and some are not. However,
flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule and false otherwise.

Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

Constraints:
    - 1 <= flowerbed.length <= 2 * 10^4
    - flowerbed[i] is 0 or 1
    - There are no two adjacent flowers in flowerbed
    - 0 <= n <= flowerbed.length
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Determines if n flowers can be planted following the no-adjacent rule.

        Time Complexity: O(len(flowerbed))
        Space Complexity: O(1) - modifies input in place

        Args:
            flowerbed: Array representing the flowerbed (0 = empty, 1 = occupied)
            n: Number of flowers to plant

        Returns:
            True if n flowers can be planted, False otherwise
        """
        count = 0

        for i in range(len(flowerbed)):
            # Check if current position is empty
            if flowerbed[i] == 0:
                # Check left neighbor (empty if i == 0)
                left_empty = i == 0 or flowerbed[i - 1] == 0
                # Check right neighbor (empty if i == len - 1)
                right_empty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

                # If both neighbors are empty, we can plant here
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1

                    # Early termination if we've planted enough
                    if count >= n:
                        return True

        return count >= n


class SolutionNonModifying:
    """Solution that doesn't modify the input array"""

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Determines if n flowers can be planted without modifying input.

        Time Complexity: O(len(flowerbed))
        Space Complexity: O(1)
        """
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = i == 0 or flowerbed[i - 1] == 0
                right_empty = i == length - 1 or flowerbed[i + 1] == 0

                if left_empty and right_empty:
                    count += 1
                    # Mark as planted for future iterations
                    # We need to pretend we planted, so skip next position
                    if i < length - 1:
                        # Create a copy for this iteration
                        flowerbed = flowerbed.copy()
                        flowerbed[i] = 1

                    if count >= n:
                        return True

        return count >= n


class SolutionCopy:
    """Solution that makes a copy to preserve original input"""

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Determines if n flowers can be planted using a copy of the array.

        Time Complexity: O(len(flowerbed))
        Space Complexity: O(len(flowerbed)) for the copy
        """
        bed = flowerbed.copy()
        count = 0

        for i in range(len(bed)):
            if bed[i] == 0:
                left_empty = i == 0 or bed[i - 1] == 0
                right_empty = i == len(bed) - 1 or bed[i + 1] == 0

                if left_empty and right_empty:
                    bed[i] = 1
                    count += 1

                    if count >= n:
                        return True

        return count >= n
