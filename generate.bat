@echo off
setlocal enabledelayedexpansion

REM
set PROGRAM=./generator.py

REM Loop for each test
for /l %%i in (1, 1, 8) do (
    set /a "result=%%i * 1000 + 9000"
    REM
    call python %PROGRAM% "test%%i_M!result!_N20_K10" "1" "10" "20" !result! "10"

    REM Optionally, you can print the return code of the program
    echo Test %%M_%%i: Return Code - !ERRORLEVEL!
     
)
endlocal