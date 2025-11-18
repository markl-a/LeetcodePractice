# 貢獻指南

感謝你對本專案的貢獻！

## 🚀 如何貢獻

### 1. Fork 專案

點擊右上角的 "Fork" 按鈕

### 2. Clone 到本地

```bash
git clone https://github.com/YOUR_USERNAME/LeetcodePractice.git
cd LeetcodePractice
```

### 3. 創建分支

```bash
git checkout -b feature/your-feature-name
```

### 4. 設置開發環境

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
pre-commit install
```

### 5. 進行修改

#### 添加新題目

每個題目應包含：

1. **solution.py** - 主要解答文件
2. **test_solution.py** - 測試文件

**solution.py 範本**：

```python
"""
[題號]. [題目名稱]

Difficulty: [Easy/Medium/Hard]
Topics: [標籤1, 標籤2]

Problem:
[題目描述]

Example 1:
    Input: [輸入]
    Output: [輸出]
    Explanation: [說明]

Constraints:
    - [約束條件]
"""

from typing import List  # 根據需要導入


class Solution:
    def methodName(self, param: Type) -> ReturnType:
        """
        [方法說明]

        Time Complexity: O(...)
        Space Complexity: O(...)

        Args:
            param: [參數說明]

        Returns:
            [返回值說明]
        """
        # 實作
        pass
```

**test_solution.py 範本**：

```python
"""Tests for LeetCode [題號]. [題目名稱]"""

import pytest
from solution import Solution


class Test[MethodName]:
    """Test cases for [methodName] method"""

    @pytest.fixture
    def solution(self):
        """Create Solution instance"""
        return Solution()

    @pytest.mark.parametrize(
        "input1,input2,expected",
        [
            # Example test cases
            (input1_val, input2_val, expected_val),
            # Edge cases
            # Additional test cases
        ],
    )
    def test_method_name(self, solution, input1, input2, expected):
        """Test methodName with various inputs"""
        assert solution.methodName(input1, input2) == expected
```

### 6. 確保程式碼品質

執行所有檢查：

```bash
# 格式化
black .

# Linting
ruff check .

# 類型檢查
mypy . --ignore-missing-imports

# 執行測試
pytest
```

或使用 pre-commit：

```bash
pre-commit run --all-files
```

### 7. 提交更改

```bash
git add .
git commit -m "feat: add solution for problem [題號]"
```

**Commit 訊息規範**：

- `feat:` 新功能
- `fix:` 修復錯誤
- `docs:` 文檔更新
- `style:` 格式調整
- `refactor:` 重構
- `test:` 測試相關
- `chore:` 其他維護

### 8. 推送到 GitHub

```bash
git push origin feature/your-feature-name
```

### 9. 創建 Pull Request

前往 GitHub 並創建 Pull Request

## 📋 程式碼規範

### Python 風格

- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- 使用 Black 格式化（行寬 100）
- 使用類型註解
- 編寫清晰的 docstrings

### 測試規範

- 每個解答必須有對應的測試
- 測試應包含：
  - 範例測試案例
  - 邊界條件
  - 錯誤情況（如適用）
  - 效能測試（對於複雜解法）
- 測試覆蓋率應盡可能高

### 文檔規範

- 每個解答必須包含複雜度分析
- 使用中文或英文均可，但保持一致
- 複雜的演算法應包含註解說明

## ✅ Pull Request 檢查清單

提交 PR 前請確認：

- [ ] 程式碼已格式化（`black .`）
- [ ] 通過 linting 檢查（`ruff check .`）
- [ ] 通過類型檢查（`mypy .`）
- [ ] 所有測試通過（`pytest`）
- [ ] 添加了適當的測試案例
- [ ] 更新了 README（如有需要）
- [ ] Commit 訊息清晰明確

## 🐛 報告 Bug

請使用 GitHub Issues 報告 bug，並包含：

1. 問題描述
2. 重現步驟
3. 預期行為
4. 實際行為
5. 環境資訊（Python 版本等）

## 💡 建議新功能

歡迎提出新功能建議！請使用 GitHub Issues 並標記為 "enhancement"

## 📝 問題討論

有任何問題都歡迎在 GitHub Issues 中討論！

---

再次感謝你的貢獻！ 🎉
