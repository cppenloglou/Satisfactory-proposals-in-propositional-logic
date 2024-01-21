@echo off
setlocal enabledelayedexpansion

REM
set VALIDATOR="..\bcsp_validate.exe"

REM Loop for each method
for %%M in (depth, hill) do (
  REM Loop for each test
  for /l %%i in (1, 1, 26) do (
        set /a "result=%%i * 40 + 160"
    for /l %%t in (1, 1, 10) do (

        REM
        call %VALIDATOR% "..\Tests\test%%i_M!result!_N10_K6_%%t.txt" "..\M200-1200_N10_K6_26_Solved\solution_%%M_test%%i_M!result!_N10_K6_%%t.txt"

        REM Optionally, you can print the return code of the program
        echo Test %%M_%%i: Return Code - !ERRORLEVEL!
    ) 
  )
)
endlocal