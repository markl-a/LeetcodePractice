#!/usr/bin/env python3
"""
測試模板生成器：為 LeetCode 解決方案自動生成 pytest 測試框架

功能：
- 掃描所有題目目錄
- 識別尚未有測試的題目（沒有 test_solution.py）
- 分析 solution.py 提取方法簽名
- 生成標準化的 pytest 測試模板

使用方式：
    python scripts/generate_tests.py [--dry-run] [--verbose] [--problem INDEX]
"""

import argparse
import ast
import re
import sys
from pathlib import Path
from typing import NamedTuple

# 難度標記對照
DIFFICULTY_MARKS = {
    "Easy": "easy",
    "Medium": "medium",
    "Hard": "hard",
}

# 難度對照表（與 migrate_solutions.py 共用）
DIFFICULTY_MAP = {
    "1768": "Easy",
    "1071": "Easy",
    "1431": "Easy",
    "605": "Easy",
    "345": "Easy",
    "283": "Easy",
    "392": "Easy",
    "643": "Easy",
    "1732": "Easy",
    "724": "Easy",
    "2215": "Easy",
    "1207": "Easy",
    "933": "Easy",
    "104": "Easy",
    "872": "Easy",
    "88": "Easy",
    "27": "Easy",
    "389": "Easy",
    "2460": "Easy",
    "2570": "Easy",
    "206": "Easy",
    "26": "Easy",
    "151": "Medium",
    "238": "Medium",
    "334": "Medium",
    "443": "Medium",
    "11": "Medium",
    "1679": "Medium",
    "1456": "Medium",
    "1004": "Medium",
    "1493": "Medium",
    "1657": "Medium",
    "2352": "Medium",
    "2390": "Medium",
    "735": "Medium",
    "394": "Medium",
    "649": "Medium",
    "2095": "Medium",
    "328": "Medium",
    "2130": "Medium",
    "1448": "Medium",
    "437": "Medium",
    "1372": "Medium",
    "236": "Medium",
    "199": "Medium",
    "17": "Medium",
    "22": "Medium",
    "1749": "Medium",
    "873": "Medium",
    "2161": "Medium",
    "1780": "Medium",
    "2579": "Medium",
    "2965": "Medium",
    "2523": "Medium",
    "3208": "Medium",
    "1079": "Medium",
    "2698": "Medium",
    "1718": "Hard",
    "1028": "Hard",
}


class MethodInfo(NamedTuple):
    """方法資訊結構"""

    name: str
    params: list[tuple[str, str]]  # (param_name, type_hint)
    return_type: str


class ProblemInfo(NamedTuple):
    """題目資訊結構"""

    index: str
    problem_number: str
    title: str
    directory: Path
    has_solution: bool
    has_test: bool
    methods: list[MethodInfo]


def get_base_dir() -> Path:
    """獲取專案根目錄"""
    script_path = Path(__file__).resolve()
    return script_path.parent.parent


def parse_directory_name(dirname: str) -> tuple[str, str, str] | None:
    """解析目錄名稱以提取題目資訊"""
    pattern = r"^(\d+)\.Problems?\s*(\d+)\.\s*(.+)$"
    match = re.match(pattern, dirname)
    if match:
        return match.group(1), match.group(2), match.group(3).strip()
    return None


def extract_methods_from_solution(solution_path: Path) -> list[MethodInfo]:
    """
    從 solution.py 中提取 Solution class 的方法資訊

    Args:
        solution_path: solution.py 文件路徑

    Returns:
        MethodInfo 列表
    """
    methods = []

    try:
        with open(solution_path, encoding="utf-8") as f:
            content = f.read()

        tree = ast.parse(content)

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == "Solution":
                for item in node.body:
                    if isinstance(item, ast.FunctionDef) and not item.name.startswith("_"):
                        # 提取參數
                        params = []
                        for arg in item.args.args:
                            if arg.arg == "self":
                                continue
                            type_hint = ""
                            if arg.annotation:
                                type_hint = ast.unparse(arg.annotation)
                            params.append((arg.arg, type_hint))

                        # 提取返回類型
                        return_type = ""
                        if item.returns:
                            return_type = ast.unparse(item.returns)

                        methods.append(
                            MethodInfo(name=item.name, params=params, return_type=return_type)
                        )

    except (SyntaxError, FileNotFoundError) as e:
        print(f"  警告：無法解析 {solution_path}: {e}")

    return methods


def scan_problems(base_dir: Path) -> list[ProblemInfo]:
    """掃描所有題目目錄並收集資訊"""
    problems_dir = base_dir / "Leetcode_重刷紀錄"
    problems = []

    if not problems_dir.exists():
        print(f"錯誤：找不到題目目錄 {problems_dir}")
        sys.exit(1)

    for item in sorted(problems_dir.iterdir()):
        if not item.is_dir() or item.name.startswith("."):
            continue

        parsed = parse_directory_name(item.name)
        if not parsed:
            continue

        index, problem_number, title = parsed
        solution_file = item / "solution.py"
        test_file = item / "test_solution.py"

        methods = []
        if solution_file.exists():
            methods = extract_methods_from_solution(solution_file)

        problems.append(
            ProblemInfo(
                index=index,
                problem_number=problem_number,
                title=title,
                directory=item,
                has_solution=solution_file.exists(),
                has_test=test_file.exists(),
                methods=methods,
            )
        )

    return problems


