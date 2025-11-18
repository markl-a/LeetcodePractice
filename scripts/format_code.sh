#!/bin/bash
# 格式化和檢查程式碼

set -e

echo "🎨 Formatting code with Black..."
black .

echo ""
echo "🔍 Linting with Ruff..."
ruff check . --fix

echo ""
echo "📝 Type checking with mypy..."
mypy . --ignore-missing-imports || true

echo ""
echo "✅ Code formatting and checks completed!"
