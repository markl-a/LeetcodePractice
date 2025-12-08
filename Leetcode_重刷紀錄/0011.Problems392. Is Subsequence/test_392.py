"""Tests for LeetCode 392. Is Subsequence"""

import pytest
from pathlib import Path
import importlib.util

# Dynamic import to avoid module name conflicts
_solution_path = Path(__file__).parent / "solution.py"
_spec = importlib.util.spec_from_file_location("solution_392", _solution_path)
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)

Solution = _solution.Solution
SolutionIterator = _solution.SolutionIterator
SolutionRecursive = _solution.SolutionRecursive


class TestIsSubsequence:
    """Test cases for isSubsequence method"""

    @pytest.fixture
    def solution(self):
        """Create Solution instance"""
        return Solution()

    @pytest.mark.parametrize(
        "s,t,expected",
        [
            # Example test cases
            ("abc", "ahbgdc", True),
            ("axc", "ahbgdc", False),
            # Empty s
            ("", "ahbgdc", True),
            ("", "", True),
            # Empty t
            ("a", "", False),
            # Same strings
            ("abc", "abc", True),
            # Single characters
            ("a", "a", True),
            ("a", "b", False),
            ("a", "ba", True),
            ("a", "ab", True),
            # Longer subsequences
            ("ace", "abcde", True),
            ("aec", "abcde", False),
            # All same characters
            ("aaa", "aaaa", True),
            ("aaaa", "aaa", False),
            # No common characters
            ("xyz", "abc", False),
            # Subsequence at beginning
            ("ab", "abcdef", True),
            # Subsequence at end
            ("ef", "abcdef", True),
            # Every other character
            ("ace", "abcdef", True),
            ("bdf", "abcdef", True),
            # Long strings
            ("abc", "a" * 1000 + "b" * 1000 + "c" * 1000, True),
            # s longer than t
            ("abcd", "abc", False),
        ],
    )
    def test_is_subsequence(self, solution, s, t, expected):
        """Test isSubsequence with various inputs"""
        assert solution.isSubsequence(s, t) == expected

    def test_all_solutions_consistent(self):
        """Ensure all solutions produce the same results"""
        sol1 = Solution()
        sol2 = SolutionIterator()
        sol3 = SolutionRecursive()

        test_cases = [
            ("abc", "ahbgdc"),
            ("axc", "ahbgdc"),
            ("", "test"),
            ("test", "test"),
            ("ace", "abcde"),
        ]

        for s, t in test_cases:
            result1 = sol1.isSubsequence(s, t)
            result2 = sol2.isSubsequence(s, t)
            result3 = sol3.isSubsequence(s, t)
            assert result1 == result2 == result3, f"Solutions differ for ({s}, {t})"
