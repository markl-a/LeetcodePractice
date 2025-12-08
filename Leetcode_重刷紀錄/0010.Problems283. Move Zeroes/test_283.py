"""Tests for LeetCode 283. Move Zeroes"""

import pytest
from pathlib import Path
import importlib.util

# Dynamic import to avoid module name conflicts
_solution_path = Path(__file__).parent / "solution.py"
_spec = importlib.util.spec_from_file_location("solution_283", _solution_path)
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)

Solution = _solution.Solution
SolutionTwoPass = _solution.SolutionTwoPass
SolutionCountZeros = _solution.SolutionCountZeros


class TestMoveZeroes:
    """Test cases for moveZeroes method"""

    @pytest.fixture
    def solution(self):
        """Create Solution instance"""
        return Solution()

    @pytest.fixture
    def solution_two_pass(self):
        """Create SolutionTwoPass instance"""
        return SolutionTwoPass()

    @pytest.mark.parametrize(
        "nums,expected",
        [
            # Example test cases
            ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
            ([0], [0]),
            # No zeros
            ([1, 2, 3], [1, 2, 3]),
            ([1], [1]),
            # All zeros
            ([0, 0, 0], [0, 0, 0]),
            ([0, 0], [0, 0]),
            # Zeros at beginning
            ([0, 0, 1], [1, 0, 0]),
            ([0, 0, 0, 1], [1, 0, 0, 0]),
            # Zeros at end
            ([1, 0, 0], [1, 0, 0]),
            ([1, 2, 0, 0], [1, 2, 0, 0]),
            # Alternating
            ([0, 1, 0, 2, 0, 3], [1, 2, 3, 0, 0, 0]),
            ([1, 0, 2, 0, 3, 0], [1, 2, 3, 0, 0, 0]),
            # Two elements
            ([0, 1], [1, 0]),
            ([1, 0], [1, 0]),
            # Negative numbers
            ([-1, 0, 2, 0, -3], [-1, 2, -3, 0, 0]),
            ([0, -1, 0, -2], [-1, -2, 0, 0]),
            # Large numbers
            ([0, 1000000, 0, -1000000], [1000000, -1000000, 0, 0]),
            # Mixed
            ([4, 2, 4, 0, 0, 3, 0, 5, 1, 0], [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]),
        ],
    )
    def test_move_zeroes(self, solution, nums, expected):
        """Test moveZeroes with various inputs"""
        nums_copy = nums.copy()
        solution.moveZeroes(nums_copy)
        assert nums_copy == expected

    def test_all_solutions_consistent(self):
        """Ensure all solutions produce the same results"""
        sol1 = Solution()
        sol2 = SolutionTwoPass()
        sol3 = SolutionCountZeros()

        test_cases = [
            [0, 1, 0, 3, 12],
            [0],
            [1, 2, 3],
            [0, 0, 0],
            [0, 1, 0, 2, 0, 3],
        ]

        for nums in test_cases:
            nums1, nums2, nums3 = nums.copy(), nums.copy(), nums.copy()
            sol1.moveZeroes(nums1)
            sol2.moveZeroes(nums2)
            sol3.moveZeroes(nums3)
            assert nums1 == nums2 == nums3, f"Solutions differ for {nums}"

    def test_in_place_modification(self, solution):
        """Test that the function modifies the array in place"""
        nums = [0, 1, 0, 3, 12]
        original_id = id(nums)
        solution.moveZeroes(nums)
        assert id(nums) == original_id, "Array was replaced instead of modified in place"

    def test_preserves_non_zero_order(self, solution):
        """Test that relative order of non-zero elements is preserved"""
        nums = [0, 5, 0, 3, 0, 1, 0, 2]
        solution.moveZeroes(nums)
        non_zeros = [x for x in nums if x != 0]
        assert non_zeros == [5, 3, 1, 2], "Non-zero order not preserved"

    def test_zeros_at_end(self, solution):
        """Test that all zeros are at the end"""
        nums = [0, 1, 0, 2, 0, 3]
        solution.moveZeroes(nums)
        # Find first zero position
        first_zero = -1
        for i, x in enumerate(nums):
            if x == 0:
                first_zero = i
                break
        # All elements after first zero should be zero
        if first_zero != -1:
            assert all(x == 0 for x in nums[first_zero:])

    def test_element_count_preserved(self, solution):
        """Test that no elements are lost or added"""
        nums = [0, 1, 0, 3, 12]
        original_count = len(nums)
        original_zeros = nums.count(0)
        solution.moveZeroes(nums)
        assert len(nums) == original_count
        assert nums.count(0) == original_zeros
