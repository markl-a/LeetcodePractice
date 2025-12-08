"""Tests for LeetCode 11. Container With Most Water"""

import pytest
from pathlib import Path
import importlib.util

_solution_path = Path(__file__).parent / "solution.py"
_spec = importlib.util.spec_from_file_location("solution_11", _solution_path)
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)

Solution = _solution.Solution


class TestMaxArea:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize(
        "height,expected",
        [
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
            ([1, 1], 1),
            ([4, 3, 2, 1, 4], 16),
            ([1, 2, 1], 2),
            ([1, 2, 4, 3], 4),
            ([2, 3, 4, 5, 18, 17, 6], 17),
            ([1, 8, 6, 2, 5, 4, 8, 25, 7], 49),
            ([1, 3, 2, 5, 25, 24, 5], 24),
            ([0, 0], 0),
            ([1, 0], 0),
            ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 25),
        ],
    )
    def test_max_area(self, solution, height, expected):
        assert solution.maxArea(height) == expected

    def test_result_non_negative(self, solution):
        test_cases = [[1, 2, 3], [0, 0, 0], [1, 1]]
        for height in test_cases:
            assert solution.maxArea(height) >= 0
