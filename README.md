# LeetCode Practice 刷題練習

[![Tests](https://github.com/markl-a/LeetcodePractice/workflows/Tests/badge.svg)](https://github.com/markl-a/LeetcodePractice/actions)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

系統化的 LeetCode 刷題紀錄，包含詳細的解題思路、多種解法比較、完整的測試案例。

> 💡 **個人建議**：先開始刷題，再優化流程、方法和各個方面

## 📊 進度總覽

| 類別 | 已完成 | 有測試 | 進度 |
|------|--------|--------|------|
| **總題數** | 67 | 5 | - |
| **標準格式** | 5 | 5 | 🟢 |
| **待轉換** | 62 | 0 | 🟡 |

### 刷題計劃

- [x] **Phase 1**: [LeetCode 75](https://leetcode.com/studyplan/leetcode-75/) (進行中)
- [ ] **Phase 2**: [Top Interview 150](https://leetcode.com/studyplan/top-interview-150/)
- [ ] **Phase 3**: [Top 100 Liked](https://leetcode.com/studyplan/top-100-liked/)
- [ ] **Phase 4**: Sprint Interview 公司特定題目

## 🏗️ 專案結構

```
LeetcodePractice/
├── .github/
│   └── workflows/          # CI/CD 配置
│       └── test.yml        # 自動化測試
├── Leetcode_重刷紀錄/       # LeetCode 題目解答
│   ├── conftest.py         # pytest 配置（動態導入處理）
│   ├── 0001.Problems1768. Merge Strings Alternately/
│   │   ├── solution.py     # 主要解法（含類型註解和docstring）
│   │   ├── test_1768.py    # 完整測試案例（以題號命名）
│   │   └── __init__.py     # Python 包標識
│   └── ...
├── scripts/
│   ├── new_problem.sh      # 創建新題目模板
│   ├── format_code.sh      # 程式碼格式化
│   └── run_tests.sh        # 執行測試
├── conftest.py             # 根目錄 pytest 配置
├── requirements.txt        # Python 依賴
├── pyproject.toml          # 專案配置
└── README.md               # 本文件
```

## 🚀 快速開始

### 環境設置

1. **Clone 專案**
```bash
git clone https://github.com/markl-a/LeetcodePractice.git
cd LeetcodePractice
```

2. **建立虛擬環境**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. **安裝依賴**
```bash
pip install -r requirements.txt
```

### 執行測試

```bash
# 執行所有測試
pytest

# 執行特定題目的測試
pytest "Leetcode_重刷紀錄/0001.Problems1768. Merge Strings Alternately/" -v

# 執行測試並顯示覆蓋率
pytest --cov=. --cov-report=html

# 平行執行測試（加速）
pytest -n auto
```

### 創建新題目

使用腳本快速創建新題目模板：

```bash
# 用法: ./scripts/new_problem.sh <序號> <題號> <題目名稱> [難度]
./scripts/new_problem.sh 68 2574 "Left and Right Sum Differences" easy

# 這會創建：
# - Leetcode_重刷紀錄/0068.Problems2574. Left and Right Sum Differences/
#   ├── solution.py      # 解法模板
#   ├── test_2574.py     # 測試模板
#   └── __init__.py      # 包標識
```

### 程式碼品質檢查

```bash
# 格式化程式碼
black .

# Linting 檢查
ruff check .

# 類型檢查
mypy . --ignore-missing-imports

# 執行所有檢查
black . && ruff check . && mypy .
```

### 設置 Pre-commit Hooks

```bash
# 安裝 pre-commit
pip install pre-commit

# 設置 hooks
pre-commit install

# 手動執行所有 hooks
pre-commit run --all-files
```

## 📝 題目列表

### Array / String

| # | 題目 | 難度 | 解法 | 測試 | 標籤 |
|---|------|------|------|------|------|
| 1768 | [Merge Strings Alternately](Leetcode_重刷紀錄/0001.Problems1768.%20Merge%20Strings%20Alternately/) | 🟢 Easy | ✅ | ✅ | Two Pointers, String |
| 1071 | [Greatest Common Divisor of Strings](Leetcode_重刷紀錄/0002.Problems1071.%20Greatest%20Common%20Divisor%20of%20Strings/) | 🟢 Easy | ✅ | ✅ | String, Math |
| 1431 | [Kids With the Greatest Number of Candies](Leetcode_重刷紀錄/0003.Problems1431.%20Kids%20With%20the%20Greatest%20Number%20of%20Candies/) | 🟢 Easy | ✅ | ✅ | Array |
| 605 | [Can Place Flowers](Leetcode_重刷紀錄/0004.Problems605.%20Can%20Place%20Flowers/) | 🟢 Easy | ✅ | ✅ | Array, Greedy |
| 345 | [Reverse Vowels of a String](Leetcode_重刷紀錄/0005.Problems345.%20Reverse%20Vowels%20of%20a%20String/) | 🟢 Easy | ✅ | ✅ | Two Pointers, String |

### Two Pointers

### Sliding Window

### Prefix Sum

### Hash Map / Set

### Stack

### Queue

### Linked List

### Binary Tree - DFS

### Binary Tree - BFS

### Graph - DFS

### Graph - BFS

### Heap / Priority Queue

### Binary Search

### Backtracking

### Dynamic Programming

### Trie

### Intervals

### Monotonic Stack

### Bit Manipulation

## 📚 解法特色

每個題目都包含：

1. **📖 完整題目描述**
   - 題目難度和主題標籤
   - 詳細的問題陳述
   - 多個範例和約束條件

2. **💡 多種解法**
   - 最優解法（時間/空間複雜度最佳）
   - 替代解法（不同思路）
   - 暴力解法（教學用途）

3. **📊 複雜度分析**
   - 時間複雜度 (Time Complexity)
   - 空間複雜度 (Space Complexity)

4. **🔍 類型註解**
   - 完整的 Python type hints
   - 清晰的函數簽名

5. **📝 詳細註解**
   - Docstrings 說明
   - 關鍵步驟註解

6. **✅ 完整測試**
   - 範例測試案例
   - 邊界條件測試
   - 大規模測試
   - 效能測試

## 🛠️ 技術棧

- **語言**: Python 3.8+
- **測試**: pytest, pytest-cov
- **程式碼品質**: Black, Ruff, mypy
- **CI/CD**: GitHub Actions
- **版本控制**: Git

## 📖 其他資源

### 1. Crack the Coding Interview, 6th Edition

主要是每章節的筆記心得，範例以外面開源的相通範例為主。

- 📕 [英文原版 PDF](http://www.crackingthecodinginterview.com/)
- 📗 [中文翻譯 GitHub](https://github.com/careercup/CtCI-6th-Edition-Python)

### 2. Leetcode_重刷紀錄

系統化的 LeetCode 解題紀錄，包含詳細解答和測試。

### 3. 刷題實戰筆記

實戰心得和解題技巧總結。

**參考資源**：
- [LeetCode Solutions (Java/Python)](https://walkccc.me/LeetCode/)
- [LeetCode 101](https://github.com/changgyhub/leetcode_101)
- [代碼隨想錄](https://programmercarl.com/)

## 🤝 貢獻

歡迎提交 Issue 或 Pull Request！

## 📄 授權

本專案採用 [MIT License](LICENSE)

---

⭐ 如果這個專案對你有幫助，歡迎給個 Star！

**Happy Coding! 💻**
