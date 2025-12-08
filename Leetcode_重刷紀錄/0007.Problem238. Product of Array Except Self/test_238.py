"""Tests for LeetCode 238. Product of Array Except Self"""

import pytest
from pathlib import Path
import importlib.util

# Dynamic import to avoid module name conflicts
_solution_path = Path(__file__).parent / "solution.py"
_spec = importlib.util.spec_from_file_location("solution_238", _solution_path)
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)

Solution = _solution.Solution
SolutionTwoArrays = _solution.SolutionTwoArrays


class TestProductExceptSelf:
    """Test cases for productExceptSelf method"""

    @pytest.fixture
    def solution(self):
        """Create Solution instance"""
        return Solution()

    @pytest.fixture
    def solution_two_arrays(self):
        """Create SolutionTwoArrays instance"""
        return SolutionTwoArrays()

    @pytest.mark.parametrize(
        "nums,expected",
        [
            # Example test cases
            ([1, 2, 3, 4], [24, 12, 8, 6]),
            ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
            # Two elements
            ([1, 2], [2, 1]),
            ([0, 0], [0, 0]),
            ([5, 10], [10, 5]),
            # All ones
            ([1, 1, 1, 1], [1, 1, 1, 1]),
            # All same
            ([2, 2, 2, 2], [8, 8, 8, 8]),
            # With one zero
            ([1, 2, 0, 4], [0, 0, 8, 0]),
            ([0, 1, 2, 3], [6, 0, 0, 0]),
            # With multiple zeros
            ([0, 0, 1], [0, 0, 0]),
            ([1, 0, 2, 0], [0, 0, 0, 0]),
            # Negative numbers
            ([-1, -2, -3], [6, 3, 2]),
            ([-1, 2, -3, 4], [-24, 12, -8, 6]),
            # Mixed positive and negative
            ([1, -1, 1, -1], [1, -1, 1, -1]),
            ([2, -3, 4, -5], [60, -40, 30, -24]),
            # Larger numbers
            ([10, 20, 30], [600, 300, 200]),
            # Single digit sequence
            ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
        ],
    )
    def test_product_except_self(self, solution, nums, expected):
        """Test productExceptSelf with various inputs"""
        assert solution.productExceptSelf(nums) == expected

    def test_both_solutions_consistent(self):
        """Ensure both solutions produce the same results"""
        sol1 = Solution()
        sol2 = SolutionTwoArrays()

        test_cases = [
            [1, 2, 3, 4],
            [-1, 1, 0, -3, 3],
            [1, 2],
            [0, 1, 2],
            [-1, -2, -3, -4],
        ]

        for nums in test_cases:
            result1 = sol1.productExceptSelf(nums)
            result2 = sol2.productExceptSelf(nums)
            assert result1 == result2, f"Solutions differ for {nums}"

    def test_result_length(self, solution):
        """Test that result length equals input length"""
        test_cases = [
            [1, 2],
            [1, 2, 3, 4, 5],
            [0] * 10,
        ]

        for nums in test_cases:
            result = solution.productExceptSelf(nums)
            assert len(result) == len(nums), f"Length mismatch for {nums}"

    def test_product_verification(self, solution):
        """Verify that answer[i] * nums[i] equals total product (when no zeros)"""
        nums = [1, 2, 3, 4, 5]
        total_product = 1
        for n in nums:
            total_product *= n

        result = solution.productExceptSelf(nums)

        for i in range(len(nums)):
            assert result[i] * nums[i] == total_product, f"Product verification failed at index {i}"

    def test_no_division_used(self, solution):
        """Verify solution works with zeros (division would fail)"""
        # This implicitly tests that division is not used
        test_cases = [
            [0, 1, 2],
            [1, 0, 3],
            [1, 2, 0],
            [0, 0, 0],
        ]

        for nums in test_cases:
            # Should not raise any exception
            result = solution.productExceptSelf(nums)
            assert len(result) == len(nums)
