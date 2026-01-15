#!/usr/bin/env python3
"""
遷移腳本：將舊格式的 LeetCode 解決方案轉換為新的標準格式

功能：
- 掃描所有題目目錄
- 識別尚未遷移的題目（沒有 solution.py）
- 從舊格式文件提取代碼並生成標準化的 solution.py
- 保留原始文件作為備份

使用方式：
    python scripts/migrate_solutions.py [--dry-run] [--verbose]
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import NamedTuple


class ProblemInfo(NamedTuple):
    """題目資訊結構"""

    index: str  # 例如 "0006"
    problem_number: str  # 例如 "151"
    title: str  # 例如 "Reverse Words in a String"
    directory: Path
    old_file: Path | None
    has_solution: bool


# LeetCode 題目難度對照表（基於題號）
DIFFICULTY_MAP = {
    # Easy
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
    # Medium
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
    "17": "Medium",
    "2375": "Medium",
    "1415": "Medium",
    "1980": "Medium",
    "1261": "Medium",
    "889": "Medium",
    "2467": "Medium",
    "1524": "Medium",
    "236": "Medium",
    "22": "Medium",
    "1749": "Medium",
    "199": "Medium",
    "873": "Medium",
    "2161": "Medium",
    "1780": "Medium",
    "2579": "Medium",
    "2965": "Medium",
    "2523": "Medium",
    "3208": "Medium",
    "1079": "Medium",
    "2698": "Medium",
    # Hard
    "1718": "Hard",
    "1028": "Hard",
}

# 題目主題對照表
TOPIC_MAP = {
    "1768": "Two Pointers, String",
    "1071": "Math, String",
    "1431": "Array",
    "605": "Array, Greedy",
    "345": "Two Pointers, String",
    "151": "Two Pointers, String",
    "238": "Array, Prefix Sum",
    "334": "Array, Greedy",
    "443": "Two Pointers, String",
    "283": "Array, Two Pointers",
    "392": "Two Pointers, String, Dynamic Programming",
    "11": "Array, Two Pointers, Greedy",
    "1679": "Array, Hash Table, Two Pointers, Sorting",
    "643": "Array, Sliding Window",
    "1456": "String, Sliding Window",
    "1004": "Array, Binary Search, Sliding Window, Prefix Sum",
    "1493": "Array, Dynamic Programming, Sliding Window",
    "1732": "Array, Prefix Sum",
    "724": "Array, Prefix Sum",
    "2215": "Array, Hash Table",
    "1207": "Array, Hash Table",
    "1657": "Hash Table, String, Sorting",
    "2352": "Array, Hash Table, Matrix, Simulation",
    "2390": "String, Stack, Simulation",
    "735": "Array, Stack, Simulation",
    "394": "String, Stack, Recursion",
    "933": "Design, Queue, Data Stream",
    "649": "String, Greedy, Queue",
    "2095": "Linked List, Two Pointers",
    "328": "Linked List",
    "206": "Linked List, Recursion",
    "2130": "Linked List, Two Pointers, Stack",
    "104": "Tree, DFS, BFS, Binary Tree",
    "872": "Tree, DFS, Binary Tree",
    "1448": "Tree, DFS, BFS, Binary Tree",
    "437": "Tree, DFS, Binary Tree",
    "1372": "Tree, DFS, Dynamic Programming, Binary Tree",
    "236": "Tree, DFS, Binary Tree",
    "199": "Tree, DFS, BFS, Binary Tree",
    "17": "Hash Table, String, Backtracking",
    "22": "String, Dynamic Programming, Backtracking",
    "88": "Array, Two Pointers, Sorting",
    "27": "Array, Two Pointers",
    "26": "Array, Two Pointers",
    "389": "Hash Table, String, Bit Manipulation, Sorting",
    "1749": "Array, Dynamic Programming",
    "873": "Array, Hash Table, Dynamic Programming",
    "2460": "Array, Simulation",
    "2570": "Array, Hash Table, Two Pointers",
    "2161": "Array, Two Pointers, Simulation",
    "1780": "Math",
    "2579": "Math, Geometry",
    "2965": "Array, Hash Table, Math, Matrix",
    "2523": "Math, Number Theory",
    "3208": "Array, Sliding Window",
    "1079": "Hash Table, String, Backtracking, Counting",
    "2698": "Math, Backtracking",
    "1718": "Array, Backtracking",
    "1028": "String, Tree, DFS, Binary Tree",
    "889": "Array, Hash Table, Divide and Conquer, Tree, Binary Tree",
    "2467": "Array, Tree, DFS, BFS, Graph",
    "1524": "Array, Math, Dynamic Programming, Prefix Sum",
    "2375": "String, Backtracking, Stack, Greedy",
    "1415": "String, Backtracking",
    "1980": "Array, Hash Table, String, Backtracking",
    "1261": "Hash Table, Tree, DFS, BFS, Design, Binary Tree",
}


def get_base_dir() -> Path:
    """獲取專案根目錄"""
    script_path = Path(__file__).resolve()
    return script_path.parent.parent


def parse_directory_name(dirname: str) -> tuple[str, str, str] | None:
    """
    解析目錄名稱以提取題目資訊

    Args:
        dirname: 目錄名稱，例如 "0006.Problems151. Reverse Words in a String"

    Returns:
        (index, problem_number, title) 或 None
    """
    # 匹配模式：0006.Problems151. Title 或 0006.Problem151. Title
    pattern = r"^(\d+)\.Problems?\s*(\d+)\.\s*(.+)$"
    match = re.match(pattern, dirname)
    if match:
        return match.group(1), match.group(2), match.group(3).strip()
    return None


def find_old_solution_file(directory: Path) -> Path | None:
    """
    在目錄中尋找舊格式的解決方案文件

    Args:
        directory: 題目目錄

    Returns:
        舊格式文件路徑或 None
    """
    # 排除已經是新格式的文件
    exclude = {"solution.py", "test_solution.py", "__init__.py", "__pycache__"}

    for file in directory.iterdir():
        if file.is_file() and file.suffix == ".py" and file.name not in exclude:
            return file
    return None


def scan_problems(base_dir: Path) -> list[ProblemInfo]:
    """
    掃描所有題目目錄並收集資訊

    Args:
        base_dir: 專案根目錄

    Returns:
        ProblemInfo 列表
    """
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
        old_file = find_old_solution_file(item)

        problems.append(
            ProblemInfo(
                index=index,
                problem_number=problem_number,
                title=title,
                directory=item,
                old_file=old_file,
                has_solution=solution_file.exists(),
            )
        )

    return problems


def extract_code_from_old_file(file_path: Path) -> str:
    """
    從舊格式文件中提取代碼

    Args:
        file_path: 舊格式文件路徑

    Returns:
        提取的代碼（Solution class 部分）
    """
    with open(file_path, encoding="utf-8") as f:
        content = f.read()

    # 移除開頭的註解行（// 或 #）
    lines = content.split("\n")
    code_lines = []
    in_code = False

    for line in lines:
        # 跳過開頭的單行註解
        if not in_code and (line.strip().startswith("//") or line.strip().startswith("#")):
            if "class" not in line.lower():
                continue
        in_code = True
        code_lines.append(line)

    return "\n".join(code_lines).strip()


def generate_solution_file(problem: ProblemInfo) -> str:
    """
    生成標準化的 solution.py 內容

    Args:
        problem: 題目資訊

    Returns:
        solution.py 文件內容
    """
    difficulty = DIFFICULTY_MAP.get(problem.problem_number, "Medium")
    topics = TOPIC_MAP.get(problem.problem_number, "Algorithm")

    # 從舊文件提取代碼
    old_code = ""
    if problem.old_file and problem.old_file.exists():
        old_code = extract_code_from_old_file(problem.old_file)

    # 如果沒有提取到代碼，使用預設模板
    if not old_code or "class Solution" not in old_code:
        old_code = '''class Solution:
    def solve(self, *args):
        """
        TODO: Implement solution

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        pass'''

    # 確保代碼有正確的縮排和文檔
    template = f'''"""
{problem.problem_number}. {problem.title}

Difficulty: {difficulty}
Topics: {topics}

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

{old_code}
'''
    return template


def migrate_problem(problem: ProblemInfo, dry_run: bool = False, verbose: bool = False) -> bool:
    """
    遷移單個題目到新格式

    Args:
        problem: 題目資訊
        dry_run: 是否只是模擬執行
        verbose: 是否顯示詳細資訊

    Returns:
        是否成功遷移
    """
    if problem.has_solution:
        if verbose:
            print(f"  跳過 {problem.index}: 已有 solution.py")
        return False

    if not problem.old_file:
        if verbose:
            print(f"  跳過 {problem.index}: 找不到舊格式文件")
        return False

    solution_content = generate_solution_file(problem)
    solution_path = problem.directory / "solution.py"

    if dry_run:
        print(f"  [DRY-RUN] 將創建: {solution_path}")
        if verbose:
            print(f"    來源: {problem.old_file.name}")
        return True

    # 寫入新的 solution.py
    with open(solution_path, "w", encoding="utf-8") as f:
        f.write(solution_content)

    print(f"  ✓ 已創建: {solution_path.name}")
    if verbose:
        print(f"    來源: {problem.old_file.name}")

    return True


def main():
    """主函數"""
    parser = argparse.ArgumentParser(description="遷移 LeetCode 解決方案到新格式")
    parser.add_argument("--dry-run", action="store_true", help="模擬執行，不實際修改文件")
    parser.add_argument("--verbose", "-v", action="store_true", help="顯示詳細資訊")
    args = parser.parse_args()

    base_dir = get_base_dir()
    print(f"掃描專案目錄: {base_dir}")
    print()

    problems = scan_problems(base_dir)

    # 統計
    total = len(problems)
    already_migrated = sum(1 for p in problems if p.has_solution)
    to_migrate = [p for p in problems if not p.has_solution and p.old_file]

    print(f"📊 統計資訊:")
    print(f"   總題目數: {total}")
    print(f"   已遷移: {already_migrated}")
    print(f"   待遷移: {len(to_migrate)}")
    print(f"   無法遷移（無舊文件）: {total - already_migrated - len(to_migrate)}")
    print()

    if not to_migrate:
        print("✅ 沒有需要遷移的題目")
        return

    print(f"🔄 開始遷移 {len(to_migrate)} 個題目...")
    if args.dry_run:
        print("   (DRY-RUN 模式 - 不會實際修改文件)")
    print()

    migrated = 0
    for problem in to_migrate:
        if migrate_problem(problem, args.dry_run, args.verbose):
            migrated += 1

    print()
    print(f"✅ 遷移完成: {migrated} 個題目")


if __name__ == "__main__":
    main()
