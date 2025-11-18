"""Tests for LeetCode 1768. Merge Strings Alternately"""

import pytest
from solution import Solution, SolutionAlternative


class TestMergeStringsAlternately:
    """Test cases for mergeAlternately method"""

    @pytest.fixture
    def solution(self):
        """Create Solution instance"""
        return Solution()

    @pytest.fixture
    def solution_alt(self):
        """Create SolutionAlternative instance"""
        return SolutionAlternative()

    @pytest.mark.parametrize(
        "word1,word2,expected",
        [
            # Example test cases
            ("abc", "pqr", "apbqcr"),
            ("ab", "pqrs", "apbqrs"),
            ("abcd", "pq", "apbqcd"),
            # Edge cases
            ("a", "b", "ab"),
            ("a", "", "a"),
            ("", "b", "b"),
            ("", "", ""),
            # Same length strings
            ("hello", "world", "hweolrllod"),
            ("12345", "abcde", "1a2b3c4d5e"),
            # Very different lengths
            ("x", "yzabcd", "xyzabcd"),
            ("abcdefgh", "1", "a1bcdefgh"),
            # Single character
            ("z", "z", "zz"),
            # Longer strings
            ("programming", "contest", "pcroongtreasmtming"),
            ("leetcode", "solutions", "lseoeltuctoidoens"),
            # Numbers as strings
            ("123", "456", "142536"),
            # Repeated characters
            ("aaa", "bbb", "ababab"),
            ("aaaa", "b", "abaaa"),
        ],
    )
    def test_merge_alternately(self, solution, word1, word2, expected):
        """Test mergeAlternately with various inputs"""
        assert solution.mergeAlternately(word1, word2) == expected

    @pytest.mark.parametrize(
        "word1,word2,expected",
        [
            ("abc", "pqr", "apbqcr"),
            ("ab", "pqrs", "apbqrs"),
            ("abcd", "pq", "apbqcd"),
            ("", "", ""),
        ],
    )
    def test_merge_alternately_alternative(self, solution_alt, word1, word2, expected):
        """Test alternative solution"""
        assert solution_alt.mergeAlternately(word1, word2) == expected

    def test_both_solutions_consistent(self):
        """Ensure both solutions produce the same results"""
        sol1 = Solution()
        sol2 = SolutionAlternative()

        test_cases = [
            ("abc", "pqr"),
            ("ab", "pqrs"),
            ("abcd", "pq"),
            ("hello", "world"),
            ("", "test"),
            ("test", ""),
        ]

        for word1, word2 in test_cases:
            result1 = sol1.mergeAlternately(word1, word2)
            result2 = sol2.mergeAlternately(word1, word2)
            assert result1 == result2, f"Solutions differ for ({word1}, {word2})"
