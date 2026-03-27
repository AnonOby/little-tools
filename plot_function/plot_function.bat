@echo off
echo ========================================
echo Updating pip and installing/upgrading required packages...
echo ========================================
REM Replace [PATH_TO_PYTHON] with the full path to your Python executable
REM Example: "C:\Python39\python.exe"
"[PATH_TO_PYTHON]" -m pip install --upgrade pip
"[PATH_TO_PYTHON]" -m pip install --upgrade matplotlib numpy scipy sympy
echo.
echo ========================================
echo Starting function plotter...
echo ========================================
REM Replace [PATH_TO_SCRIPT] with the full path to plot_function.py
REM Example: "C:\Users\YourName\scripts\plot_function.py"
"[PATH_TO_PYTHON]" "[PATH_TO_SCRIPT]"
echo.
echo Script finished. Press any key to close this window...
pause > nul
