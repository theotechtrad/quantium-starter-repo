#!/bin/bash

# Script to automatically run the Dash app test suite
# This script can be integrated into CI/CD pipelines

echo "========================================="
echo "  Quantium Dash App - Test Suite Runner"
echo "========================================="
echo ""

# Step 1: Activate virtual environment
echo "Step 1: Activating virtual environment..."
if [ -d "venv" ]; then
    source venv/Scripts/activate
    echo "✓ Virtual environment activated"
else
    echo "✗ Error: Virtual environment not found!"
    exit 1
fi

echo ""

# Step 2: Run the test suite
echo "Step 2: Running test suite..."
pytest test_app.py -v

# Step 3: Capture exit code
TEST_RESULT=$?

echo ""

# Step 4: Return appropriate exit code
if [ $TEST_RESULT -eq 0 ]; then
    echo "========================================="
    echo "  ✓ ALL TESTS PASSED!"
    echo "========================================="
    exit 0
else
    echo "========================================="
    echo "  ✗ TESTS FAILED!"
    echo "========================================="
    exit 1
fi