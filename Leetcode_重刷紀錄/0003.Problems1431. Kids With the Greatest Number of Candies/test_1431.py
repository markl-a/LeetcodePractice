"""Tests for LeetCode 1431. Kids With the Greatest Number of Candies"""

import pytest
from pathlib import Path
import importlib.util

# Dynamic import to avoid module name conflicts
_solution_path = Path(__file__).parent / "solution.py"
_spec = importlib.util.spec_from_file_location("solution_1431", _solution_path)
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)

Solution = _solution.Solution
SolutionExplicit = _solution.SolutionExplicit
SolutionOnePass = _solution.SolutionOnePass


class TestKidsWithCandies:
    """Test cases for kidsWithCandies method"""

    @pytest.fixture
    def solution(self):
        """Create Solution instance"""
        return Solution()

    @pytest.fixture
    def solution_explicit(self):
        """Create SolutionExplicit instance"""
        return SolutionExplicit()

    @pytest.fixture
    def solution_one_pass(self):
        """Create SolutionOnePass instance"""
        return SolutionOnePass()

    @pytest.mark.parametrize(
        "candies,extra_candies,expected",
        [
            # Example test cases
            ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
            ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
            ([12, 1, 12], 10, [True, False, True]),
            # Edge cases - all kids can have max
            ([1, 1, 1], 5, [True, True, True]),
            ([5, 5, 5], 0, [True, True, True]),
            # Edge cases - only one kid can have max
            ([10, 1, 1], 0, [True, False, False]),
            ([1, 2, 3], 0, [False, False, True]),
            # Minimum size (n = 2)
            ([5, 10], 5, [True, True]),
            ([5, 10], 4, [False, True]),
            # Large extra candies
            ([1, 2, 3], 100, [True, True, True]),
            # All same except one
            ([5, 5, 5, 10], 5, [True, True, True, True]),
            ([5, 5, 5, 10], 4, [False, False, False, True]),
            # Sequential candies
            ([1, 2, 3, 4, 5], 5, [True, True, True, True, True]),
            ([1, 2, 3, 4, 5], 3, [False, True, True, True, True]),
            ([1, 2, 3, 4, 5], 0, [False, False, False, False, True]),
            # Random larger cases
            ([10, 20, 30, 15, 25], 10, [False, True, True, False, True]),
            ([100, 1, 50, 99], 50, [True, False, True, True]),
            # All kids have same candies
            ([7, 7, 7, 7], 3, [True, True, True, True]),
            # Large numbers
            ([99, 100, 98, 97], 50, [True, True, True, True]),
            ([99, 100, 98, 97], 0, [False, True, False, False]),
            # Extra candies exactly match the difference
            ([5, 10], 5, [True, True]),
            ([5, 11], 5, [False, True]),
        ],
    )
    def test_kids_with_candies(self, solution, candies, extra_candies, expected):
        """Test kidsWithCandies with various inputs"""
        assert solution.kidsWithCandies(candies, extra_candies) == expected

    def test_all_solutions_consistent(self):
        """Ensure all solutions produce the same results"""
        sol1 = Solution()
        sol2 = SolutionExplicit()
        sol3 = SolutionOnePass()

        test_cases = [
            ([2, 3, 5, 1, 3], 3),
            ([4, 2, 1, 1, 2], 1),
            ([12, 1, 12], 10),
            ([1, 1, 1], 5),
            ([10, 20, 30], 15),
        ]

        for candies, extra in test_cases:
            result1 = sol1.kidsWithCandies(candies, extra)
            result2 = sol2.kidsWithCandies(candies, extra)
            result3 = sol3.kidsWithCandies(candies, extra)
            assert (
                result1 == result2 == result3
            ), f"Solutions differ for ({candies}, {extra})"

    def test_result_length_matches_input(self, solution):
        """Test that result length always matches input length"""
        test_cases = [
            ([1, 2], 1),
            ([1, 2, 3, 4, 5], 10),
            ([10] * 100, 5),
        ]

        for candies, extra in test_cases:
            result = solution.kidsWithCandies(candies, extra)
            assert len(result) == len(candies)

    def test_at_least_one_true(self, solution):
        """Test that at least one kid can have the maximum (given enough extra candies)"""
        test_cases = [
            ([1, 2, 3], 100),
            ([5, 10, 15], 50),
            ([1, 1, 1], 0),
        ]

        for candies, extra in test_cases:
            result = solution.kidsWithCandies(candies, extra)
            assert any(result), f"No True in result for ({candies}, {extra})"
