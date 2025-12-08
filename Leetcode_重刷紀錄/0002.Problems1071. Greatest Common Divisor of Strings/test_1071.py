"""Tests for LeetCode 1071. Greatest Common Divisor of Strings"""

import pytest
from pathlib import Path
import importlib.util

# Dynamic import to avoid module name conflicts
_solution_path = Path(__file__).parent / "solution.py"
_spec = importlib.util.spec_from_file_location("solution_1071", _solution_path)
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)

Solution = _solution.Solution
SolutionRecursive = _solution.SolutionRecursive
SolutionBruteForce = _solution.SolutionBruteForce


class TestGCDOfStrings:
    """Test cases for gcdOfStrings method"""

    @pytest.fixture
    def solution(self):
        """Create Solution instance"""
        return Solution()

    @pytest.fixture
    def solution_recursive(self):
        """Create SolutionRecursive instance"""
        return SolutionRecursive()

    @pytest.fixture
    def solution_brute(self):
        """Create SolutionBruteForce instance"""
        return SolutionBruteForce()

    @pytest.mark.parametrize(
        "str1,str2,expected",
        [
            # Example test cases
            ("ABCABC", "ABC", "ABC"),
            ("ABABAB", "ABAB", "AB"),
            ("LEET", "CODE", ""),
            # Edge cases
            ("A", "A", "A"),
            ("AB", "AB", "AB"),
            ("ABC", "ABCABC", "ABC"),
            # No common divisor
            ("ABCD", "XY", ""),
            ("AAA", "BB", ""),
            # Same string
            ("TEST", "TEST", "TEST"),
            # One character divisor
            ("AAA", "AAAA", "A"),
            ("BBBB", "BB", "BB"),
            # Complex patterns
            ("ABABABAB", "ABAB", "ABAB"),
            ("ABCABCABC", "ABCABC", "ABC"),
            ("XYXYXYXY", "XYXY", "XYXY"),
            # Different lengths with GCD
            ("ABCABCABCABC", "ABCABC", "ABC"),
            ("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXX"),
            # Long strings with single char GCD
            ("A" * 100, "A" * 50, "A"),
            ("AB" * 50, "AB" * 25, "AB"),
            # No match at all
            ("AAAAAA", "BBBBBB", ""),
            ("ABCDEF", "GHIJKL", ""),
        ],
    )
    def test_gcd_of_strings(self, solution, str1, str2, expected):
        """Test gcdOfStrings with various inputs"""
        assert solution.gcdOfStrings(str1, str2) == expected

    @pytest.mark.parametrize(
        "str1,str2,expected",
        [
            ("ABCABC", "ABC", "ABC"),
            ("ABABAB", "ABAB", "AB"),
            ("LEET", "CODE", ""),
            ("AAA", "AAAA", "A"),
        ],
    )
    def test_gcd_recursive(self, solution_recursive, str1, str2, expected):
        """Test recursive solution"""
        assert solution_recursive.gcdOfStrings(str1, str2) == expected

    @pytest.mark.parametrize(
        "str1,str2,expected",
        [
            ("ABCABC", "ABC", "ABC"),
            ("ABABAB", "ABAB", "AB"),
            ("LEET", "CODE", ""),
            ("AAA", "AAAA", "A"),
        ],
    )
    def test_gcd_brute_force(self, solution_brute, str1, str2, expected):
        """Test brute force solution"""
        assert solution_brute.gcdOfStrings(str1, str2) == expected

    def test_all_solutions_consistent(self):
        """Ensure all solutions produce the same results"""
        sol1 = Solution()
        sol2 = SolutionRecursive()
        sol3 = SolutionBruteForce()

        test_cases = [
            ("ABCABC", "ABC"),
            ("ABABAB", "ABAB"),
            ("LEET", "CODE"),
            ("A", "A"),
            ("AAA", "AAAA"),
            ("ABCD", "XY"),
        ]

        for str1, str2 in test_cases:
            result1 = sol1.gcdOfStrings(str1, str2)
            result2 = sol2.gcdOfStrings(str1, str2)
            result3 = sol3.gcdOfStrings(str1, str2)
            assert (
                result1 == result2 == result3
            ), f"Solutions differ for ({str1}, {str2}): {result1}, {result2}, {result3}"

    def test_symmetry(self, solution):
        """Test that gcdOfStrings(a, b) == gcdOfStrings(b, a)"""
        test_cases = [("ABCABC", "ABC"), ("ABABAB", "ABAB"), ("LEET", "CODE")]

        for str1, str2 in test_cases:
            assert solution.gcdOfStrings(str1, str2) == solution.gcdOfStrings(str2, str1)