def generate_test_file(problem: ProblemInfo) -> str:
    """
    生成標準化的 test_solution.py 內容

    Args:
        problem: 題目資訊

    Returns:
        test_solution.py 文件內容
    """
    difficulty = DIFFICULTY_MAP.get(problem.problem_number, "Medium")
    difficulty_mark = DIFFICULTY_MARKS.get(difficulty, "medium")

    # 生成測試方法
    test_methods = []

    if problem.methods:
        for method in problem.methods:
            # 生成參數模板
            param_names = [p[0] for p in method.params]
            param_template = ", ".join(param_names) if param_names else "input_data"

            # 根據返回類型生成預期值模板
            expected_template = "expected"
            if method.return_type:
                if "List" in method.return_type:
                    expected_template = "[]"
                elif "int" in method.return_type:
                    expected_template = "0"
                elif "str" in method.return_type:
                    expected_template = '""'
                elif "bool" in method.return_type:
                    expected_template = "True"
                else:
                    expected_template = "None"

            test_methods.append(
                f'''
class Test{method.name.title().replace("_", "")}:
    """測試 Solution.{method.name} 方法"""

    @pytest.mark.parametrize(
        "{param_template}, expected",
        [
            # 基本測試用例
            # TODO: 添加測試數據
            # ({param_template}, {expected_template}),
        ],
    )
    def test_basic_cases(self, solution, {param_template}, expected):
        """基本功能測試"""
        result = solution.{method.name}({", ".join(param_names)})
        assert result == expected

    def test_edge_cases(self, solution):
        """邊界條件測試"""
        # TODO: 添加邊界測試
        pass
'''
            )
    else:
        # 如果沒有找到方法，使用通用模板
        test_methods.append(
            '''
class TestSolution:
    """測試 Solution 類"""

    @pytest.mark.parametrize(
        "input_data, expected",
        [
            # 基本測試用例
            # TODO: 添加測試數據
        ],
    )
    def test_basic_cases(self, solution, input_data, expected):
        """基本功能測試"""
        # TODO: 調用正確的方法
        # result = solution.method_name(input_data)
        # assert result == expected
        pass

    def test_edge_cases(self, solution):
        """邊界條件測試"""
        # TODO: 添加邊界測試
        pass
'''
        )

    test_methods_str = "\n".join(test_methods)

    template = f'''"""
測試文件：{problem.problem_number}. {problem.title}

使用 pytest 運行測試：
    pytest {problem.directory.name}/test_solution.py -v
"""

import pytest

from .solution import Solution


@pytest.fixture
def solution():
    """創建 Solution 實例"""
    return Solution()


@pytest.mark.{difficulty_mark}
{test_methods_str}
'''
    return template


def generate_test(problem: ProblemInfo, dry_run: bool = False, verbose: bool = False) -> bool:
    """
    為單個題目生成測試文件

    Args:
        problem: 題目資訊
        dry_run: 是否只是模擬執行
        verbose: 是否顯示詳細資訊

    Returns:
        是否成功生成
    """
    if problem.has_test:
        if verbose:
            print(f"  跳過 {problem.index}: 已有 test_solution.py")
        return False

    if not problem.has_solution:
        if verbose:
            print(f"  跳過 {problem.index}: 沒有 solution.py（請先執行遷移）")
        return False

    test_content = generate_test_file(problem)
    test_path = problem.directory / "test_solution.py"

    if dry_run:
        print(f"  [DRY-RUN] 將創建: {test_path}")
        if verbose and problem.methods:
            print(f"    找到方法: {', '.join(m.name for m in problem.methods)}")
        return True

    # 寫入測試文件
    with open(test_path, "w", encoding="utf-8") as f:
        f.write(test_content)

    print(f"  ✓ 已創建: {test_path.name}")
    if verbose and problem.methods:
        print(f"    測試方法: {', '.join(m.name for m in problem.methods)}")

    return True


def main():
    """主函數"""
    parser = argparse.ArgumentParser(description="為 LeetCode 解決方案生成測試模板")
    parser.add_argument("--dry-run", action="store_true", help="模擬執行，不實際修改文件")
    parser.add_argument("--verbose", "-v", action="store_true", help="顯示詳細資訊")
    parser.add_argument("--problem", "-p", type=str, help="只處理指定的題目（使用索引，如 0006）")
    args = parser.parse_args()

    base_dir = get_base_dir()
    print(f"掃描專案目錄: {base_dir}")
    print()

    problems = scan_problems(base_dir)

    # 如果指定了特定題目
    if args.problem:
        problems = [p for p in problems if p.index == args.problem]
        if not problems:
            print(f"錯誤：找不到題目 {args.problem}")
            sys.exit(1)

    # 統計
    total = len(problems)
    has_test = sum(1 for p in problems if p.has_test)
    has_solution = sum(1 for p in problems if p.has_solution)
    to_generate = [p for p in problems if not p.has_test and p.has_solution]

    print(f"📊 統計資訊:")
    print(f"   總題目數: {total}")
    print(f"   已有測試: {has_test}")
    print(f"   有 solution.py: {has_solution}")
    print(f"   待生成測試: {len(to_generate)}")
    print()

    if not to_generate:
        print("✅ 沒有需要生成測試的題目")
        return

    print(f"🔄 開始生成 {len(to_generate)} 個測試文件...")
    if args.dry_run:
        print("   (DRY-RUN 模式 - 不會實際修改文件)")
    print()

    generated = 0
    for problem in to_generate:
        if generate_test(problem, args.dry_run, args.verbose):
            generated += 1

    print()
    print(f"✅ 生成完成: {generated} 個測試文件")
    print()
    print("💡 提示：生成的測試文件包含 TODO 標記，請手動添加測試用例")


if __name__ == "__main__":
    main()
