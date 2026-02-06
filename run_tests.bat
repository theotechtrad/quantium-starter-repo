@echo off
REM Script to automatically run the Dash app test suite

echo =========================================
echo   Quantium Dash App - Test Suite Runner
echo =========================================
echo.

REM Step 1: Activate virtual environment
echo Step 1: Activating virtual environment...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    echo [32m√ Virtual environment activated[0m
) else (
    echo [31m× Error: Virtual environment not found![0m
    exit /b 1
)

echo.

REM Step 2: Run the test suite
echo Step 2: Running test suite...
pytest test_app.py -v

REM Step 3: Check if tests passed
if %ERRORLEVEL% EQU 0 (
    echo.
    echo =========================================
    echo   [32m√ ALL TESTS PASSED![0m
    echo =========================================
    exit /b 0
) else (
    echo.
    echo =========================================
    echo   [31m× TESTS FAILED![0m
    echo =========================================
    exit /b 1
)