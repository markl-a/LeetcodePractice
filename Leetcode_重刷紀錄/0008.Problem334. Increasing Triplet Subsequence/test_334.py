"""Tests for LeetCode 334. Increasing Triplet Subsequence"""

import pytest
from pathlib import Path
import importlib.util

_solution_path = Path(__file__).parent / "solution.py"
_spec = importlib.util.spec_from_file_location("solution_334", _solution_path)
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)

Solution = _solution.Solution
SolutionMinMax = _solution.SolutionMinMax


class TestIncreasingTriplet:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize(
        "nums,expected",
        [
            ([1, 2, 3, 4, 5], True),
            ([5, 4, 3, 2, 1], False),
            ([2, 1, 5, 0, 4, 6], True),
            ([1, 2], False),
            ([1, 1, 1], False),
            ([1, 2, 3], True),
            ([1, 5, 0, 4, 1, 3], True),
            ([20, 100, 10, 12, 5, 13], True),
            ([1, 1, 1, 1, 1], False),
            ([5, 1, 6], False),
            ([1, 2, 1, 2, 1, 2, 1, 2], False),
            ([1, 2, 2, 1], False),
            ([0, 4, 2, 1, 0, -1, -3], False),
        ],
    )
    def test_increasing_triplet(self, solution, nums, expected):
        assert solution.increasingTriplet(nums) == expected

    def test_both_solutions_consistent(self):
        sol1, sol2 = Solution(), SolutionMinMax()
        test_cases = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 1, 5, 0, 4, 6], [1, 2], [1, 5, 0, 4, 1, 3]]
        for nums in test_cases:
            assert sol1.increasingTriplet(nums) == sol2.increasingTriplet(nums)
