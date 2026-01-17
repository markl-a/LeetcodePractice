#!/usr/bin/env python3
"""
題目索引生成器：自動生成按難度和主題分類的題目索引

功能：
- 掃描所有題目目錄
- 按難度等級分類（Easy/Medium/Hard）
- 按算法主題分類
- 生成 Markdown 格式的索引文件
- 統計完成進度

使用方式：
    python scripts/generate_index.py [--output FILE]
"""

import argparse
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import NamedTuple


class ProblemInfo(NamedTuple):
    """題目資訊結構"""

    index: str
    problem_number: str
    title: str
    directory: Path
    difficulty: str
    topics: list[str]
    has_solution: bool
    has_test: bool
    link: str


# 難度對照表
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

# 主題對照表
TOPIC_MAP = {
    "1768": ["Two Pointers", "String"],
    "1071": ["Math", "String"],
    "1431": ["Array"],
    "605": ["Array", "Greedy"],
    "345": ["Two Pointers", "String"],
    "151": ["Two Pointers", "String"],
    "238": ["Array", "Prefix Sum"],
    "334": ["Array", "Greedy"],
    "443": ["Two Pointers", "String"],
    "283": ["Array", "Two Pointers"],
    "392": ["Two Pointers", "String", "Dynamic Programming"],
    "11": ["Array", "Two Pointers", "Greedy"],
    "1679": ["Array", "Hash Table", "Two Pointers", "Sorting"],
    "643": ["Array", "Sliding Window"],
    "1456": ["String", "Sliding Window"],
    "1004": ["Array", "Binary Search", "Sliding Window", "Prefix Sum"],
    "1493": ["Array", "Dynamic Programming", "Sliding Window"],
    "1732": ["Array", "Prefix Sum"],
    "724": ["Array", "Prefix Sum"],
    "2215": ["Array", "Hash Table"],
    "1207": ["Array", "Hash Table"],
    "1657": ["Hash Table", "String", "Sorting"],
    "2352": ["Array", "Hash Table", "Matrix", "Simulation"],
    "2390": ["String", "Stack", "Simulation"],
    "735": ["Array", "Stack", "Simulation"],
    "394": ["String", "Stack", "Recursion"],
    "933": ["Design", "Queue", "Data Stream"],
    "649": ["String", "Greedy", "Queue"],
    "2095": ["Linked List", "Two Pointers"],
    "328": ["Linked List"],
    "206": ["Linked List", "Recursion"],
    "2130": ["Linked List", "Two Pointers", "Stack"],
    "104": ["Tree", "DFS", "BFS", "Binary Tree"],
    "872": ["Tree", "DFS", "Binary Tree"],
    "1448": ["Tree", "DFS", "BFS", "Binary Tree"],
    "437": ["Tree", "DFS", "Binary Tree"],
    "1372": ["Tree", "DFS", "Dynamic Programming", "Binary Tree"],
    "236": ["Tree", "DFS", "Binary Tree"],
    "199": ["Tree", "DFS", "BFS", "Binary Tree"],
    "17": ["Hash Table", "String", "Backtracking"],
    "22": ["String", "Dynamic Programming", "Backtracking"],
    "88": ["Array", "Two Pointers", "Sorting"],
    "27": ["Array", "Two Pointers"],
    "26": ["Array", "Two Pointers"],
    "389": ["Hash Table", "String", "Bit Manipulation", "Sorting"],
    "1749": ["Array", "Dynamic Programming"],
    "873": ["Array", "Hash Table", "Dynamic Programming"],
    "2460": ["Array", "Simulation"],
    "2570": ["Array", "Hash Table", "Two Pointers"],
    "2161": ["Array", "Two Pointers", "Simulation"],
    "1780": ["Math"],
    "2579": ["Math", "Geometry"],
    "2965": ["Array", "Hash Table", "Math", "Matrix"],
    "2523": ["Math", "Number Theory"],
    "3208": ["Array", "Sliding Window"],
    "1079": ["Hash Table", "String", "Backtracking", "Counting"],
    "2698": ["Math", "Backtracking"],
    "1718": ["Array", "Backtracking"],
    "1028": ["String", "Tree", "DFS", "Binary Tree"],
    "889": ["Array", "Hash Table", "Divide and Conquer", "Tree", "Binary Tree"],
    "2467": ["Array", "Tree", "DFS", "BFS", "Graph"],
    "1524": ["Array", "Math", "Dynamic Programming", "Prefix Sum"],
    "2375": ["String", "Backtracking", "Stack", "Greedy"],
    "1415": ["String", "Backtracking"],
    "1980": ["Array", "Hash Table", "String", "Backtracking"],
    "1261": ["Hash Table", "Tree", "DFS", "BFS", "Design", "Binary Tree"],
}


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


def scan_problems(base_dir: Path) -> list[ProblemInfo]:
    """掃描所有題目目錄並收集資訊"""
    problems_dir = base_dir / "Leetcode_重刷紀錄"
    problems = []

    for item in sorted(problems_dir.iterdir()):
        if not item.is_dir() or item.name.startswith("."):
            continue

        parsed = parse_directory_name(item.name)
        if not parsed:
            continue

        index, problem_number, title = parsed
        solution_file = item / "solution.py"
        test_file = item / "test_solution.py"

        difficulty = DIFFICULTY_MAP.get(problem_number, "Medium")
        topics = TOPIC_MAP.get(problem_number, ["Algorithm"])
        link = f"https://leetcode.com/problems/{title.lower().replace(' ', '-').replace('.', '')}/"

        problems.append(
            ProblemInfo(
                index=index,
                problem_number=problem_number,
                title=title,
                directory=item,
                difficulty=difficulty,
                topics=topics,
                has_solution=solution_file.exists(),
                has_test=test_file.exists(),
                link=link,
            )
        )

    return problems


