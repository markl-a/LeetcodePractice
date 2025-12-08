"""
Pytest configuration for LeetCode Practice.

This conftest.py handles the module path for each test file,
allowing tests to import from their local solution.py files.
"""

import sys
from pathlib import Path


def pytest_configure(config):
    """Add all problem directories to sys.path during pytest configuration."""
    leetcode_dir = Path(__file__).parent / "Leetcode_重刷紀錄"
    if leetcode_dir.exists():
        for problem_dir in sorted(leetcode_dir.iterdir(), reverse=True):
            if problem_dir.is_dir() and not problem_dir.name.startswith("."):
                path_str = str(problem_dir)
                if path_str not in sys.path:
                    sys.path.insert(0, path_str)


def pytest_runtest_setup(item):
    """
    Before each test, ensure the correct solution module is loaded.
    """
    test_dir = Path(item.fspath).parent
    path_str = str(test_dir)

    # Remove existing solution module to force reimport from correct directory
    modules_to_remove = [key for key in list(sys.modules.keys())
                         if key == "solution" or key.startswith("solution.")]
    for mod in modules_to_remove:
        del sys.modules[mod]

    # Ensure test directory is first in path
    if path_str in sys.path:
        sys.path.remove(path_str)
    sys.path.insert(0, path_str)
