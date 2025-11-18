#!/bin/bash
# 執行所有測試並生成報告

set -e

echo "🧪 Running tests..."
echo ""

# 執行測試
pytest -v \
    --tb=short \
    --cov=. \
    --cov-report=html \
    --cov-report=term-missing:skip-covered \
    --cov-report=xml

echo ""
echo "✅ Tests completed!"
echo ""
echo "📊 Coverage report generated:"
echo "   - HTML: htmlcov/index.html"
echo "   - XML: coverage.xml"
echo ""
