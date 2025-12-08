#!/bin/bash

# new_problem.sh - 創建新的 LeetCode 題目模板
# 用法: ./scripts/new_problem.sh <序號> <題號> <題目名稱> [難度]
# 範例: ./scripts/new_problem.sh 68 2574 "Left and Right Sum Differences" easy

set -e

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 檢查參數
if [ $# -lt 3 ]; then
    echo -e "${RED}錯誤: 參數不足${NC}"
    echo "用法: $0 <序號> <題號> <題目名稱> [難度]"
    echo "範例: $0 68 2574 \"Left and Right Sum Differences\" easy"
    exit 1
fi

SEQ_NUM=$(printf "%04d" $1)
PROBLEM_NUM=$2
PROBLEM_NAME=$3
DIFFICULTY=${4:-"Medium"}  # 預設為 Medium

# 標準化難度
case $(echo "$DIFFICULTY" | tr '[:upper:]' '[:lower:]') in
    easy)   DIFFICULTY="Easy" ;;
    medium) DIFFICULTY="Medium" ;;
    hard)   DIFFICULTY="Hard" ;;
    *)      DIFFICULTY="Medium" ;;
esac

# 創建目錄
PROBLEM_DIR="Leetcode_重刷紀錄/${SEQ_NUM}.Problems${PROBLEM_NUM}. ${PROBLEM_NAME}"

if [ -d "$PROBLEM_DIR" ]; then
    echo -e "${YELLOW}警告: 目錄已存在: $PROBLEM_DIR${NC}"
    read -p "是否覆蓋? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

mkdir -p "$PROBLEM_DIR"

# 創建 solution.py
cat > "$PROBLEM_DIR/solution.py" << 'SOLUTION_EOF'
"""
PROBLEM_NUM. PROBLEM_NAME

Difficulty: DIFFICULTY
Topics: TODO

Problem:
TODO: Add problem description here.

Example 1:
    Input: TODO
    Output: TODO
    Explanation: TODO

Example 2:
    Input: TODO
    Output: TODO
    Explanation: TODO

Constraints:
    - TODO: Add constraints
"""

from typing import List, Optional


class Solution:
    def solutionMethod(self, param: int) -> int:
        """
        Main solution using optimal approach.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            param: TODO describe parameter

        Returns:
            TODO describe return value
        """
        # TODO: Implement solution
        pass


class SolutionAlternative:
    """Alternative solution using different approach"""

    def solutionMethod(self, param: int) -> int:
        """
        Alternative solution.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement alternative solution
        pass
SOLUTION_EOF

# 替換佔位符
sed -i "s/PROBLEM_NUM/${PROBLEM_NUM}/g" "$PROBLEM_DIR/solution.py"
sed -i "s/PROBLEM_NAME/${PROBLEM_NAME}/g" "$PROBLEM_DIR/solution.py"
sed -i "s/DIFFICULTY/${DIFFICULTY}/g" "$PROBLEM_DIR/solution.py"

# 創建 test_{題號}.py
cat > "$PROBLEM_DIR/test_${PROBLEM_NUM}.py" << TEST_EOF
"""Tests for LeetCode ${PROBLEM_NUM}. ${PROBLEM_NAME}"""

import pytest
from pathlib import Path
import importlib.util

# Dynamic import to avoid module name conflicts
_solution_path = Path(__file__).parent / "solution.py"
_spec = importlib.util.spec_from_file_location("solution_${PROBLEM_NUM}", _solution_path)
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)

Solution = _solution.Solution
SolutionAlternative = _solution.SolutionAlternative


class TestSolutionMethod:
    """Test cases for solutionMethod"""

    @pytest.fixture
    def solution(self):
        """Create Solution instance"""
        return Solution()

    @pytest.fixture
    def solution_alt(self):
        """Create SolutionAlternative instance"""
        return SolutionAlternative()

    @pytest.mark.parametrize(
        "param,expected",
        [
            # Example test cases
            # TODO: Add test cases from problem description
            (1, 1),
            # Edge cases
            # TODO: Add edge cases
        ],
    )
    def test_solution_method(self, solution, param, expected):
        """Test solutionMethod with various inputs"""
        assert solution.solutionMethod(param) == expected

    @pytest.mark.parametrize(
        "param,expected",
        [
            (1, 1),
        ],
    )
    def test_solution_alternative(self, solution_alt, param, expected):
        """Test alternative solution"""
        assert solution_alt.solutionMethod(param) == expected

    def test_both_solutions_consistent(self):
        """Ensure both solutions produce the same results"""
        sol1 = Solution()
        sol2 = SolutionAlternative()

        test_cases = [
            # TODO: Add test cases
            1,
        ]

        for param in test_cases:
            result1 = sol1.solutionMethod(param)
            result2 = sol2.solutionMethod(param)
            assert result1 == result2, f"Solutions differ for {param}"
TEST_EOF

# 創建 __init__.py
touch "$PROBLEM_DIR/__init__.py"

echo -e "${GREEN}✓ 成功創建題目模板:${NC}"
echo -e "  ${BLUE}目錄:${NC} $PROBLEM_DIR"
echo -e "  ${BLUE}檔案:${NC}"
echo "    - solution.py"
echo "    - test_${PROBLEM_NUM}.py"
echo "    - __init__.py"
echo ""
echo -e "${YELLOW}下一步:${NC}"
echo "1. 編輯 solution.py 添加題目描述和實現"
echo "2. 編輯 test_${PROBLEM_NUM}.py 添加測試案例"
echo "3. 運行測試: pytest \"$PROBLEM_DIR\" -v"
