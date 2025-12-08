"""Tests for LeetCode 151. Reverse Words in a String"""

import pytest
from pathlib import Path
import importlib.util

# Dynamic import to avoid module name conflicts
_solution_path = Path(__file__).parent / "solution.py"
_spec = importlib.util.spec_from_file_location("solution_151", _solution_path)
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)

Solution = _solution.Solution
SolutionTwoPointers = _solution.SolutionTwoPointers
SolutionInPlace = _solution.SolutionInPlace


class TestReverseWords:
    """Test cases for reverseWords method"""

    @pytest.fixture
    def solution(self):
        """Create Solution instance"""
        return Solution()

    @pytest.fixture
    def solution_two_pointers(self):
        """Create SolutionTwoPointers instance"""
        return SolutionTwoPointers()

    @pytest.fixture
    def solution_in_place(self):
        """Create SolutionInPlace instance"""
        return SolutionInPlace()

    @pytest.mark.parametrize(
        "s,expected",
        [
            # Example test cases
            ("the sky is blue", "blue is sky the"),
            ("  hello world  ", "world hello"),
            ("a good   example", "example good a"),
            # Single word
            ("word", "word"),
            ("  word  ", "word"),
            # Two words
            ("hello world", "world hello"),
            ("  hello   world  ", "world hello"),
            # Multiple spaces
            ("a  b  c", "c b a"),
            ("   a   b   c   ", "c b a"),
            # Long string
            ("one two three four five", "five four three two one"),
            # Numbers and letters
            ("test123 abc456", "abc456 test123"),
            ("1 2 3 4 5", "5 4 3 2 1"),
            # Mixed case
            ("Hello World", "World Hello"),
            ("UPPER lower MiXeD", "MiXeD lower UPPER"),
            # Edge cases
            ("a", "a"),
            ("  a  ", "a"),
            ("ab", "ab"),
            ("a b", "b a"),
            # Many words
            ("a b c d e f g", "g f e d c b a"),
            # Palindrome words
            ("level deed civic", "civic deed level"),
        ],
    )
    def test_reverse_words(self, solution, s, expected):
        """Test reverseWords with various inputs"""
        assert solution.reverseWords(s) == expected

    def test_all_solutions_consistent(self):
        """Ensure all solutions produce the same results"""
        sol1 = Solution()
        sol2 = SolutionTwoPointers()
        sol3 = SolutionInPlace()

        test_cases = [
            "the sky is blue",
            "  hello world  ",
            "a good   example",
            "word",
            "  spaces   everywhere  ",
        ]

        for s in test_cases:
            result1 = sol1.reverseWords(s)
            result2 = sol2.reverseWords(s)
            result3 = sol3.reverseWords(s)
            assert result1 == result2 == result3, f"Solutions differ for '{s}'"

    def test_no_leading_trailing_spaces(self, solution):
        """Test that result has no leading or trailing spaces"""
        test_cases = [
            "  hello world  ",
            "   test   ",
            "  a  b  c  ",
        ]

        for s in test_cases:
            result = solution.reverseWords(s)
            assert result == result.strip(), f"Result has leading/trailing spaces: '{result}'"

    def test_single_space_between_words(self, solution):
        """Test that result has exactly one space between words"""
        test_cases = [
            "a   b   c",
            "hello    world",
            "  too   many   spaces  ",
        ]

        for s in test_cases:
            result = solution.reverseWords(s)
            assert "  " not in result, f"Result has multiple spaces: '{result}'"

    def test_word_count_preserved(self, solution):
        """Test that word count is preserved after reversal"""
        test_cases = [
            "one two three",
            "a b c d e",
            "single",
        ]

        for s in test_cases:
            original_words = len(s.split())
            result_words = len(solution.reverseWords(s).split())
            assert original_words == result_words, f"Word count mismatch for '{s}'"

    def test_double_reverse_is_identity(self, solution):
        """Test that reversing twice returns the original (normalized) string"""
        test_cases = [
            "hello world",
            "a b c",
            "one two three four",
        ]

        for s in test_cases:
            once = solution.reverseWords(s)
            twice = solution.reverseWords(once)
            # After normalizing spaces, double reverse should be identity
            normalized = " ".join(s.split())
            assert twice == normalized, f"Double reverse failed for '{s}'"
