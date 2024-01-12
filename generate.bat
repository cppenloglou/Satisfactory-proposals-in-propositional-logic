@echo off
setlocal enabledelayedexpansion

REM
set PROGRAM=./generator.py

REM Loop for each test
for /l %%i in (1, 1, 26) do (
    set /a "result=%%i * 40 + 160"
    REM
    call python %PROGRAM% "test%%i_M!result!_N10_K6" "1" "10" "10" !result! "6"

    REM Optionally, you can print the return code of the program
    echo Test %%M_%%i: Return Code - !ERRORLEVEL!
     
)
endlocal