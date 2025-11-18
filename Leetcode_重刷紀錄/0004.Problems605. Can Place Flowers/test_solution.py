"""Tests for LeetCode 605. Can Place Flowers"""

import pytest
from solution import Solution, SolutionNonModifying, SolutionCopy


class TestCanPlaceFlowers:
    """Test cases for canPlaceFlowers method"""

    @pytest.fixture
    def solution(self):
        """Create Solution instance"""
        return Solution()

    @pytest.fixture
    def solution_non_modifying(self):
        """Create SolutionNonModifying instance"""
        return SolutionNonModifying()

    @pytest.fixture
    def solution_copy(self):
        """Create SolutionCopy instance"""
        return SolutionCopy()

    @pytest.mark.parametrize(
        "flowerbed,n,expected",
        [
            # Example test cases
            ([1, 0, 0, 0, 1], 1, True),
            ([1, 0, 0, 0, 1], 2, False),
            # Edge cases - single element
            ([0], 1, True),
            ([1], 0, True),
            ([1], 1, False),
            ([0], 2, False),
            # Edge cases - two elements
            ([0, 0], 1, True),
            ([0, 0], 2, False),
            ([1, 0], 0, True),
            ([1, 0], 1, False),
            ([0, 1], 1, False),
            # Edge cases - n = 0
            ([1, 0, 1], 0, True),
            ([0, 0, 0], 0, True),
            # All empty
            ([0, 0, 0], 2, True),
            ([0, 0, 0, 0, 0], 3, True),
            ([0, 0, 0, 0, 0], 4, False),
            # All occupied
            ([1, 1, 1], 0, True),
            ([1, 1, 1], 1, False),
            # Alternating pattern
            ([1, 0, 1, 0, 1], 0, True),
            ([1, 0, 1, 0, 1], 1, False),
            # Can plant at beginning
            ([0, 0, 1], 1, True),
            ([0, 0, 1, 0, 0], 2, True),
            # Can plant at end
            ([1, 0, 0], 1, True),
            ([1, 0, 0, 0], 1, True),
            # Multiple valid positions
            ([0, 0, 0, 0, 0, 0, 0], 3, True),
            ([0, 0, 0, 0, 0, 0, 0], 4, True),
            ([0, 0, 0, 0, 0, 0, 0], 5, False),
            # Complex patterns
            ([1, 0, 0, 0, 0, 1], 2, False),
            ([1, 0, 0, 0, 1, 0, 0], 2, True),
            ([0, 1, 0, 1, 0, 1, 0], 0, True),
            ([0, 1, 0, 1, 0, 1, 0], 1, False),
            # Long sequences
            ([0] * 10, 5, True),
            ([0] * 10, 6, True),
            ([0] * 10, 7, False),
            # Mixed patterns
            ([1, 0, 0, 0, 0, 0, 1, 0, 0], 2, True),
            ([1, 0, 0, 0, 0, 0, 1, 0, 0], 3, False),
            ([0, 0, 1, 0, 0, 1, 0, 0], 3, True),
            # Exact match
            ([0, 0, 0, 0, 0], 3, True),
            ([0, 1, 0, 0, 0, 1, 0, 0], 2, True),
        ],
    )
    def test_can_place_flowers(self, solution, flowerbed, n, expected):
        """Test canPlaceFlowers with various inputs"""
        # Create a copy since solution modifies in place
        flowerbed_copy = flowerbed.copy()
        assert solution.canPlaceFlowers(flowerbed_copy, n) == expected

    def test_all_solutions_consistent(self):
        """Ensure all solutions produce the same results"""
        sol1 = Solution()
        sol2 = SolutionNonModifying()
        sol3 = SolutionCopy()

        test_cases = [
            ([1, 0, 0, 0, 1], 1),
            ([1, 0, 0, 0, 1], 2),
            ([0, 0, 0], 2),
            ([1, 0, 1], 0),
            ([0] * 10, 5),
        ]

        for flowerbed, n in test_cases:
            result1 = sol1.canPlaceFlowers(flowerbed.copy(), n)
            result2 = sol2.canPlaceFlowers(flowerbed.copy(), n)
            result3 = sol3.canPlaceFlowers(flowerbed.copy(), n)
            assert (
                result1 == result2 == result3
            ), f"Solutions differ for ({flowerbed}, {n})"

    def test_original_preserved_with_copy_solution(self):
        """Test that SolutionCopy preserves the original array"""
        sol = SolutionCopy()
        original = [1, 0, 0, 0, 1]
        original_copy = original.copy()

        sol.canPlaceFlowers(original, 1)

        assert original == original_copy, "Original array was modified"

    def test_greedy_approach_optimal(self, solution):
        """Test that greedy approach gives optimal solution"""
        # In a greedy approach, we should plant as soon as possible
        # This should give us the maximum number of flowers
        test_cases = [
            ([0, 0, 0, 0, 0], 3),  # Can plant at 0, 2, 4
            ([0, 0, 0, 0, 0, 0, 0], 4),  # Can plant at 0, 2, 4, 6
        ]

        for flowerbed, n in test_cases:
            assert solution.canPlaceFlowers(flowerbed.copy(), n) == True
