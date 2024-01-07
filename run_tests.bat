@echo off
setlocal enabledelayedexpansion
REM Set the path to your C program
set PROGRAM=bcsp.exe

REM Loop for each method
for %%M in (depth, hill) do (
  REM Loop for each test
  for /l %%i in (1, 1, 8) do (
        set /a "result=%%i * 1000 + 9000"
    for /l %%t in (1, 1, 10) do (

        REM Run the program with the specified method, random numbers as strings, and write the output to a file
        call %PROGRAM% %%M "test%%i_M!result!_N20_K10_%%t.txt" "solution_%%M_test%%i_M!result!_N20_K10_%%t.txt"

        REM Optionally, you can print the return code of the program
        echo Test %%M_%%i: Return Code - !ERRORLEVEL!
    ) 
  )
)
endlocal