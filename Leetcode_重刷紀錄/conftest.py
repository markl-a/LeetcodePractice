"""
Local conftest for LeetCode problem tests.

Provides utilities for importing solution modules from the same directory as the test file.
"""

import importlib.util
import sys
from pathlib import Path

import pytest


def load_solution_module(test_file_path: str):
    """
    Load the solution.py module from the same directory as the test file.

    Args:
        test_file_path: The __file__ attribute of the test module

    Returns:
        The loaded solution module
    """
    test_dir = Path(test_file_path).parent
    solution_path = test_dir / "solution.py"

    if not solution_path.exists():
        raise FileNotFoundError(f"solution.py not found in {test_dir}")

    # Create a unique module name to avoid conflicts
    module_name = f"solution_{test_dir.name.replace('.', '_').replace(' ', '_')}"

    # Remove any cached version of this specific module
    if module_name in sys.modules:
        del sys.modules[module_name]

    spec = importlib.util.spec_from_file_location(module_name, solution_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module


@pytest.fixture
def solution_module(request):
    """
    Pytest fixture that provides the solution module for the current test file.

    Usage in test files:
        def test_something(solution_module):
            Solution = solution_module.Solution
            sol = Solution()
            ...
    """
    return load_solution_module(request.fspath)
