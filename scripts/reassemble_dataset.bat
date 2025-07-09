@echo off
echo Reassembling dataset chunks back into dataset.csv...
echo.

cd /d "%~dp0"
python reassemble_dataset_binary.py

echo.
pause