def generate_index_markdown(problems: list[ProblemInfo]) -> str:
    """生成索引 Markdown 內容"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # 統計
    total = len(problems)
    easy = sum(1 for p in problems if p.difficulty == "Easy")
    medium = sum(1 for p in problems if p.difficulty == "Medium")
    hard = sum(1 for p in problems if p.difficulty == "Hard")
    with_solution = sum(1 for p in problems if p.has_solution)
    with_test = sum(1 for p in problems if p.has_test)

    # 按主題分類
    by_topic: dict[str, list[ProblemInfo]] = defaultdict(list)
    for p in problems:
        for topic in p.topics:
            by_topic[topic].append(p)

    # 難度顏色
    difficulty_badge = {
        "Easy": "🟢",
        "Medium": "🟡",
        "Hard": "🔴",
    }

    # 狀態標記
    def status_icon(p: ProblemInfo) -> str:
        if p.has_test:
            return "✅"
        elif p.has_solution:
            return "📝"
        else:
            return "⬜"

    lines = [
        "# LeetCode 題目索引",
        "",
        f"> 自動生成於 {now}",
        "",
        "## 📊 統計總覽",
        "",
        "| 指標 | 數量 |",
        "|------|------|",
        f"| 總題目數 | {total} |",
        f"| 🟢 Easy | {easy} |",
        f"| 🟡 Medium | {medium} |",
        f"| 🔴 Hard | {hard} |",
        f"| 📝 有解答 | {with_solution} |",
        f"| ✅ 有測試 | {with_test} |",
        "",
        "### 進度條",
        "",
        f"解答進度: {with_solution}/{total} ({with_solution * 100 // total}%)",
        "",
        f"```",
        f"[{'█' * (with_solution * 30 // total)}{'░' * (30 - with_solution * 30 // total)}]",
        f"```",
        "",
        f"測試進度: {with_test}/{total} ({with_test * 100 // total}%)",
        "",
        f"```",
        f"[{'█' * (with_test * 30 // total)}{'░' * (30 - with_test * 30 // total)}]",
        f"```",
        "",
        "---",
        "",
        "## 📚 按難度分類",
        "",
    ]

    # 按難度列出
    for difficulty in ["Easy", "Medium", "Hard"]:
        badge = difficulty_badge[difficulty]
        filtered = [p for p in problems if p.difficulty == difficulty]
        lines.append(f"### {badge} {difficulty} ({len(filtered)} 題)")
        lines.append("")
        lines.append("| # | 題號 | 題目 | 狀態 | 主題 |")
        lines.append("|---|------|------|------|------|")

        for p in filtered:
            topics_str = ", ".join(p.topics[:3])
            if len(p.topics) > 3:
                topics_str += "..."
            status = status_icon(p)
            lines.append(
                f"| {p.index} | [{p.problem_number}]({p.link}) | {p.title} | {status} | {topics_str} |"
            )

        lines.append("")

    # 按主題分類
    lines.append("---")
    lines.append("")
    lines.append("## 🏷️ 按主題分類")
    lines.append("")

    # 排序主題（按題目數量降序）
    sorted_topics = sorted(by_topic.items(), key=lambda x: -len(x[1]))

    for topic, topic_problems in sorted_topics:
        lines.append(f"### {topic} ({len(topic_problems)} 題)")
        lines.append("")
        lines.append("| 題號 | 題目 | 難度 | 狀態 |")
        lines.append("|------|------|------|------|")

        for p in sorted(topic_problems, key=lambda x: x.index):
            badge = difficulty_badge[p.difficulty]
            status = status_icon(p)
            lines.append(f"| [{p.problem_number}]({p.link}) | {p.title} | {badge} | {status} |")

        lines.append("")

    # 圖例
    lines.extend(
        [
            "---",
            "",
            "## 📖 圖例",
            "",
            "| 符號 | 意義 |",
            "|------|------|",
            "| ✅ | 有完整測試 |",
            "| 📝 | 僅有解答 |",
            "| ⬜ | 待完成 |",
            "| 🟢 | Easy |",
            "| 🟡 | Medium |",
            "| 🔴 | Hard |",
            "",
        ]
    )

    return "\n".join(lines)


def main():
    """主函數"""
    parser = argparse.ArgumentParser(description="生成 LeetCode 題目索引")
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="PROBLEM_INDEX.md",
        help="輸出文件名（預設：PROBLEM_INDEX.md）",
    )
    args = parser.parse_args()

    base_dir = get_base_dir()
    print(f"掃描專案目錄: {base_dir}")

    problems = scan_problems(base_dir)
    print(f"找到 {len(problems)} 個題目")

    # 生成索引
    content = generate_index_markdown(problems)

    # 寫入文件
    output_path = base_dir / args.output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ 索引已生成: {output_path}")

    # 顯示統計
    easy = sum(1 for p in problems if p.difficulty == "Easy")
    medium = sum(1 for p in problems if p.difficulty == "Medium")
    hard = sum(1 for p in problems if p.difficulty == "Hard")

    print()
    print("📊 統計:")
    print(f"   🟢 Easy: {easy}")
    print(f"   🟡 Medium: {medium}")
    print(f"   🔴 Hard: {hard}")


if __name__ == "__main__":
    main()
