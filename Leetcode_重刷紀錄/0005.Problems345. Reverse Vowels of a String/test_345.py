"""Tests for LeetCode 345. Reverse Vowels of a String"""

import pytest
from pathlib import Path
import importlib.util

# Dynamic import to avoid module name conflicts
_solution_path = Path(__file__).parent / "solution.py"
_spec = importlib.util.spec_from_file_location("solution_345", _solution_path)
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)

Solution = _solution.Solution
SolutionStack = _solution.SolutionStack
SolutionTwoPass = _solution.SolutionTwoPass


class TestReverseVowels:
    """Test cases for reverseVowels method"""

    @pytest.fixture
    def solution(self):
        """Create Solution instance"""
        return Solution()

    @pytest.fixture
    def solution_stack(self):
        """Create SolutionStack instance"""
        return SolutionStack()

    @pytest.fixture
    def solution_two_pass(self):
        """Create SolutionTwoPass instance"""
        return SolutionTwoPass()

    @pytest.mark.parametrize(
        "s,expected",
        [
            # Example test cases
            ("hello", "holle"),
            ("leetcode", "leotcede"),
            # Single vowel
            ("a", "a"),
            ("e", "e"),
            ("i", "i"),
            ("o", "o"),
            ("u", "u"),
            # Single consonant
            ("b", "b"),
            ("z", "z"),
            # No vowels
            ("bcdfg", "bcdfg"),
            ("rhythm", "rhythm"),
            ("xyz", "xyz"),
            # All vowels
            ("aeiou", "uoiea"),
            ("AEIOU", "UOIEA"),
            ("aEiOu", "uOiEa"),
            # Mixed case
            ("Hello", "Holle"),
            ("LeetCode", "LeotCede"),
            ("Programming", "Prigrammong"),
            # Two vowels
            ("ae", "ea"),
            ("EA", "AE"),
            ("ab", "ab"),
            ("ba", "ba"),
            # Multiple same vowels
            ("aaa", "aaa"),
            ("AAA", "AAA"),
            ("aaabbb", "aaabbb"),
            # Complex patterns
            ("race car", "race car"),
            ("beautiful", "buiutafel"),
            ("education", "odicatuen"),
            # Vowels at edges
            ("apple", "eppla"),
            ("orange", "erango"),
            ("umbrella", "ambrellu"),
            # Long strings
            ("a" * 100 + "b" * 100, "a" * 100 + "b" * 100),
            ("aeiou" * 10, "uoiea" * 10),
            # Special characters and spaces
            ("a b c", "a b c"),
            ("a!e@i#o$u", "u!o@i#e$a"),
            ("Hello, World!", "Hollo, Werld!"),
            # Numbers
            ("a1e2i3o4u5", "u1o2i3e4a5"),
            ("12345", "12345"),
            # Empty-like cases (minimum length is 1)
            ("x", "x"),
            # Palindromes
            ("racecar", "racecar"),
            ("level", "level"),
            # Upper and lower mixed
            ("AaBbCc", "aABbCc"),
            ("aEiOu", "uOiEa"),
            ("HeLLo WoRLd", "HoLLo WeRLd"),
        ],
    )
    def test_reverse_vowels(self, solution, s, expected):
        """Test reverseVowels with various inputs"""
        assert solution.reverseVowels(s) == expected

    def test_all_solutions_consistent(self):
        """Ensure all solutions produce the same results"""
        sol1 = Solution()
        sol2 = SolutionStack()
        sol3 = SolutionTwoPass()

        test_cases = [
            "hello",
            "leetcode",
            "aeiou",
            "bcdfg",
            "Hello, World!",
            "a",
            "xyz",
        ]

        for s in test_cases:
            result1 = sol1.reverseVowels(s)
            result2 = sol2.reverseVowels(s)
            result3 = sol3.reverseVowels(s)
            assert result1 == result2 == result3, f"Solutions differ for {s}"

    def test_preserves_length(self, solution):
        """Test that output length equals input length"""
        test_cases = ["hello", "world", "a", "xyz", "aeiou" * 100]

        for s in test_cases:
            result = solution.reverseVowels(s)
            assert len(result) == len(s), f"Length mismatch for {s}"

    def test_preserves_consonants_and_positions(self, solution):
        """Test that consonants remain in their original positions"""
        s = "hello"
        result = solution.reverseVowels(s)

        # Check consonants
        assert result[0] == "h"
        assert result[2] == "l"
        assert result[3] == "l"

    def test_case_sensitivity(self, solution):
        """Test that vowel case is preserved"""
        test_cases = [
            ("AE", "EA"),  # Uppercase swapped
            ("ae", "ea"),  # Lowercase swapped
            ("Ae", "eA"),  # Mixed case swapped
            ("HELLO", "HOLLE"),
        ]

        for s, expected in test_cases:
            assert solution.reverseVowels(s) == expected

    def test_double_reverse_is_identity(self, solution):
        """Test that reversing vowels twice returns original string"""
        test_cases = ["hello", "leetcode", "world", "aeiou"]

        for s in test_cases:
            once = solution.reverseVowels(s)
            twice = solution.reverseVowels(once)
            assert twice == s, f"Double reverse failed for {s}"
